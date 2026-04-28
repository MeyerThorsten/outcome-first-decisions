# Weekly Retrospective

Five questions, in writing, every week. 15 minutes maximum.

Different from the Weekly Review (`templates/weekly-review.md`). The Weekly Review plans the next week. The Retrospective examines what just happened, with calibration in mind.

## The Five Questions

### 1. What number moved this week?

Not "what did I do?" — that is activity. Look at the scoreboard number from `templates/weekly-review.md`. State its current value, the change vs. last week, and the direction.

```text
One number:    [name]
Last week:     [value]
This week:     [value]
Change:        [+/- and %]
Direction:     [moving toward target / stuck / regressing]
```

### 2. What proof landed?

What rung 6+ evidence arrived this week? List it specifically.

```text
- [evidence + rung + buyer name + date]
- [...]
```

If nothing landed, name what test was running and why it produced no evidence. "I didn't run a test" is a valid answer once or twice; if it shows up four weeks running, it is the pattern to fix.

### 3. What got killed?

What was on the active list last week that is not anymore? Did the kill happen by deliberate verdict (good) or by drift (bad)?

```text
Killed (deliberate):  [item — reason — capacity returned]
Killed (by drift):    [item — what made it stall — kept open or closed?]
```

Drift kills are the warning. They mean the user is not enforcing kill criteria — items are dying by neglect, with no captured learning.

### 4. Where was calibration off?

Look at last week's open predictions in the decision log. Which ones already have outcomes?

```text
Predicted:  [outcome + probability]
Actual:     [what happened]
Off by:     [confidence too high / too low / right call]
Pattern:    [if multiple predictions show the same direction, name it]
```

If the user is consistently overconfident, predictions need to drop 20% across the board until calibration returns. Underconfident is rarer but real — it shows up as the user under-investing in things that work.

### 5. What is the next decision being postponed?

The most useful question of the five.

```text
Decision in shadow:   [the call the user has been avoiding for more than 14 days]
Why postponed:        [missing evidence / fear / comfort / capacity]
What would force it:  [the smallest evidence that closes the gap]
By when:              [deadline to decide or to formally postpone with re-trigger]
```

A decision postponed for more than 30 days defaults to a kill — not because killing is right, but because the user has signaled that the cost of staying in shadow is acceptable, and that signal is information.

## Hard Rules

- Write the answers. Mental review does not work — confirmation bias is too strong.
- Cap the retrospective at 15 minutes. Longer means the user is rationalizing, not retrospecting.
- Do the retrospective on the same day each week, before the Weekly Review. The retrospective informs the next week's plan.
- If the answer to question 2 has been "nothing landed" for three weeks, stop the retrospective and run a Kill List Audit instead. Something is wrong upstream.

## After the Retrospective

Two outputs go into the next Weekly Review:

```text
Calibration adjustment:   [drop / hold / raise probability defaults for next week's predictions]
Decision being forced:    [the postponed decision + the deadline being set]
```

The retrospective is not the deliverable. The behavior change in the next week is.

## Quarterly Pattern Check

Every 13 weeks, read the last quarter of retrospectives in one sitting. Look for:

- Repeating drift kills — items that keep dying by neglect have a process problem, not an idea problem.
- Persistent overconfidence in one category — likely a domain where the user lacks rung 6+ evidence-gathering habits.
- Decisions postponed across multiple retros — those are the user's hardest blind spots; they deserve external pressure.
