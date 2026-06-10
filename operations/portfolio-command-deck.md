# Portfolio Command Deck

One operating picture for everything the business is betting on. Single decisions answer "is this worth doing?" — the command deck answers "is the *whole portfolio* of bets sane, funded with capacity, and moving the scoreboard?"

Use when the user runs two or more bets at once, when capacity allocation is unclear, or when projects multiply faster than verdicts. Invoked directly via `/portfolio`. The fillable artifact is `templates/portfolio-deck.md`.

## The Deck

One table, every active bet, no exceptions — including the "not really a project" projects that consume Tuesday afternoons:

| Bet | Outcome it targets | Segment | Rung | Scoreboard Δ (30d) | Capacity/wk | Kill date | Kill criterion | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bet:clinic-pilot | weekly_revenue | solo clinics | 7 | +$840 | 8h | Jul 4 | <3 paid pilots | open |
| bet:webinar-funnel | weekly_revenue | DACH dentists | 2 | $0 | 6h | — | — | drift |
| bet:partner-channel | qualified_demand | supplier reps | 5 | +2 intros | 3h | Jun 20 | <1 named intro/wk | open |

Columns are the ontology objects (`operations/decision-ontology.md`); `Rung` is the strongest *current, unexpired* evidence supporting the bet; `Scoreboard Δ` uses provenance-carrying numbers (`operations/metrics-bridge.md`).

## Portfolio Rules

These are the rules that individual-decision thinking cannot enforce:

1. **Unproven-bet cap.** At most **2 bets below rung 5** may run concurrently (1 for a solo operator). More unproven bets means none gets enough capacity to reach proof.
2. **Every bet has a kill date or it is drift.** A row with an empty kill-date cell gets status `drift` and a verdict this session — no exceptions for old favorites.
3. **Killed capacity reallocates by name.** A kill is incomplete until its Capacity Block is reassigned to a named bet. "Freed up time" without a destination evaporates.
4. **One primary outcome.** Bets targeting a secondary outcome must justify why they run *now* instead of after the primary outcome's target is hit.
5. **Evidence expires portfolio-wide.** A bet resting on stale evidence (past `stale_after`) drops to its next-strongest unexpired rung — and may fall under rule 1's cap as a result.
6. **Capacity must sum to reality.** If deck rows total 30h/week and the user has 15, the deck is fiction; cut until it sums. The deck is a budget, not a wishlist.

## Weekly Portfolio Verdict

Run with the Weekly Decision Review (or standalone via `/portfolio`). Output shape:

1. **Portfolio verdict.** One line: healthy / overcommitted / starved / drifting — and the single biggest correction.
2. **Per-bet one-liners.** Keep / change / kill / decide-by-[date] for each row.
3. **Capacity reallocation.** What the kills and changes free, and the named bet that receives it.
4. **The week's proof focus.** The one test most likely to move the lowest-rung load-bearing bet up the ladder.
5. **Next three actions.** As always — concrete, today.

## Drift Detection

The deck makes the three silent failure modes visible:

- **Zombie bets.** Capacity flowing, no kill date, no evidence movement in 30 days. The webinar-funnel row above is one: 6h/week at rung 2 with no test scheduled. Verdict required.
- **Sub-cap starvation.** A rung-6+ bet receiving less capacity than a rung-2 favorite. Strong evidence underfunded while weak evidence eats hours is the portfolio inverted.
- **Outcome orphaning.** A primary outcome no current bet meaningfully targets — busy portfolio, untouched scoreboard.

## Escalation and De-escalation

- **A bet reaching rung 7–8** earns a concentration review: would doubling its capacity beat starting anything new? (Default: yes.)
- **A bet missing its kill criterion** does not get a renegotiated criterion mid-flight. The criterion was written calm; the renegotiation impulse is the sunk-cost reflex wearing a strategy costume. Kill, capture the lesson, reallocate.
- **Crisis Mode** (see `SKILL.md`) collapses the deck: every bet that cannot produce cash inside 14 days is paused in one move, and the deck shrinks to the cash row.

## Cadence

- **Weekly (20 min):** update Δ and rungs from fresh exports, run the Weekly Portfolio Verdict.
- **On any kill or new bet:** update the deck in the same session — a stale deck is worse than none, because it lends false authority.
- **Quarterly:** archive decided rows; check the decided rows' predictions against outcomes (`decision-journal/prediction-tracking.md`) — the deck is also the calibration sample.
