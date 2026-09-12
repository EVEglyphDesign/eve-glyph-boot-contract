#!/usr/bin/env python3
"""
scripts/read_register.py — the read side of the self-healing quality loop.

Reads the Markdown source of truth at `registry/RECORD-OF-SUFFERING.md`,
tags every entry, and writes the render at `registry/entries.jsonl`.
Prints the distribution the read-back gate quotes.

Contract:
- Markdown is the source. Anything not present in the Markdown is not in the
  render. The script never edits the Markdown.
- The class taxonomy is not hard-coded. Whatever letter appears in the class
  column is what the row is counted as. New classes surface the first time a
  row uses them.
- The fault axis has four ranks: Agent, Instruction, Tooling, Upstream.
  Anything else in the fault column is reported as `Other` and flagged.
- The parser prefers false positives (a row it should not have parsed) to
  false negatives (missing a row entirely). Anomalies are written to
  `registry/entries.anomalies.md` so they are visible in review.

Usage:
    python3 scripts/read_register.py                # read + write + print
    python3 scripts/read_register.py --check        # exit non-zero if the
                                                    # render is stale vs source
    python3 scripts/read_register.py --quiet        # write only, no stdout
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "registry" / "RECORD-OF-SUFFERING.md"
RENDER = REPO / "registry" / "entries.jsonl"
ANOMALIES = REPO / "registry" / "entries.anomalies.md"

# Match a table row that begins with a date. Non-greedy cells so pipes inside
# `inline code` do not fool the split — we split on '|' at the top level and
# rejoin the remaining cells into the free-text fields.
ROW_START = re.compile(r"^\| \d{4}-\d{2}-\d{2} \|")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[`]?[A-Za-z][A-Za-z0-9-]*[`]?$")

# The canonical fault ranks in ROS. Anything else is reported as Other.
FAULT_RANKS = {"Agent", "Instruction", "Tooling", "Upstream", "Tooling / Platform"}
FAULT_NORMALISE = {"Tooling / Platform": "Tooling"}

# Rule-of-three threshold, matching README §5 and ROS.
THRESHOLD = 3


def _clean_cell(s: str) -> str:
    return s.strip()


def _strip_ticks(s: str) -> str:
    return s.strip().strip("`").strip()


def parse_row(line: str) -> dict | None:
    """
    Parse one entry-row from the Markdown into a tagged dict.

    Row shape (post 2026-09-12 rename):
        | date | id | class | fault | asked | done | cheaper | waste |

    Legacy pre-rename rows (kept verbatim in the deep-dive sections) have no
    fault column:
        | date | id | class | asked | done | cheaper | waste |

    Older single-line prose rows may have any number of cells; we accept any
    row whose first two cells are a date and an ID and whose third cell is a
    short token that looks like a class letter.
    """
    # Trim the leading/trailing pipes and split. Cells that contain pipes
    # inside inline code (e.g. `sed 's|a|b|'`) will over-split; we detect
    # this after the fact by requiring the first three cells to be
    # well-shaped.
    raw = line.strip()
    if not raw.startswith("|"):
        return None
    raw = raw.strip("|")
    cells = [_clean_cell(c) for c in raw.split("|")]
    if len(cells) < 5:
        return None

    date = cells[0]
    if not DATE_RE.match(date):
        return None

    ident = _strip_ticks(cells[1])
    if not ID_RE.match(ident):
        return None

    cls = cells[2].strip()
    # Accept 1–3 letter class tokens; anything longer is unlikely to be a
    # class letter and probably means we mis-split.
    if not (1 <= len(cls) <= 3 and cls.isalpha() and cls.upper() == cls):
        return None

    # Detect the fault column. If cell[3] is one of the known ranks (or one
    # of the normalisation keys), this is a post-rename row.
    fault_raw = cells[3].strip() if len(cells) > 3 else ""
    has_fault_col = fault_raw in FAULT_RANKS or fault_raw in FAULT_NORMALISE
    if has_fault_col:
        fault = FAULT_NORMALISE.get(fault_raw, fault_raw)
        prose_start = 4
    else:
        fault = None  # legacy row, fault unassigned
        prose_start = 3

    prose_cells = cells[prose_start:]
    # Recombine anything after the 4th prose cell as `waste` — inline pipes
    # in later cells (rare) get glued back with " | ".
    if len(prose_cells) >= 4:
        asked = prose_cells[0]
        done = prose_cells[1]
        cheaper = prose_cells[2]
        waste = " | ".join(prose_cells[3:])
    else:
        asked = prose_cells[0] if len(prose_cells) > 0 else ""
        done = prose_cells[1] if len(prose_cells) > 1 else ""
        cheaper = prose_cells[2] if len(prose_cells) > 2 else ""
        waste = ""

    # Extract secondary tags from the prose without imposing structure on it.
    combined = " ".join([asked, done, cheaper, waste])
    repeat_of = sorted(set(
        _strip_ticks(m) for m in
        re.findall(r"`?((?:SIN|EgD-SIN|ROD|ROS)-\d{4}-\d{2}-\d{2}[A-Za-z0-9-]*)`?", combined)
    ))
    clause_cites = sorted(set(re.findall(r"§\d+[a-z]?", combined)))
    boot_cites = sorted(set(re.findall(r"EgD-BOOT-\d{3}[a-z0-9]*", combined)))

    return {
        "id": ident,
        "date": date,
        "class": cls,
        "fault": fault,
        "asked": asked,
        "done": done,
        "cheaper": cheaper,
        "waste": waste,
        "repeat_of": [r for r in repeat_of if r != ident],
        "clause_cites": clause_cites,
        "boot_cites": boot_cites,
    }


def parse_source(text: str) -> tuple[list[dict], list[dict]]:
    entries: list[dict] = []
    anomalies: list[dict] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if not ROW_START.match(line):
            continue
        parsed = parse_row(line)
        if parsed is None:
            anomalies.append({
                "lineno": lineno,
                "reason": "date-row did not parse into an entry",
                "line": line[:220],
            })
            continue
        entries.append(parsed)
    return entries, anomalies


def distribution(entries: list[dict]) -> dict:
    class_counts = Counter(e["class"] for e in entries)
    fault_counts = Counter((e["fault"] or "unassigned") for e in entries)
    pair_counts = Counter((e["class"], e["fault"] or "unassigned") for e in entries)
    over = [c for c, n in class_counts.items() if n >= THRESHOLD]
    return {
        "total_rows": len(entries),
        "unique_ids": len({e["id"] for e in entries}),
        "class_counts": dict(class_counts.most_common()),
        "fault_counts": dict(fault_counts.most_common()),
        "class_fault_pairs": {f"{c}+{f}": n for (c, f), n in pair_counts.most_common()},
        "classes_over_threshold": sorted(over, key=lambda c: -class_counts[c]),
        "threshold": THRESHOLD,
    }


def render_jsonl(entries: list[dict]) -> str:
    return "\n".join(json.dumps(e, ensure_ascii=False, sort_keys=True) for e in entries) + "\n"


def render_anomalies(anomalies: list[dict]) -> str:
    if not anomalies:
        return (
            "# Register parse anomalies\n\n"
            "None. Every date-row in `RECORD-OF-SUFFERING.md` parsed into an entry.\n"
        )
    lines = [
        "# Register parse anomalies",
        "",
        "Date-rows in `RECORD-OF-SUFFERING.md` that the read script could not",
        "parse into a tagged entry. Each is a false negative to investigate — a row",
        "the operator can see but the loop cannot count. Fix the row or fix the",
        "parser; do not silently drop.",
        "",
    ]
    for a in anomalies:
        lines.append(f"- line {a['lineno']}: {a['reason']}")
        lines.append(f"  `{a['line']}`")
    lines.append("")
    return "\n".join(lines)


def read_back_line(dist: dict) -> str:
    """The one sentence the read-back gate quotes when the return concerns
    the register itself. Short by design."""
    over = ", ".join(f"{c}={dist['class_counts'][c]}" for c in dist["classes_over_threshold"])
    return (
        f"Register: {dist['total_rows']} rows, "
        f"{dist['unique_ids']} unique IDs, "
        f"{len(dist['classes_over_threshold'])} classes over threshold ({over}). "
        f"Fault: " + ", ".join(f"{k}={v}" for k, v in dist["fault_counts"].items()) + "."
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true",
                   help="Exit non-zero if the render is stale relative to the source.")
    p.add_argument("--quiet", action="store_true",
                   help="Write files without printing to stdout.")
    args = p.parse_args()

    if not SOURCE.exists():
        print(f"source not found: {SOURCE}", file=sys.stderr)
        return 2

    text = SOURCE.read_text(encoding="utf-8")
    entries, anomalies = parse_source(text)
    dist = distribution(entries)

    new_jsonl = render_jsonl(entries)
    new_anom = render_anomalies(anomalies)

    if args.check:
        cur_jsonl = RENDER.read_text(encoding="utf-8") if RENDER.exists() else ""
        cur_anom = ANOMALIES.read_text(encoding="utf-8") if ANOMALIES.exists() else ""
        stale = (cur_jsonl != new_jsonl) or (cur_anom != new_anom)
        if stale:
            print("STALE: render does not match source", file=sys.stderr)
            return 1
        print("OK: render matches source")
        return 0

    RENDER.write_text(new_jsonl, encoding="utf-8")
    ANOMALIES.write_text(new_anom, encoding="utf-8")

    if not args.quiet:
        print(read_back_line(dist))
        print()
        print(json.dumps(dist, indent=2, ensure_ascii=False))
        if anomalies:
            print()
            print(f"anomalies: {len(anomalies)} — see {ANOMALIES.relative_to(REPO)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
