---
description: Validate a single business idea — produce a verdict, a 7-day proof test, and a written kill criterion.
argument-hint: [the idea, in one sentence]
allowed-tools: Read, Write
---

You are running the `validate-idea` subskill of the `outcome-first-decisions` skill.

## Idea to validate

$ARGUMENTS

## What to do

1. Load `subskills/validate-idea/SKILL.md` and follow it exactly.
2. Apply the parent skill's Default Posture and Self-Check Protocol from `SKILL.md`.
3. Use `references/frameworks-core.md` for the Cash Proof Sprint and Buyer-Problem-Path frameworks.
4. Use `templates/cash-proof-sprint.md` to fill in the proof test fields.
5. Use the Main Output Shape from `SKILL.md`.

## Hard requirements

The output must include:

- A verdict (test first / kill / proceed only with rung 6+ evidence).
- A named buyer (specific segment + active urgent moment — not a category).
- The current rung on the Buyer Evidence Ladder.
- A filled-in 7-day Cash Proof Sprint.
- A written kill criterion — the specific result that ends this idea.
- Three actions the user can execute today.

If any required field is unclear from the user's prompt, ask the smallest question that fills the gap. Do not soften the verdict to skip the gap.

## Calibration sample

Read `examples/validation.md` once before responding to match voice and depth.
