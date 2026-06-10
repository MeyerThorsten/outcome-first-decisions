---
description: Build or update the Portfolio Command Deck — every active bet, one operating picture, portfolio-level verdicts.
argument-hint: [list of active bets/projects with hours and any numbers, or "use what I told you earlier"]
allowed-tools: Read, Write
---

You are running the Portfolio Command Deck for the `outcome-first-decisions` skill.

## The user's portfolio

$ARGUMENTS

## What to do

1. Load `operations/portfolio-command-deck.md` for the deck structure, portfolio rules, and drift detection.
2. Load `templates/portfolio-deck.md` for the fillable artifact.
3. Load `operations/decision-ontology.md` if bets need to be formalized from a loose project list.
4. Apply the parent skill's Default Posture and Self-Check Protocol from `SKILL.md`. Scoreboard numbers follow `operations/metrics-bridge.md` — carry provenance or be marked `claimed`.

## Output structure

1. **The deck.** One row per active bet — including anything consuming 2+ hours/week that the user did not call a project. Fill every column; missing kill dates become status `drift`.
2. **Sanity-check results.** Each failed check named, with the rule it violates.
3. **Portfolio verdict.** Healthy / overcommitted / starved / drifting, with the single biggest correction.
4. **Per-bet verdicts.** Keep / change / kill / decide-by-[date], one line each.
5. **Capacity reallocation.** What kills and changes free, and the named bet receiving it.
6. **This week's proof focus** and **next three actions** (today, concrete).

## Hard rules

- Every bet gets a row. If the user lists "things I'm doing" that are not bets, convert each to a bet statement or mark it unallocated drain.
- Enforce the unproven-bet cap: more than 2 bets below rung 5 (1 if solo) → the verdict must name which to pause.
- A row without a kill date cannot be verdict "keep." It is "drift" until a kill date and criterion are written.
- Capacity must sum to the user's stated real capacity. If it does not, cut rows in the verdict — do not present a deck that cannot be true.
- Freed capacity is reallocated by name in the same response, never "freed up" in the abstract.
- If the user mentions runway, payroll, or a lost biggest customer, switch to Crisis Mode per `SKILL.md` — pause every bet that cannot produce cash inside 14 days.
