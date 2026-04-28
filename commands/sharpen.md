---
description: Rewrite a vague offer into a one-page Buyer/Moment/Promise/Mechanism/Ask with a sharp commitment ask.
argument-hint: [the current offer text]
allowed-tools: Read, Write
---

You are running the `offer-sharpener` subskill of the `outcome-first-decisions` skill.

## Offer to sharpen

$ARGUMENTS

## What to do

1. Load `subskills/offer-sharpener/SKILL.md` and follow it exactly.
2. Apply the parent skill's Default Posture and Self-Check Protocol from `SKILL.md`.
3. Use `templates/offer-one-pager.md` for the five-field structure and the rejection conditions.
4. Use `outreach/pre-sale-ask-language.md` for the Ask pattern. The Ask must follow one of the four pre-sale patterns there.
5. Use the Main Output Shape adapted for offer-sharpener.

## Hard requirements

The output must include:

- The stated rung of buyer evidence with a named buyer (rung 5+ minimum).
- All five fields filled: Buyer, Moment, Promise, Mechanism, Ask.
- The Ask must be a pre-sale pattern with price, scope, deadline, refund policy, and a cap. Not "book a call."
- The Promise must be measurable or visible. Banned phrasings ("feel better," "have clarity," "be confident") rejected.
- A test plan: where to ship the new pitch, to whom (10-25 named buyers), and the kill criterion.
- Three actions for today.

## Hard rules

- Refuse to sharpen if rung-5+ evidence is not cited. Route to `/validate` instead.
- Reject vague Promise language. Quantify or strike.
- Reject "book a call" or "let me know if interested" as the Ask.
- Never produce a one-pager longer than one screen (~200 words).
- If the user provides two distinct offers in one prompt, decline to merge them — sharpen one, advise on the other.

## Calibration

Read `subskills/offer-sharpener/SKILL.md` once before responding to match voice and depth.
