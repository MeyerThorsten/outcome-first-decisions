# Decision Log Format

A log of every keep / change / kill verdict, with predictions and outcomes.

The log is the evidence base for whether the user's judgment is improving. Without it, every decision feels equally good in hindsight.

## Why Keep a Decision Log

- Memory rewrites itself. The log preserves the decision exactly as made.
- Predictions reveal calibration drift. A user who predicts 80% confidence and is right 50% of the time has a calibration problem worth fixing.
- Killed projects produce learning that disappears without a write-up.
- Returning patterns become visible — the user's specific pitfalls show up across entries.

## The Entry Schema

Each decision is one entry with eight fields. Fill in fields 1-6 at decision time. Fill in fields 7-8 at outcome time.

```text
ID:                 [date + short slug, e.g., 2026-04-28-cohort-presale]
Decision:           [what is being decided, in 1 sentence]
Verdict:            [keep / change / kill / test]
Reasoning:          [the business logic — 2-3 sentences max]
Prediction:         [what the user expects to happen + probability, e.g., "5+ deposits by Friday — 60%"]
Kill criterion:     [the specific result that would prove the verdict wrong]
Deadline:           [date the outcome is checked]

— Outcome (filled later) —

Outcome:            [what actually happened — facts only]
Lesson:             [pattern to remember + where it applies next time]
```

## Normative Schema (YAML frontmatter, required for new entries)

The text format above is the legacy form. New entries adopt the YAML frontmatter schema below. The schema makes the journal queryable — agents can grep for verdicts, drifted entries, or category-specific predictions.

```yaml
---
id: 2026-04-28-cohort-presale         # date + slug
decision: "Run the 6-week positioning cohort"
verdict: test                          # keep | change | kill | test
category: pricing                      # validation | prioritization | pricing | hire | partnership | offer | channel | other
buyer: "Past brand-strategy clients"
scoreboard_number: weekly_revenue
prediction:
  outcome: "5+ paid deposits collected by Friday"
  confidence: 0.60                     # 0.10 increments
kill_criterion: "0-1 deposits → cohort cancels"
deadline: 2026-05-08
status: open                           # open | hit | missed | drifted
outcome: null                          # filled at deadline
lesson: null                           # filled at deadline
tags: [cohort, presale, list-channel]
---

[Free-form reasoning, 2-3 sentences max. Do not exceed.]
```

### Hard rules

- The `confidence` field is required at decision time, in 0.10 increments. No entry without it.
- The `deadline` is required. Entries past their deadline with `status: open` are auto-promoted to `status: drifted` on the next review.
- The `category` field is required. It powers hit-rate-by-category citation in `prediction-tracking.md`.
- The `outcome` and `lesson` fields are filled at the deadline. Skipping them turns the entry into decision debt.

### Why YAML frontmatter

With entries on disk in this schema, agents can:

- `grep -l "verdict: kill"` to find every kill decision.
- Filter `status: open` past deadline to surface drifted decisions.
- Compute hit rate by `category` for calibration.

The schema also forces the user to articulate fields that are easy to skip in prose — especially `confidence` and `category`.

### Migration

Existing prose entries continue to work. Convert opportunistically: when revisiting an entry to fill in its outcome, take a minute to also restate it in YAML form.

## When to Open an Entry

- Every keep / change / kill verdict from a Worth Filter, Cash Proof Sprint, or Kill List Audit.
- Any commitment above ~10 hours of effort or above a defined cash threshold the user sets (default: $1k).
- Any decision the user has been postponing for more than 14 days that finally gets a verdict.

Skip routine choices that don't carry consequence — the log is for decisions, not tasks.

## Prediction Discipline

The prediction field is the most important and the most often skipped.

A useful prediction names:

- **What** specifically should happen.
- **By when.**
- **The probability** the user assigns (in 10% increments — 30%, 60%, 80%; not "I think it'll work").

Sample predictions:

- "5+ paid deposits collected by Friday — 60% confidence."
- "AE ramp to quota by month 2 with the playbook — 40% confidence."
- "Vendor X partnership produces 2+ named pilot intros in 30 days — 50% confidence."

The probability matters because it makes calibration visible (see `prediction-tracking.md`).

## Outcome Capture

When the deadline arrives:

1. **Record what happened.** Facts only — numbers, dates, signed/unsigned, contacted/not contacted.
2. **Compare to prediction.** Did the outcome match? Was the probability appropriate?
3. **Write the lesson.** One sentence. Specific enough to apply to the next similar decision.

If the outcome is incomplete or the deadline slips, capture that too — and reset the deadline. A drifted decision is a kill candidate.

## Storage

Pick the storage that fits the user's existing workflow:

- **Notion / Obsidian / similar:** one page per entry, indexed by date.
- **Spreadsheet:** one row per entry, the schema as columns. Easy for prediction-tracking calibration math.
- **Plain markdown file:** `decisions.md`, append-only.

The format does not matter. The discipline of writing the prediction *before* the outcome is what matters.

## Example Entry

```text
ID:               2026-04-28-cohort-presale
Decision:         Run the 6-week positioning cohort, $2k, 8 seats, pre-sold to existing list.
Verdict:          Test (Cash Proof Sprint).
Reasoning:        Worth Filter scored 26/30. Existing list is the channel. 7-day window forces clean answer.
Prediction:       5+ paid deposits ($2.5k+) by Friday May 8 — 60% confidence.
Kill criterion:   0-1 deposits → cohort cancels, capacity does not redirect to book project.
Deadline:         2026-05-08

— Outcome —

Outcome:          [filled May 8]
Lesson:           [filled May 8]
```

## Quarterly Review

Every 90 days, read the last quarter's entries in one sitting. Look for:

- Decisions where the prediction was very off (calibration drift).
- Decisions where the kill criterion was not enforced (discipline drift).
- Repeated lesson patterns (the user's persistent blind spot).

Use the patterns to update the user's Conversation Rules in their copy of the skill.
