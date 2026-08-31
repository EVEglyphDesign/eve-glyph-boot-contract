# Sovereign-starter geometry — EgD-GEO-002

Binding on any agent drawing, redrawing, embedding, or citing the
sovereign-starter triangle diagram — the one that shows **Boot contract,
Canon, Sin registry inside the Repository**. Read this before writing SVG.

If a description of the diagram in this file and the operator's hand-drawn
reference [`skills/sovereign-starter-geometry/reference.jpeg`](./reference.jpeg)
ever disagree, the reference image wins. Look at it.

---

## The one-sentence contract

**The operator's eye and the projected objective sit on opposite sides of the
repository circle. The whole circle of data sits between them. The triangle is
inscribed in the circle with its three vertices — Boot contract, Canon, Sin
registry — on the boundary.**

This is the founding axis of the Theriault Family Method. It is the copyright.
Surfaces that violate it are logged as heritage defects (class **H**) at the top
of `registry/SIN-DEFECTS.md`, not filed as cosmetic drift.

---

## 1. The fixed geometry

The diagram carries four elements that are non-negotiable.

- **The repository** is a dark circle. Ink `#1a1a1a`, stroke 2px. Not a
  whisper (`#e7e1d3`, 1.5px is a defect). The boundary must read as a real
  containing edge or the whole claim collapses.
- **The triangle** is isosceles, inscribed in the repository circle at
  angles **90°, 210°, 330°**. Ink `#1a1a1a`, stroke 2px. Fill `none`.
- **Three vertex dots**, orange `#e87722`, radius 7. Each dot sits *exactly*
  on the circle boundary — it is an intersection point, not a point inside
  the circle.
- **Three vertex labels** in Fraunces 17 / 600 / `#1a1a1a`:
  - **Boot contract** at the top
  - **Canon** at the lower-left
  - **Sin registry** at the lower-right

Vertices are on the boundary because each is a claim the repository makes
against the world: how the surface behaves before it does anything (Boot
contract), how the artifact leaves the repository (Canon), how the truth of
what happened is preserved (Sin registry). A vertex floating inside the
circle is a claim the repository does not touch — which is the opposite of
what the diagram is for.

---

## 2. Canonical coordinates

For the standard `520 × 380` viewBox used on the sovereign-starter page and
in every template.

- Circle centre `(260, 200)`, radius `150`
- Boot contract vertex `(260, 50)` — top of circle, 90°
- Canon vertex `(130, 275)` — lower-left, 210°
- Sin registry vertex `(390, 275)` — lower-right, 330°

Verify the vertices are on the boundary by evaluating
`(x − 260)² + (y − 200)² = 150² = 22500` for each — every vertex satisfies
it exactly. If a vertex fails this check, the geometry is wrong and the
correction is coordinate arithmetic, not visual eyeballing.

If a surface uses a different viewBox, scale from these numbers by the same
ratio and re-verify the on-boundary check. Do not eyeball.

---

## 3. Reference SVG snippet

Paste this straight into any surface that needs the base diagram. Add axes,
operator dot, and star on top; never edit the base coordinates.

```svg
<svg viewBox="0 0 520 380" xmlns="http://www.w3.org/2000/svg"
     role="img" aria-labelledby="tri-title tri-desc">
  <title id="tri-title">Boot contract, Canon and Sin registry inscribed in the repository circle</title>
  <desc id="tri-desc">A dark circle labelled the repository contains an isosceles triangle whose three vertices sit on the boundary of the circle: Boot contract at the top, Canon at the lower left, Sin registry at the lower right.</desc>

  <!-- repository circle - ink 2px, a real boundary -->
  <circle cx="260" cy="200" r="150" fill="none" stroke="#1a1a1a" stroke-width="2"/>
  <text x="260" y="368" text-anchor="middle"
        font-family="Fraunces, Georgia, serif" font-size="13"
        font-style="italic" fill="#6b665c">the repository</text>

  <!-- triangle inscribed in the circle -->
  <polygon points="260,50 130,275 390,275"
           fill="none" stroke="#1a1a1a" stroke-width="2"/>

  <!-- vertex dots, each ON the boundary -->
  <circle cx="260" cy="50"  r="7" fill="#e87722"/>
  <circle cx="130" cy="275" r="7" fill="#e87722"/>
  <circle cx="390" cy="275" r="7" fill="#e87722"/>

  <!-- vertex labels -->
  <text x="260" y="32"  text-anchor="middle"
        font-family="Fraunces, Georgia, serif" font-size="17"
        font-weight="600" fill="#1a1a1a">Boot contract</text>
  <text x="112" y="300" text-anchor="middle"
        font-family="Fraunces, Georgia, serif" font-size="17"
        font-weight="600" fill="#1a1a1a">Canon</text>
  <text x="408" y="300" text-anchor="middle"
        font-family="Fraunces, Georgia, serif" font-size="17"
        font-weight="600" fill="#1a1a1a">Sin registry</text>

  <!-- Founding axis (§0.1 of the boot contract, §4 of this skill).
       The operator's eye and the projected objective sit on opposite sides
       of the repository circle. The line between them passes through the
       whole circle of data. Do NOT ship this diagram without both marks. -->

  <!-- Operator's eye — blue X, lower-left, outside the circle. -->
  <g stroke="#1e5fb3" stroke-width="6" stroke-linecap="round" fill="none">
    <line x1="40"  y1="315" x2="80"  y2="355"/>
    <line x1="80"  y1="315" x2="40"  y2="355"/>
  </g>
  <text x="30" y="338" text-anchor="middle"
        font-family="Fraunces, Georgia, serif" font-size="22"
        font-weight="700" fill="#1e5fb3">*</text>

  <!-- Projected objective — red X, upper-right, outside the circle. -->
  <g stroke="#c8102e" stroke-width="6" stroke-linecap="round" fill="none">
    <line x1="440" y1="45"  x2="480" y2="85"/>
    <line x1="480" y1="45"  x2="440" y2="85"/>
  </g>
</svg>
```

