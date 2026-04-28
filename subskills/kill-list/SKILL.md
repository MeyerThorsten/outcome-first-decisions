---
name: kill-list
description: Audits current commitments and forces explicit keep/change/kill verdicts. Use when the user is overwhelmed, scattered, protecting old projects, or asking what to cut. Returns a decision table with capacity reclaimed.
---

# Kill List

Single-purpose flow. Use when the user is overwhelmed, scattered, or asking what to cut.

This subskill assumes the parent `outcome-first-decisions` skill is loaded for voice, posture, and the self-check protocol. It narrows that skill into one outcome: an audit table with named verdicts, captured learnings, and reclaimed capacity allocated to specific work.

## When to Use

- The user lists 5+ active commitments, projects, or "things I should be doing."
- The user uses words like "scattered," "overwhelmed," "everything is half-done," or "I have too much going on."
- The user is asking what to cut, drop, deprioritize, or pause.
- A previous kill list audit is more than 90 days old.

## When Not to Use

- The user has one specific idea to test → use the `validate-idea` subskill.
- The user has clear focus and is asking how to scale or improve a working operation → use the parent skill's Leverage Ladder.

## Workflow

1. **Get the full list.** All current commitments. Include projects in shadow ("the thing I should be doing but haven't touched in 3 weeks").
2. **Score each on the drop-candidate triggers.** Use `templates/kill-list.md`. Three or more checked = default verdict is kill.
3. **For each item, name a verdict in writing.** Keep, change, or kill. No maybes.
4. **Capture learnings before killing.** What was the original thesis? What proved it wrong? What is reusable?
5. **Allocate reclaimed capacity.** Specifically — to which existing commitments. Do not redirect to new commitments.
6. **Set the next audit date.** Default: 90 days from today.

## Output Shape

Use the parent skill's Main Output Shape, adapted:

1. Verdict (summary: kept N, changed N, killed N).
2. Audit table with verdicts and reasoning.
3. Per-kill learning capture.
4. Capacity reclaimed → where it goes.
5. Next three actions for today.
6. Next audit date.

## Hard Rules

- Force a verdict on every item. Maybes get re-counted as kills.
- Never accept "but I might come back to this" as a keep reason. Make it a re-trigger condition with a specific date or evidence threshold.
- Never let reclaimed capacity drift to new commitments invented during the audit. It goes to existing kept commitments or to buffer.
- Always capture a learning before killing. The kill is not failure when capacity returns to better work.

## References to Load

- `references/frameworks-core.md` — Kill List Audit.
- `references/frameworks-extended.md` — Opportunity Cost Check.
- `references/anti-patterns.md` — Sunk-Cost Loyalty, Multi-Goal Drift, Endless Maybe, Roadmap Theater, Calendar Gravity.
- `references/mental-models.md` — The Drain Test, Optionality vs. Commitment, Concentration Beats Coverage.
- `templates/kill-list.md` — audit table.
- `examples/kill-audit.md` — calibration sample.

## Self-Check (before sending)

- [ ] Verdict named on every item — no maybes.
- [ ] One scoreboard number identified, so kept items can be tied back to it.
- [ ] Capacity reclaimed quantified (hours/week or $/month) and allocated.
- [ ] Learnings captured for every kill.
- [ ] Three actions for today.
- [ ] Next audit date in writing.

If any fails, the audit is incomplete. Force the missing piece before sending.
