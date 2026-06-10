# Changelog

All notable changes to the Outcome-First Decisions skill package.

## [Unreleased] — v1.1.0

### Added

- **7 new industry overlays** — marketplace, local business, education / coaching, healthcare, fintech, hardware / physical products, and nonprofit — bringing vertical coverage to 12, each in the established six-section structure (unit of value, wrong narrative, rung-6+ signals, hardest-to-fake proof test, anti-patterns, scoreboard defaults).
- **Overlay builder** (`industry-overlays/overlay-builder.md`) — a six-question derivation protocol that constructs an overlay for any vertical not on the list, including a hybrid rule for businesses that span verticals (the buyer's money decides which overlay leads).
- **Decision-operations layer** (`operations/`):
  - `decision-ontology.md` — eight typed objects (Outcome, Buyer Segment, Bet, Proof Test, Evidence, Decision, Capacity Block, Risk) with YAML schemas, stable IDs, relations, grep query patterns, and a staged adoption path. Extends the decision journal into a queryable plain-file decision graph.
  - `metrics-bridge.md` — source-grounded scoreboard numbers: provenance schema (exported / computed / claimed), source map by scoreboard type, freshness rules, and a no-naked-numbers rule for verdict-driving metrics.
  - `portfolio-command-deck.md` — cross-bet operating picture with portfolio rules (unproven-bet cap, mandatory kill dates, named capacity reallocation), drift detection, and a weekly portfolio verdict shape.
- **`/portfolio` slash command** (`commands/portfolio.md`) and fillable **portfolio deck template** (`templates/portfolio-deck.md`).
- **SKILL.md**: Vertical Overlay Protocol (match / derive / hybrid), portfolio routing branch, data-grounding posture line, reference-loading rows for the new layers, and memory-protocol entries for the command deck and metric provenance.
- **`/log-decision` slash command** (`commands/log-decision.md`) — opens journal entries (confidence required, in 0.10 increments) and closes them at the deadline (outcome, lesson, calibration-table row), running the Agent Citation Protocol in both directions. Wires the decision journal and prediction tracking end to end.
- **Two new worked examples** — `examples/crisis-mode.md` (the collapsed output shape under 70 days of runway) and `examples/portfolio.md` (a five-bet command deck with rule violations surfaced and capacity reallocated).
- **CI workflows** — `.github/workflows/test.yml` (structural validation + zip build on every push/PR) and `.github/workflows/release.yml` (tag `v*` → validate → build → GitHub Release with the zip asset).
- **Structural test harness** (`tests/validate_package.py`) — validates frontmatter, referenced paths across the whole package (commands, subskills, operations, workflows, templates), overlay section structure, slash-command parity and frontmatter, marketing-count truthfulness, md/html page sync, and relative links. Run with `python3 tests/validate_package.py`.
- **Deterministic zip build** (`build/package.sh`).
- `CHANGELOG.md` (this file).

### Changed

- README and website pages updated for the new vertical coverage, decision-operations layer, and `/portfolio` command; marketing counts now enforced by tests.
- Crisis Mode reference path corrected to `references/frameworks-core.md`.

## [1.0.0] — 2026-04-28

Initial public release: six core frameworks, seven supporting frameworks, Buyer Evidence Ladder, Crisis Mode, decision journal with calibration tracking, five industry overlays, buyer-conversation kit, Stuck-to-Shipped workflow, three subskills, five slash commands. Licensed AGPL-3.0, distributed via GitHub Releases.
