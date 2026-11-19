"""Public-repository name check (EgD-BOOT-017).

Fails when a tracked text file, or a commit message being pushed, contains a
client, partner or person name that must stay in the -private repository.
The names are not stored here: .github/public-denylist.txt holds salted
SHA-256 hashes only. Hashes stop casual reading, not someone who guesses a
name and hashes it.

Usage:
  python .github/public_check.py                 # check working tree
  python .github/public_check.py --rev <sha>     # check files at a commit
  python .github/public_check.py --log A..B      # also check commit messages
  python .github/public_check.py --hash <name>   # print the line to add
"""
import hashlib, pathlib, re, subprocess, sys

SALT = "egd-public-check-v1:"
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
DENY = HERE / "public-denylist.txt"
IGNORE = HERE / "public-check-ignore.txt"
BINARY = re.compile(r"\.(pdf|jpe?g|png|gif|ico|zip|ttf|otf|woff2?)$", re.I)
TOKEN = re.compile(r"[a-z0-9]+")


def h(word):
    return hashlib.sha256((SALT + word.lower()).encode()).hexdigest()


def load():
    word, sub, pair = set(), {}, set()
    for line in DENY.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        kind, digest, *rest = line.split()
        if kind == "w":
            word.add(digest)
        elif kind == "p":
            pair.add(digest)
        elif kind == "s":
            sub.setdefault(int(rest[0]), set()).add(digest)
    return word, sub, pair


def hits(text, word, sub, pair=frozenset()):
    found = set()
    toks = TOKEN.findall(text.lower())
    for a, b in zip(toks, toks[1:]):  # two-word names, kind p
        if h(a + b) in pair:
            found.add(f"{a} {b}")
    for tok in set(toks):
        if h(tok) in word:
            found.add(tok)
        for n, digests in sub.items():
            for i in range(len(tok) - n + 1):
                if h(tok[i:i + n]) in digests:
                    found.add(tok)
                    break
    return found


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                          check=True).stdout


def main(argv):
    if "--hash" in argv:
        name = argv[argv.index("--hash") + 1].lower()
        print(f"w {h(name)}")
        print(f"s {h(name)} {len(name)}   # substring form, for distinctive names")
        print("two-word name: pass it without the space and use p instead of w")
        return 0
    rev = argv[argv.index("--rev") + 1] if "--rev" in argv else None
    log = argv[argv.index("--log") + 1] if "--log" in argv else None
    word, sub, pair = load()
    ignore = set()
    if IGNORE.exists():
        ignore = {l.strip() for l in IGNORE.read_text(encoding="utf-8").splitlines()
                  if l.strip() and not l.startswith("#")}
    skip = {".github/public-denylist.txt", ".github/public-check-ignore.txt"}
    files = git("ls-tree", "-r", "--name-only", rev).decode().splitlines() if rev \
        else git("ls-files").decode().splitlines()
    bad = []
    for f in files:
        if f in skip or f in ignore or BINARY.search(f):
            continue
        try:
            data = git("show", f"{rev}:{f}") if rev else (ROOT / f).read_bytes()
        except Exception:
            continue
        text = data.decode("utf-8", "replace")
        for n, line in enumerate(text.splitlines(), 1):
            found = hits(line, word, sub, pair)
            if found:
                bad.append(f"{f}:{n}: {', '.join(sorted(found))}")
    if log:
        for entry in git("log", "--format=%h%x00%B%x01", *log.split()).decode().split("\x01"):
            if "\x00" not in entry:
                continue
            sha, msg = entry.strip().split("\x00", 1)
            found = hits(msg, word, sub, pair)
            if found:
                bad.append(f"commit {sha} message: {', '.join(sorted(found))}")
    if bad:
        print("Public check FAILED: names that belong in the -private repo (EgD-BOOT-017):")
        print("\n".join(bad))
        print("Fix: replace with role labels (Client C, Dealer group B, Partner T ...),"
              " full text to the -private repo first.")
        return 1
    print(f"Public check OK: {len(files)} files" + (f", commits {log}" if log else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
