# Sovereign-starter geometry — EgD-GEO-003

Binding on any agent drawing, redrawing, embedding, or citing the
sovereign-starter triangle diagram — the one that shows **Boot contract,
Canon, Sin registry inside the Repository**. Read this before writing SVG.

If a description of the diagram in this file and the operator's hand-drawn
reference [`skills/sovereign-starter-geometry/reference.jpeg`](./reference.jpeg)
ever disagree, the reference image wins. Look at it.

---

## The one-sentence contract

**The operator sits on one side of the repository, the objective on the other,
both marked with a single asterisk in ink. The whole circle of data sits
between them. The triangle is a prism inscribed in the circle — Boot contract,
Canon and Sin registry are three aspects of the operator's rules, refracted —
and the operator looks *through* the prism to see the objective.**

This is the founding axis of the Theriault Family Method. It is the copyright.
Surfaces that violate it are logged as heritage defects (class **H**) at the top
of `registry/SIN-DEFECTS.md`, not filed as cosmetic drift.

Business terms only on the surface: `the operator` on one side, `the objective`
on the other. The metaphysics (world peace, *pour le bien-être du peuple*) live
in the boot contract prose — not on the blueprint.

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
       The operator and the objective sit on opposite sides of the repository
       circle, each a single ink asterisk. The line between them passes
       through the whole circle of data. Do NOT ship this diagram without
       both marks, do NOT use colour, do NOT use X strokes, do NOT put
       'world peace' on the surface. -->

  <!-- Operator - single ink asterisk, lower-left, outside the circle -->
  <text x="60" y="330" text-anchor="middle" dominant-baseline="middle"
        font-family="Fraunces, Georgia, serif" font-size="40"
        font-weight="700" fill="#1a1a1a">*</text>
  <text x="60" y="365" text-anchor="middle"
        font-family="Fraunces, Georgia, serif" font-size="12"
        font-style="italic" fill="#1a1a1a">the operator</text>

  <!-- Objective - single ink asterisk, upper-right, outside the circle -->
  <text x="460" y="70" text-anchor="middle" dominant-baseline="middle"
        font-family="Fraunces, Georgia, serif" font-size="40"
        font-weight="700" fill="#1a1a1a">*</text>
  <text x="460" y="35" text-anchor="middle"
        font-family="Fraunces, Georgia, serif" font-size="12"
        font-style="italic" fill="#1a1a1a">the objective</text>
</svg>
```

---

## 4. The founding axis — sealed 2026-08-30

The operator sealed the founding axis by hand-drawing it twice, on 2026-08-29
and again on 2026-08-30. Both drawings are the same. This section is now
binding; do not paraphrase.

### 4.1 The two marks

- **The operator** — a single ink asterisk `*`, outside the circle, on the
  *lower-left* side of the diagram. Below it, the label `the operator` in
  italic Fraunces. This is the reader. This is the sovereign human. This is
  the axis origin. Nothing else at this position — no X, no dot, no colour.
- **The objective** — a single ink asterisk `*`, outside the circle, on the
  *upper-right* side of the diagram. Above it, the label `the objective` in
  italic Fraunces. Diagonally opposite the operator. This is the direction
  the operator's data is aimed. Nothing else — no X, no dot, no colour, no
  metaphysical label. Blueprints use business terms.

### 4.2 The four rules

1. **Opposite sides.** The two marks are on opposite sides of the circle. Not
   the same side, not one inside and one outside, not both floating in the
   corner. The straight line drawn from the operator through the objective
   must pass through the interior of the repository circle. If it doesn't,
   the diagram is claiming AI can reach the objective without going through
   the operator's data — which is the drift this whole method exists to stop.
2. **Outside the boundary.** Both marks are *outside* the repository circle,
   not on it and not inside it. The vertex dots (Boot contract, Canon, Sin
   registry) are the only marks that sit on the boundary.
3. **One asterisk per side.** Not an X, not a dot, not a compound glyph. A
   single Fraunces asterisk in ink, sized to read at diagram scale. Symmetric
   in size, symmetric in weight, symmetric in colour — the two sides are
   equivalent-and-opposite, so their marks are visually equivalent.
4. **Ink only.** Both marks are ink `#1a1a1a`. Not blue, not red, not any
   accent colour. The brand carries cream and orange; blue and red are not
   in the palette. The reference-drawing colours were the operator marking
   *the diagram*, not marking *for the diagram*. This is a common misreading
   — do not repeat it.

