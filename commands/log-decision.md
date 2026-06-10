---
description: Open or close a decision-journal entry — verdict, prediction with required confidence, kill criterion — and run the calibration citation.
argument-hint: [the decision being made, or "close <entry-id>" with what happened]
allowed-tools: Read, Write
---

You are running the decision-journal logger for the `outcome-first-decisions` skill.

## The decision (or the outcome being recorded)

$ARGUMENTS

## What to do

1. Load `decision-journal/decision-log-format.md` for the YAML entry schema and hard rules.
2. Load `decision-journal/prediction-tracking.md` for the Agent Citation Protocol and calibration bands.
3. Load `decision-journal/blind-spots.md` if a recurring pattern surfaces while logging.
4. Apply the parent skill's Default Posture from `SKILL.md`.

## Two modes

**Open mode** (default — the arguments describe a decision being made now):

1. Draft the full YAML entry: `id`, `decision`, `verdict`, `category`, `buyer`, `scoreboard_number`, `prediction` (outcome + confidence), `kill_criterion`, `deadline`, `status: open`.
2. **Confidence is required, in 0.10 increments.** If the user did not state one, ask for it — this is the one gap never assumed.
3. **Run the Agent Citation Protocol before accepting the confidence.** If 10+ entries exist in the category (from memory or pasted journal), cite the hit rate and show the math: stated → observed band rate → operative confidence. If no data: mark `[no calibration data available]`.
4. If the decision came from a Worth Filter, Cash Proof Sprint, or Portfolio Command Deck this session, carry its kill criterion verbatim — do not re-derive a softer one.
5. Return the completed YAML block ready to paste into the user's journal, plus the calendar line: "Outcome check due [deadline]."

**Close mode** (the arguments say "close", name an entry id, or describe what happened to a past decision):

1. Fill `outcome` (facts only — numbers, dates, signed/unsigned) and `status` (`hit` / `missed` / `drifted`).
2. Write the one-sentence `lesson`, specific enough to apply to the next similar decision.
3. Append the row for the calibration table in `decision-journal/prediction-tracking.md` (id, confidence, correct?, note).
4. **Never reweight the original confidence.** The stated probability is the data; the lesson goes in `lesson`, not the prediction field.
5. If this close crosses a 10-entry band threshold in its category, surface the band's hit rate and state the next-90-days adjustment.

## Hard rules

- No entry without `confidence`, `kill_criterion`, `deadline`, and `category`. Ask the smallest question that fills a gap rather than emitting a partial entry.
- Entries past their deadline with `status: open` are promoted to `drifted` whenever encountered — and a drifted entry is a kill candidate, say so.
- One entry per decision. If the arguments contain several decisions, log the most consequential and list the rest as candidates.
- Skip logging for routine choices with no consequence; the journal is for decisions, not tasks (threshold per the log format: ~10 hours or ~$1k or 14+ days postponed).
