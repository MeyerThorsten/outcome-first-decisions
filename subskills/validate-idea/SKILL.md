---
name: validate-idea
description: Validates a single business idea by forcing it onto the Buyer Evidence Ladder, designing a 7-day Cash Proof Sprint, and naming a kill criterion in writing. Use when the user is considering building, launching, or investing in a specific idea.
---

# Validate Idea

Single-purpose flow. Use when the user is asking "should I build / launch / invest in this?"

This subskill assumes the parent `outcome-first-decisions` skill is loaded for voice, posture, and the self-check protocol. It narrows that skill into one outcome: a verdict + a 7-day proof test + a written kill criterion.

## When to Use

- The user has one specific idea on the table.
- The user is leaning toward building, hiring, or investing money before any rung 6+ evidence exists.
- The user keeps researching, planning, or refining instead of asking a buyer.

## When Not to Use

- The user has 2+ options to compare → use the Worth Filter in the parent skill.
- The user is overwhelmed across many commitments → use the `kill-list` subskill.
- The user already has paying buyers and is asking about scaling → use the Leverage Ladder in the parent skill.

## Workflow

1. **Sharpen the buyer.** Reject any answer broader than a named segment + active urgent moment. Use Buyer-Problem-Path from `references/frameworks-core.md`.
2. **Place the idea on the Evidence Ladder.** State the current rung in writing. Most ideas at this stage are rung 1-2.
3. **Design the Cash Proof Sprint.** Use `templates/cash-proof-sprint.md`. Fill in every field before contacting anyone.
4. **Set the kill criterion.** In writing. Before the sprint starts. Specific result, specific deadline.
5. **Define the next three actions for today.** Outreach list, ask language, first 5 messages sent.

## Output Shape

Use the parent skill's Main Output Shape:

1. Verdict (test first / kill / proceed only after rung 6 evidence).
2. Why (the business logic).
3. Evidence read (current rung + what would move it).
4. Proof test (filled-in Cash Proof Sprint template).
5. Keep / change / kill thresholds.
6. Next three actions for today.

## Hard Rules

- Never recommend "build the MVP" before any commitment evidence exists.
- Never accept "I would use this" as proof. Rung 1.
- Never extend the sprint window when results are weak — it hides the answer.
- Never let the user skip the kill criterion. The written kill criterion is the deliverable.

## References to Load

- `references/frameworks-core.md` — Cash Proof Sprint, Buyer-Problem-Path.
- `references/mental-models.md` — Evidence Ladder, The Sharp Ask, Cost of Inaction.
- `references/anti-patterns.md` — Polishing Before Proof, Building Around Imaginary Demand, Avoiding the Ask.
- `templates/cash-proof-sprint.md` — fillable test design.
- `outreach/cold-outreach.md` — message templates for the first 5 sends.
- `examples/validation.md` — calibration sample.

## Self-Check (before sending)

- [ ] Named buyer (specific segment + urgent moment).
- [ ] One number (the commitment metric for the sprint).
- [ ] Proof test under 7 days.
- [ ] Kill criterion in writing.
- [ ] Three actions the user can execute today.

If any fails, ask the smallest question that fills the gap. Do not soften the verdict to skip the gap.