### 4.3 Canonical coordinates (viewBox `520 × 380`)

Both marks sit clear of the `r=150` circle centred at `(260, 200)`, so both
distances-from-centre must exceed `150`. Positions are symmetric through the
circle centre — reflecting one across `(260, 200)` gives the other exactly.

- **Operator asterisk** — ink `*` centred at `(60, 330)`, font-size 40,
  Fraunces 700, `text-anchor="middle"`, `dominant-baseline="middle"`. Distance
  from centre: √(200² + 130²) ≈ 239, well outside the boundary.
- **Operator label** — `the operator` in Fraunces 12 italic, ink, centred at
  `(60, 365)`. Below the asterisk.
- **Objective asterisk** — ink `*` centred at `(460, 70)`, same font metrics
  as the operator asterisk. Diagonally opposite by construction.
- **Objective label** — `the objective` in Fraunces 12 italic, ink, centred at
  `(460, 35)`. Above the asterisk.

### 4.4 The prism reading

The triangle is a prism. The operator looks *through* the prism at the
objective. Boot contract, Canon and Sin registry are three aspects of the
operator's rules, refracted by the same medium — the repository — into a
single line of sight that reaches the objective safely.

- **Aspects, not process.** The three vertices are three views of one thing.
  A process implies steps in time; the diagram is a single moment held under
  the operator's rules. Language that describes them as a workflow is wrong.
- **Boot contract.** How the operator expects the machine to behave before it
  touches anything.
- **Canon.** How the artifact leaves the repository.
- **Sin registry.** How the truth of what happened is preserved so it can be
  done right next time.

### 4.5 What the marks are, in business terms

- **The operator.** The sovereign human. The reader of the diagram.
- **The objective.** What the operator is aiming at. The label on the surface
  is `the objective` — nothing more specific. What the objective actually *is*
  (world peace, *pour le bien-être du peuple*, safety first and betterment
  second) lives in §0.1 of the boot contract, not on the blueprint.

---

## 5. Defect classes for this diagram

Failing any of the following is a defect against this skill. Log with the
class listed, in `registry/SIN-DEFECTS.md` in the boot-contract repository.

| # | Defect | Class |
|---|--------|-------|
| 1 | Diagram shipped without the operator and the objective on opposite sides of the circle | **H** — heritage; violates §0.1 of the boot contract |
| 2 | Operator or objective drawn on the same side of the circle, or both floating in the same corner | **H** — heritage; the axis-through-the-repository is the copyright |
| 3 | Operator or objective drawn inside or on the boundary instead of outside it | **H** — heritage |
| 4 | Either mark drawn as an X, a compound glyph, or anything other than a single Fraunces asterisk | **H** — heritage; symmetric single asterisks on both sides |
| 5 | Either mark drawn in colour (blue, red, green, or any accent). Both are ink `#1a1a1a`. | **C** — canon breach; brand palette is cream and orange only |
| 6 | Objective labelled "world peace" or any metaphysical term on the surface itself. Label is `the objective`. | **H** — heritage; blueprints use business terms |
| 7 | Vertex not on the repository boundary (fails the `(x−260)² + (y−200)² = 22500` check) | **T** — drift, wrong artifact shape |
| 8 | Repository circle drawn as a whisper (light stroke, thin, less than 2px ink) | **C** — canon breach |
| 9 | Triangle floating inside the circle with visible padding between vertices and boundary | **T** — drift |
| 10 | Vertex labels rearranged (Canon in a position other than lower-left, etc.) | **C** — canon breach |
| 11 | Vertices described as steps in a process rather than aspects of one thing (workflow language) | **H** — heritage; aspects, not process |
| 12 | Redrawing the same geometry a fourth time from prose after three redraws diverged | **R** — retrieval waste; the correct input format is the drawing, not more prose |
| 13 | Redrawing without first reading every image in `uploaded_attachments/` on the working turn | **R** — retrieval waste, unread references |

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
