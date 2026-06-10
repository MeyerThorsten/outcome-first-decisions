# Portfolio Command Deck — Template

Every active bet on one page. If it consumes hours or money, it is a row — including the side project that is "not really a project."

Protocol and rules: `operations/portfolio-command-deck.md`. Object definitions: `operations/decision-ontology.md`.

## Primary Outcome

```text
Metric:            [the one scoreboard number]
Current:           [value]   (source: [system], as of: [date])
Target:            [value] by [deadline]
Gap:               [target - current]
```

## The Deck

| # | Bet | Outcome it targets | Segment | Rung | Scoreboard Δ (30d) | Capacity/wk | Kill date | Kill criterion | Status |
| - | --- | ------------------ | ------- | ---- | ------------------ | ----------- | --------- | -------------- | ------ |
| 1 |     |                    |         |      |                    |             |           |                |        |
| 2 |     |                    |         |      |                    |             |           |                |        |
| 3 |     |                    |         |      |                    |             |           |                |        |
| 4 |     |                    |         |      |                    |             |           |                |        |

**Status options:** open, drift (no kill date), decide-now (past kill date), kept, changed, killed.

## Sanity Checks (run before the verdict)

- [ ] Capacity column sums to hours/money the user actually has.
- [ ] At most 2 bets below rung 5 (1 if solo).
- [ ] Every row has a kill date and kill criterion — rows without become `drift`.
- [ ] No rung-6+ bet receives less capacity than a rung-1–3 bet.
- [ ] Every Δ value carries provenance (source + as-of date), or is marked `claimed`.
- [ ] At least one bet targets the primary outcome.

## Weekly Portfolio Verdict

```text
Portfolio verdict:   [healthy / overcommitted / starved / drifting] — [one-line correction]

Per-bet verdicts:
  1. [bet] → [keep / change / kill / decide-by-DATE] — [one line why]
  2. ...

Capacity reallocation:
  Freed by kills/changes:  [hours or money]
  Reallocated to:          [named bet] for [named purpose]

This week's proof focus:
  [the one test that moves the lowest-rung load-bearing bet up the ladder]

Next three actions (today):
  1.
  2.
  3.

Next deck review:  [date]
```

## Kill Capture

For every killed row, complete the learning block in `templates/kill-list.md` before deleting the row. The lesson outlives the bet.
