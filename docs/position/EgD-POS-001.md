# The Additive Position

**Document ID** `EgD-POS-001` · **Key ID** `EgD-KEY-2026-07` · **Status** position paper, v2.0

Who EVEglyph Design technology is made available to, on what terms, and how it enters an
enterprise estate without competing with the vendor already in it.

> Additive, not substitutive. We mirror; we do not cannibalise. The customer keeps the
> data, the vendor keeps the customer, and the mirror feeds back.

Derived from the Executive Boot Contract `EgD-BOOT-001` — durability, repository-only
record, versioned reversibility, the rule of three — and from the working reference model
in `eve-datasphere-sovereign`.

---

## I. Who it is for

Three roles. Entry is by role, not by licence count.

### I.1 The child

The consumer model hands a child a feed. The feed selects the next input before the child
does. The boot contract already classifies that behaviour in machines as **precognitive
loading** — returning what was not asked for, anticipating a question that was not put.
In a model it is a defect. Pointed at a nine-year-old it is the business model.

We invert it. The child receives the raw material and the tools to structure it, inside
an environment scoped to school, cohort and parish, with no global discoverability
surface. The structuring is the instruction. Sorting, naming, relating and correcting are
the work, and the work leaves an artifact.

The claim is bounded and testable: for the hour a child is inside our surface, she is
building rather than being loaded. We do not claim anything about the other twenty-three.

### I.2 The household

The household is the governing body of the environment the child enters, not a user
account inside it. It needs enforceable controls that hold before commercial engagement
pressure argues the other way.

Precedence is fixed: safety, then betterment, then everything else. A feature that clears
safety but not betterment does not ship. This is a gate in the release process, not a
statement of values.

### I.3 The practitioner

The parish administrator, the utility engineer, the accountant, the dealer principal, the
consultant whose name is on the outcome. Enterprise here denotes personal, traceable
responsibility for downstream consequences — not seat count, not an SSO tier. These are
the people who absorb the cost of platform decisions taken above them.

---

## II. What is handed over

Three components. Any one of them alone is a demonstration, not a delivery.

### II.1 The sovereign database

The content already exists — curricula, registers, ledgers, archives, journal lines —
usually inside a system that will not return it in a usable shape. The gap is not
content. The gap is a durable place to put it that the originator controls.

That place is an ordinary, permanently readable relational surface: Postgres-shaped,
versioned in a repository, schema written in files a person can read. The sovereignty is
not in the engine. It is in three guarantees:

- **The schema is public and readable.** Meaning does not live in a vendor binary. It
  lives in files that outlast the vendor.
- **The record is the repository, not the session.** If it cannot be reconstructed by
  cloning and rebuilding, it is not finished.
- **Every change is versioned and carries its inverse.** A wrong turn is walked back
  without anyone's permission.

One shape serves both scales: the child sorting a calendar and the enterprise mirroring a
universal journal off a disaster-recovery copy it has already paid for. There is no
reduced-function version for the customers without a budget.

### II.2 Structuring as the curriculum

Because the schema is readable, organising the material is the education rather than a
prerequisite to it. A child who establishes that a person has a birthplace, a birthplace
has a country, and a country changes its name over time has done data modelling,
historiography and source criticism in one session, and holds a working artifact at the
end of it.

The same act at enterprise scale is master-data governance. It is the same skill, taught
early, and it is the skill the estate is short of.

### II.3 The exit, built before the entrance

Every surface ships with its own egress: full text, timestamped, extractable on demand,
in a shape another tool can read. This is not a compliance feature added after a
regulator asked. A platform that can hold a customer hostage will eventually be run by
someone who does.

Availability has three tiers. Three, not five — five options is deferral.

- **Fork it.** The repository is public. Take it, run it, no contact required. Default,
  no cost.
- **Adopt the canon.** Use the doctrine, schema and ship gates under the EVEglyph Design
  umbrella, with attribution and the precedence order intact.
- **Bring us in.** Practitioner engagement on consequential work, with a named human
  against the outcome.

---

## III. Channel strategy — SAP and Salesforce

The intended commercial position is a formal relationship with both SAP and Salesforce,
structured as reciprocal non-competition. We are not a replacement product and will not
be positioned as one.

### III.1 The agreement we seek

A mutual non-compete covering the licensed estate, with three terms:

- **No substitution.** We do not displace licensed functionality, we do not price against
  seats, and we do not appear in a renewal conversation as the alternative.
- **Mirror rights.** We may replicate objects, schemas and records into the sovereign
  layer for contexts the licensed platform does not serve, under the customer's
  authorisation and the vendor's terms.
