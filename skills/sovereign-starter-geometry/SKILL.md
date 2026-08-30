# Sovereign-starter geometry — EgD-GEO-001

Binding on any agent drawing, redrawing, embedding, or citing the
sovereign-starter triangle diagram — the one that shows **Boot contract,
Canon, Sin registry inside the Repository**. Read this before writing SVG.

If a description of the diagram in this file and the operator's hand-drawn
reference [`skills/sovereign-starter-geometry/reference.jpeg`](./reference.jpeg)
ever disagree, the reference image wins. Look at it.

---

## The one-sentence contract

**The triangle is inscribed in the repository circle. The three vertices sit
ON the boundary, not floating inside it. Everything else — axes, operator,
star — is drawn on top of that fact.**

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
</svg>
```

---

## 4. What is not yet sealed

The following elements have been described in prose but not yet drawn by the
operator. Do not invent placements — ask, or hand back
[`skills/sovereign-starter-geometry/template.svg`](./template.svg) so the
operator can draw once and every agent thereafter matches.

- **The red axis** — the operator's line. Runs through Canon. Canon is
  what the operator uses to find the light. Exact entry vertex, exit
  vertex and slope: **not sealed.**
- **The blue axis** — the outcome's line. The ideal blue contrast. Passes
  through the bifurcation. Exact placement: **not sealed.**
- **The bifurcation** — the point where the operator's line and the
  outcome's line part ways. Position: **not sealed.**
- **The operator dot** — the bifurcation is where it sits, once the axes
  are sealed.
- **The outcome star** — outside the circle, on the blue axis extended.
  Exact position: **not sealed.**

When the operator seals these, this skill upgrades to `EgD-GEO-002` and the
reference SVG in §3 is amended. Until then, ship the base diagram plus a
note that the axes are drawn separately — not a guessed version.

---

## 5. Defect classes for this diagram

Failing any of the following is a defect against this skill. Log with the
class listed, in `registry/SIN-DEFECTS.md` in the boot-contract repository.

| # | Defect | Class |
|---|--------|-------|
| 1 | Vertex not on the repository boundary (fails the `(x−260)² + (y−200)² = 22500` check) | **T** — drift, wrong artifact shape |
| 2 | Repository circle drawn as a whisper (light stroke, thin, less than 2px ink) | **C** — canon breach |
| 3 | Triangle floating inside the circle with visible padding between vertices and boundary | **T** — drift |
| 4 | Vertex labels rearranged (Canon in a position other than lower-left, etc.) | **C** — canon breach |
| 5 | Axes, operator dot, or star placed from prose without the operator's hand-drawn seal | **T** — drift, geometry-from-prose |
| 6 | Redrawing the same geometry a fourth time from prose after three redraws diverged | **R** — retrieval waste; the correct input format is the drawing, not more prose |
| 7 | Redrawing without first reading every image in `uploaded_attachments/` on the working turn | **R** — retrieval waste, unread references |

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
