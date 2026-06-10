# Design: Vertical Expansion + Decision-Operations Layer

Date: 2026-06-10
Status: Approved for implementation (user directive: develop, test, document; autonomous session)
Tracker: http://localhost:4789/projects/outcome-first-decisions

## Goal

Make Outcome-First Decisions useful for **all business verticals** (not just the five it ships with) and raise it from a single-decision advisor to an **operational decision system for a whole business** — the markdown-skill equivalent of what Palantir does for enterprises: a shared ontology, source-grounded metrics, and a live cross-bet operating picture — while keeping the package a zero-dependency, agent-portable skill.

## Constraints

- The product **is** a skill package: markdown + YAML, distributed as a zip into agent skill directories (Claude Code, Codex, Cursor). No runtime, no server, no dependencies.
- Independence guardrails (PROVENANCE.md) apply to all new content: no third-party framework names, quotes, or persona references. "Palantir-level" is a quality bar in the user's brief, not a branding element — no Palantir naming appears in shipped content.
- Marketing pages (`website/skills/outcome-first-decisions.md` + `.html`) must stay truthful: every count and capability claim must match the package. Tests enforce this.
- Existing voice and structure conventions (overlay section layout, Main Output Shape, evidence rungs) are followed exactly.

## Approaches considered

1. **Content-depth expansion (chosen).** Extend the skill itself: more verticals + a universal overlay builder, plus a new `operations/` layer (ontology, metrics grounding, portfolio command deck), structural tests, synced docs. Fits the product's nature, shippable today, testable, keeps portability.
2. **Build companion software** (dashboard/DB/web app). Rejected: changes the product category, breaks the zero-dependency install promise, duplicates what host agents + Threlmark already do, and is far beyond a single iteration.
3. **MCP server for journal/calibration storage.** Rejected for now: adds a runtime dependency that Codex/Cursor installs can't assume. The ontology is designed so an MCP layer could be added later without rework (logged as a tracker idea, not built).

## Design

### A. Vertical coverage: 12 overlays + universal builder

New files in `industry-overlays/`, each following the existing six-section structure (Unit of Value / Most-Believed-But-Wrong Narrative / Buyer-Behavior Signals (rung 6+) / Hardest-to-Fake Proof Test / Anti-Patterns / Scoreboard Defaults):

1. `marketplace.md` — two-sided marketplaces and platforms.
2. `local-business.md` — brick-and-mortar retail, restaurants, gyms, local services.
3. `education-coaching.md` — courses, cohorts, coaching, training businesses.
4. `healthcare.md` — clinics, practices, digital health, care services.
5. `fintech.md` — regulated financial products and services.
6. `hardware-physical.md` — physical products, manufacturing, DTC goods with COGS.
7. `nonprofit.md` — donor- and grant-funded organizations.

Plus `overlay-builder.md`: a 10-minute protocol the agent runs to construct an ad-hoc overlay for **any vertical not on the list** (questions that derive the unit of value, the dominant false narrative, three rung-6+ signals, the hardest-to-fake proof test, and scoreboard defaults). This is what makes the claim "all verticals" honest.

`SKILL.md` gains a **Vertical Overlay Protocol**: detect the vertical from context → load the matching overlay → if none matches, run overlay-builder inline and state the derived overlay as assumptions.

### B. Decision-operations layer (`operations/`)

The Palantir-grade translation for a skill: one shared object model, numbers grounded in source systems, and a single operating picture across all running bets.

- `operations/decision-ontology.md` — typed object model with YAML schemas and ID conventions: **Outcome, Buyer Segment, Bet, Proof Test, Evidence, Decision, Capacity Block, Risk**. Relations link objects by ID (a Bet targets an Outcome, is justified by Evidence, is tested by Proof Tests, consumes Capacity Blocks, and ends in a Decision). Extends — does not replace — the existing decision-journal schema: a journal entry is the Decision object; the ontology adds the objects around it. Includes grep/query patterns so agents can answer portfolio questions from plain files.
- `operations/metrics-bridge.md` — protocol for grounding every scoreboard number in a source system (payment processor, analytics, CRM, bank export, POS). Every metric carries provenance (`source`, `as_of`, `extraction`, `rung`); freshness rules; a "no naked numbers" rule for verdicts above a stakes threshold.
- `operations/portfolio-command-deck.md` — the cross-bet operating picture: one table of all active bets (outcome targeted, evidence rung, scoreboard delta, capacity consumed, kill date, owner), portfolio-level rules (max concurrent unproven bets, capacity reallocation on kill, drift detection), and a weekly portfolio verdict shape.
- `templates/portfolio-deck.md` — the fillable artifact for the command deck.
- `commands/portfolio.md` — `/portfolio` slash command: builds or updates the command deck from the user's bets/journal and returns portfolio-level verdicts.

`SKILL.md` routing gains: "Multiple bets running at once, or capacity unclear across projects? → Portfolio Command Deck." Reference-loading table gains the `operations/` rows. Default posture gains a data-grounding line.

### C. Tests

`tests/validate_package.py` (python3, stdlib only) — structural invariants:

1. `SKILL.md` frontmatter has `name` + `description`.
2. Every directory/file named in SKILL.md References and README file-structure exists.
3. Every overlay (except `overlay-builder.md`) contains the six required sections.
4. Slash-command lists in SKILL-adjacent docs (README, website page) match `commands/*.md` exactly.
5. Counts claimed on the website page (overlays, core/supporting frameworks, subskills, commands) match the filesystem.
6. Relative markdown links across the package resolve.
7. Website `.md` and `.html` stay in sync on headline claims (commands, counts).

`build/package.sh` — rebuilds `outcome-first-decisions.zip` deterministically with the shipped content (excludes `website/`, `docs/`, `tests/`, `build/`, git files), so the committed zip matches the tree until CI packaging (existing tracker item) lands.

### D. Documentation

- `README.md`: new capabilities, updated file structure, `/portfolio` command.
- `website/skills/outcome-first-decisions.md` and `.html` updated in lockstep: corrected counts, a "Decision operations" section, a "Verticals" section, manual additions (overlay protocol, `/portfolio`, metrics grounding). Install section keeps the live v1.0.0 link; v1.1.0 noted as next release in `CHANGELOG.md` only.
- `CHANGELOG.md` at repo root.

### E. Tracking

Each work package becomes a Threlmark item (`POST /api/projects/outcome-first-decisions/items`), moved `development` → `done` as it completes. The pre-existing item "Verify industry overlays cover the Buyer Evidence Ladder" is closed by test #3 coverage. A follow-up item records "Cut v1.1.0 release" and the deferred MCP idea.

## Error handling / edge cases

- Threlmark down → work proceeds; tracking is reconciled at the end (tracker is observability, not a dependency).
- Vertical ambiguity (e.g., "SaaS for clinics") → SKILL.md rule: the buyer's money decides; load the overlay of whoever pays (healthcare buyer ⇒ healthcare overlay, with SaaS scoreboard defaults as secondary).
- Missing source data in metrics-bridge → explicit `provenance: claimed` marking, never a refusal; the skill degrades to assumption-stating, as today.

## Testing strategy

Structural tests above run via `python3 tests/validate_package.py` and must pass before commit. Content quality is reviewed against the existing overlays' bar (specific, falsifiable, rung-anchored). The zip rebuild is verified by listing its contents.