- **Return rights.** Anything enriched, structured or corrected in the sovereign layer
  can be written back into the vendor's system of record, wherever the vendor wants it.

### III.2 Mirror without cannibalisation

We mirror; we do not compete. Every object we replicate remains the vendor's object of
record, and we hold it read-only until the customer instructs otherwise. The mirror
extends reach into environments the licensed platform is not sold into — the parish, the
household, the classroom, the small dealer, the volunteer register, the municipality —
where there is no seat to lose and no revenue to cannibalise.

The vendor's downside is therefore bounded to zero by construction: no seat is displaced,
no module is replaced, no renewal is contested. The verifiable form of that promise is
the entry rule already in force — read-only where someone else is the system of record,
additive where we are not.

### III.3 The return path

The asymmetry is the point. A system of record occupies one place. A sovereign layer
occupies many, and it persists across time rather than across a licence term. Every
context we enter generates structure — corrected master data, resolved identity,
attested activity, retained expertise — that the system of record does not currently
collect and cannot easily reach.

That structure flows back. The net direction of value between us and the vendor is
inbound to the vendor: they gain coverage in spaces they do not sell into, and they
receive the enrichment on their own terms and in their own schema. The SAP-side reference
implementation of exactly this pattern — a customer-owned model with the universal
journal as its ledger spine — already exists in `eve-datasphere-sovereign`. The
Salesforce-side equivalent is the same construction against the object model.

---

## IV. How it enters an existing estate

### IV.1 Additive to the incumbent

We do not enter to unseat running systems, their vendors, or the integrators maintaining
them. Those organisations carry long payrolls, long contracts, staff trained deeply on
one platform and now told it is obsolete, and deadlines nobody in the room set. Adding to
that problem is not a market entry, it is a liability.

Entry rule: **read-only where someone else is the system of record, additive where we are
not.** We extend what the customer already owns. The vendor keeps the customer. The
customer keeps the data.

Disruption is also poor engineering. The customer pays for a disrupted incumbent — in
outage, in retraining, in an unbudgeted migration. Making a customer absorb that to prove
a thesis is a bill sent to the wrong party.

### IV.2 Displacement capacity, built in advance

The technology moves work. Stating otherwise would not survive the first meeting. The
position is not that displacement will not occur; it is that we intend to hold the
retraining capacity when it does, at scale rather than case by case.

The staff at risk are the only people who know why the system behaves the way it does on
the last working day of the quarter. That knowledge is the scarcest asset in any
transformation and the first thing a cost-driven programme discards. The commercially
correct move is to capture it, attribute it, and put its owner in front of the new
platform as its instructor.

The same three tools do this work: the sovereign surface as the capture point for
departing expertise; the structured environment as where a mid-career practitioner learns
the new platform; the repository as the durable, attributable record that the
contribution existed.

### IV.3 Order of precedence

Fixed, and not renegotiated per deal.

- **Safety.** Nothing ships that cannot clear it, whatever it earns.
- **Betterment.** Safe but of no benefit to the user is still not shippable.
- **Everything else.** Growth, engagement, revenue and competitive position sit below the
  line, and every counterparty is told so before signature.

---

## V. What we will not do

Three refusals, stated so they can be held against us.

1. **No feed for children.** No global discoverability, no follower counts, no streaks,
   no engagement optimisation pointed at a developing mind. Standing is earned through
   evidenced service, or it is not earned.
2. **No lock-in.** No proprietary tangle, no exit fee, no schema held hostage, no
   "export" that returns a shape nobody else can read. A fork that stops working is a
   defect and is logged as one.
3. **No customer-funded thesis.** We do not break a working system to demonstrate a
   better one, and we do not go to market on somebody else's outage.

---

## VI. The standard of proof

Not a statement of intent. Each line is testable against the repository, which is the
only place it counts.

- **It is committed, or it did not happen.** No finding, figure, decision or artifact
  exists only in a conversation.
- **It is reachable, or it is not delivered.** A surface is live when the holder can open
  it — not when a pipeline turns green.
- **The failures are published too.** Breaches are logged in a public defect register
  with what was asked, what was done instead, the cheaper path that existed, and the
  waste. An institution that publishes only its wins has published nothing.

---

## VII. The position, in three sentences

The technology is handed over in a form the holder can take and leave with, because a
platform that cannot be left will eventually be run by someone who knows it.

We enter additively and read-only, and we contract for non-competition with the
incumbents, because the customer — not the vendor, and not us — pays for disruption.

We mirror into the spaces the system of record does not reach and feed the structure
back, because we occupy many contexts and it occupies one.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