---

## 4. The founding axis — sealed 2026-08-30

The operator sealed the founding axis by hand-drawing it twice, on 2026-08-29
and again on 2026-08-30. Both drawings are the same. This section is now
binding; do not paraphrase.

### 4.1 The two marks

- **The operator's eye** — blue X, outside the circle, on the *lower-left* side
  of the diagram. Beside it, an asterisk `*` in the same blue: the operator's
  own mark. This is the reader. This is the sovereign human. This is the axis
  origin.
- **The projected objective** — red X, outside the circle, on the *upper-right*
  side of the diagram. Diagonally opposite the operator's eye. This is world
  peace. This is *pour le bien-être du peuple*. This is the direction the
  operator's data is aimed.

### 4.2 The two rules

1. **Opposite sides.** The two marks are on opposite sides of the circle. Not
   the same side, not one inside and one outside, not both floating in the
   corner. The straight line drawn from the operator's eye to the objective
   must pass through the interior of the repository circle. If it doesn't,
   the diagram is claiming AI can reach the objective without going through
   the operator's data — which is the drift this whole method exists to stop.
2. **Outside the boundary.** Both marks are *outside* the repository circle,
   not on it and not inside it. The vertex dots (Boot contract, Canon, Sin
   registry) are the only marks that sit on the boundary. The operator and the
   objective are on the other side of the boundary from the machine's
   internals — the operator, because they are the sovereign human the machine
   serves; the objective, because it is the world the machine is aimed at, not
   the world the machine already contains.

### 4.3 Canonical coordinates (viewBox `520 × 380`)

Both marks sit clear of the `r=150` circle centred at `(260, 200)`, so both
distances-from-centre must exceed `150`.

- **Operator's eye** — blue X centred at `(60, 335)`. Distance from centre:
  √(200² + 135²) ≈ 241, well outside the boundary. Asterisk `*` at
  `(30, 330)` in the same blue, just to the left of the X.
- **Projected objective** — red X centred at `(460, 65)`. Distance from centre:
  √(200² + 135²) ≈ 241, symmetric with the operator's eye across the circle
  centre. Diagonally opposite by construction.

Colours are the hand-drawn colours, not a re-interpretation:

- Operator blue `#1e5fb3` — the calm blue of the reference drawing.
- Objective red `#c8102e` — the pirate red already in use for the handshake
  screenshots. Matches the reference drawing.

Both marks are drawn as **X** strokes (two crossed lines), not as dots and not
as glyphs. Stroke width 6, `stroke-linecap="round"`. Each X spans roughly 40
units corner-to-corner.

### 4.4 What the marks are, in one sentence each

- **Operator's eye.** "That's who you are, what you want." The sovereign human,
  outside the machine, looking in.
- **Projected objective.** "The direction you're aiming." World peace, safety
  first, betterment second.

---

## 5. Defect classes for this diagram

Failing any of the following is a defect against this skill. Log with the
class listed, in `registry/SIN-DEFECTS.md` in the boot-contract repository.

| # | Defect | Class |
|---|--------|-------|
| 1 | Diagram shipped without the operator's eye and the projected objective on opposite sides of the circle | **H** — heritage; violates §0.1 of the boot contract |
| 2 | Operator's eye or objective drawn on the same side of the circle, or both floating in the same corner | **H** — heritage; the axis-through-the-repository is the copyright |
| 3 | Operator's eye or objective drawn inside or on the boundary instead of outside it | **H** — heritage |
| 4 | Vertex not on the repository boundary (fails the `(x−260)² + (y−200)² = 22500` check) | **T** — drift, wrong artifact shape |
| 5 | Repository circle drawn as a whisper (light stroke, thin, less than 2px ink) | **C** — canon breach |
| 6 | Triangle floating inside the circle with visible padding between vertices and boundary | **T** — drift |
| 7 | Vertex labels rearranged (Canon in a position other than lower-left, etc.) | **C** — canon breach |
| 8 | Redrawing the same geometry a fourth time from prose after three redraws diverged | **R** — retrieval waste; the correct input format is the drawing, not more prose |
| 9 | Redrawing without first reading every image in `uploaded_attachments/` on the working turn | **R** — retrieval waste, unread references |

---

## 6. When this skill loads

Any agent working on any of the following surfaces must load this skill
before writing SVG:

- The sovereign-starter public page (`sovereign-starter/docs/index.html`)
- Any EVEglyphDesign essay, PDF or presentation that carries the triangle
- Any preview deployment of the above

Agents preparing other geometric diagrams (the EVE Glyph umbrella-and-knight
mark, the Knight Triangle, etc.) load their own skill files — this one is
specific to the Boot-contract / Canon / Sin-registry / Repository diagram.

---

## Canonical copies

- Machine copy: <https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/skills/sovereign-starter-geometry/SKILL.md>
- Reference image: <https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/skills/sovereign-starter-geometry/reference.jpeg>
- Template SVG: <https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/skills/sovereign-starter-geometry/template.svg>

If this skill and the reference image ever disagree, the reference image
wins. Fetch it — that is a rung-4 read and it is cheap.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
