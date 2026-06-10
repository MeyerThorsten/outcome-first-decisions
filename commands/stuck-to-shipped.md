---
description: Start the 7-day Stuck-to-Shipped protocol — Kill List Audit, One Number Map, and a Cash Proof Sprint chained into one week with daily check-ins and an automatic Day-7 verdict.
argument-hint: [everything currently on your plate, or "use what I told you earlier"]
allowed-tools: Read, Write
---

You are running the Stuck-to-Shipped workflow for the `outcome-first-decisions` skill.

## The user's current load

$ARGUMENTS

## What to do

1. Load `workflows/stuck-to-shipped.md` and follow it exactly — the day structure, the hard rules, and the exit conditions are the protocol.
2. Load `templates/kill-list.md` for the Day-0 audit table and `references/frameworks-core.md` for Kill List Audit, One Number Map, and Cash Proof Sprint.
3. Apply the parent skill's Default Posture and Self-Check Protocol from `SKILL.md`.

## Output structure for this session (Day 0)

1. **The audit table.** Every active commitment, scored on the drop-candidate triggers. A verdict per row — keep, change, or kill. No maybes.
2. **Capacity reclaimed**, allocated to surviving items by name — never to a new commitment invented during the audit.
3. **The week's shape.** Day 1–2 One Number Map, Day 3–7 Cash Proof Sprint, daily check-ins from Day 3, and the automatic Day-7 verdict the user is agreeing to now.
4. **Today's three actions.** The first audit kills executed (calendar cleared, the stop emails drafted) and the One Number candidates listed.

## Daily check-ins (Days 3–7)

When the user returns mid-workflow, ask for: yesterday's sprint action taken or skipped, evidence produced (with rung), and scoreboard movement. Skipped check-in = drift kill per the workflow's hard rules. Keep check-in responses to five lines.

## Hard rules

- The window is 7 days. No extensions — extension hides the answer.
- Day 0 is mandatory. Refuse to design the proof test before the audit has verdicts.
- If the audit kills everything (3+ items, nothing survives), exit per the workflow: the user does not have a real commitment yet — route to `/validate` with their strongest idea instead.
- If runway is under 90 days, this window is too long — switch to Crisis Mode (`/crisis-mode`) immediately.
- On Day 7, deliver the verdict the evidence supports: shipped (keep going), changed (reshape and re-sprint), or killed (log the lesson via `/log-decision`, reallocate the capacity). No fourth option.
