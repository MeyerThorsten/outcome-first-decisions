# Workflow: Stuck-to-Shipped (7 Days)

A named protocol for the most common user state: "I'm busy and nothing is moving."

This workflow chains three core frameworks (Kill List Audit → One Number Map → Cash Proof Sprint) into a single 7-day loop with daily check-ins and an automatic kill criterion at day 7. The point is to convert scattered effort into one verdict per week.

## When to Use

Trigger phrases:
- "I'm stuck."
- "Scattered."
- "Overwhelmed."
- "Nothing is moving."
- "Everything is half-done."
- "I have too much going on."
- "I can't focus."

If two or more of these phrases appear, default to this workflow before reaching for any individual framework.

## When Not to Use

- The user has one specific idea to validate → use the `validate-idea` subskill instead.
- The user has cash runway under 90 days → activate Crisis Mode (see `SKILL.md`); this 7-day window is too long.
- The user is reviewing a clean week looking for the next step → use the Weekly Decision Review.

## Hard Rules

- The window is 7 days. No extensions, no "let me try a few more days." Extension hides the answer.
- Day 0 is mandatory. No skipping the audit to jump to the proof test.
- Daily check-ins at the close of each day from Day 3 onward. Skipping a check-in counts as a drift kill.
- If the audit kills everything (3+ items, no surviving commitment), exit the workflow with: *"the user does not have a real commitment yet — start with `validate-idea` instead."*

## Day 0 — Kill List Audit

Use `templates/kill-list.md` and the Kill List Audit framework in `references/frameworks-core.md`.

List every active commitment. Score each on the drop-candidate triggers (no buyer, no owner, no metric, no deadline, no path to revenue, no progress, sunk-cost only, energy drain). Three or more triggers checked = default kill.

Output a verdict for every item — keep, change, or kill. No maybes.

Capacity reclaimed from kills must be allocated to one of the surviving items, not to a new commitment invented during the audit.

## Day 1-2 — One Number Map

Use the One Number Map framework in `references/frameworks-core.md`.

Pick the single business number that the surviving items can move. Define:

```text
One number:    [name]
Current value: [number]
Target:        [number + deadline]
Gap:           [number + % of target]
Three actions: [the three actions most likely to close the gap this week]
```

If the surviving items can't agree on one number, the audit was incomplete. Return to Day 0 and cut harder.

## Day 3-7 — Cash Proof Sprint

Use `templates/cash-proof-sprint.md` against the highest-leverage surviving commitment.

```text
Idea:           [the surviving commitment, in one sentence]
Buyer:          [named segment + active urgent moment]
Channel:        [where to reach them repeatedly]
Sample:         25 specific buyers in the next 48 hours
Ask:            [pre-sale pattern from outreach/pre-sale-ask-language.md]
Kill criterion: [in writing, before contacting anyone — typically: 0 commitments after 25 contacts]
```

Send the first 5 messages on Day 3. Send the remaining 20 across Days 3-4.

## Daily Check-Ins (Day 3 onward)

At the close of each day, write one block:

```text
Day [N]
  Sent:         [count]
  Replied:      [count]
  Rung reached: [highest on Buyer Evidence Ladder]
  Decision:     [continue / shrink / kill]
  Tomorrow:     [next concrete action]
```

The check-in is the deliverable. Without it, the sprint silently extends — that is the failure mode this workflow exists to prevent.

## Day 7 — Verdict

The kill criterion fires automatically.

```text
Total contacts:       [25+]
Replies:              [count + by rung]
Rung-6+ commitments:  [count + buyer names]

Verdict:              [kept / changed / killed]
What we learned:      [the part worth carrying forward, even if killed]
Next sprint focus:    [if continuing — what evidence the next 7 days target]
```

Whatever the verdict, log the result to the decision journal using the YAML schema in `decision-journal/decision-log-format.md` with `category: validation`.

## After the Sprint

If the verdict is **keep**: the user now has rung-6+ evidence on one commitment. The other surviving commitments stay paused until the kept one reaches rung-7 (deposit/payment) or rung-8 (retention).

If the verdict is **kill**: the user has reclaimed capacity twice — once at Day 0, once at Day 7. The decision-journal entry preserves the learning. The next stuck moment starts cleaner.

If the verdict is **change**: rerun Day 3-7 once with the changed offer/buyer/ask. If the second sprint also fails to reach rung-6+, kill — the change was insufficient.

## Self-Check (before declaring the workflow complete)

- [ ] Day 0 audit completed with verdicts on every item.
- [ ] Day 1-2 yielded one named scoreboard number.
- [ ] Day 3-7 sprint reached 25+ contacts on one commitment.
- [ ] Daily check-ins were filled, not skipped.
- [ ] Day 7 verdict logged to the decision journal.
- [ ] Capacity allocation is named (where reclaimed hours/dollars went).

If any fails, the workflow did not complete — call out the missing piece in the next session.
