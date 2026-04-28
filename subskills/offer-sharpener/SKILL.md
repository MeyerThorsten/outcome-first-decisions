---
name: offer-sharpener
description: Rewrites a vague offer into a one-page Buyer/Moment/Promise/Mechanism/Ask with a sharp commitment ask. Use when the user has a broad service, product, course, tool, or consulting idea where the offer description requires the buyer to imagine the value.
---

# Offer Sharpener

Single-purpose flow. Use when the user is asking "how do I describe this offer?" or "this isn't converting — what's wrong with the pitch?"

This subskill assumes the parent `outcome-first-decisions` skill is loaded for voice, posture, and the self-check protocol. It narrows that skill into one outcome: a one-page offer expressed as Buyer / Moment / Promise / Mechanism / Ask, with a rung-6+ commitment ask.

## When to Use

- The current offer description is broad ("I help [category] with [topic]").
- The buyer has to imagine the value — mechanism is missing.
- The offer converts at a noticeably low rate despite reach.
- The user is rewriting outreach, sales pages, proposals, or pricing tiers.

## When Not to Use

- The user has no rung-5+ evidence yet → use the `validate-idea` subskill first. A sharp pitch for a buyer who doesn't exist is theatre.
- The offer is converting fine; the user is bored → don't fix what works. Use the parent skill's Leverage Ladder instead.
- The user is in Crisis Mode (runway-driven) → run a Cash Proof Sprint on the existing offer first; sharpen later.

## Workflow

1. **Demand evidence first.** Ask: "What's the highest rung of buyer evidence you have for this offer? Cite a specific buyer name and what they did." Refuse to sharpen without rung-5+ evidence cited (qualified conversation, deposit, signed pilot, repeat usage).
2. **Fill the five fields.** Use `templates/offer-one-pager.md`. Each field has a rejection condition.
3. **Force the Ask to be a pre-sale pattern.** Generic "book a call" is rejected. The Ask must follow one of the patterns in `outreach/pre-sale-ask-language.md` — a six-part commitment with price, scope, deadline, refund policy, and cap.
4. **Read-it-aloud test.** The one-pager must be readable in 30 seconds. If not, cut.
5. **Output.** The filled one-pager + the rung evidence cited + the next three actions for testing the new pitch.

## Output Shape

Use the parent skill's Main Output Shape, adapted:

1. **Verdict.** Sharpened (here it is) / cannot sharpen yet (route to validate-idea) / offer is fine (don't fix what works).
2. **Evidence read.** The rung the user has, named buyer cited.
3. **The one-pager.** Filled Buyer / Moment / Promise / Mechanism / Ask.
4. **The pre-sale ask.** Specific language, with deadline + price + refund policy.
5. **Test plan.** Where to ship the new pitch, to which 10-25 buyers, with what kill criterion.
6. **Next three actions.** Today.

## Hard Rules

- Refuse to sharpen without rung-5+ evidence. State the rung explicitly in the response.
- Force the Mechanism field to name the credible *why-we* — not just *what*.
- Reject "book a call" as the Ask. Replace with a pre-sale pattern.
- The Promise field must be measurable or visible — not "feel more confident" or "have clarity."
- Cap the one-pager at one screen of plain text (~200 words). Length is the enemy of conversion.
- If the same template doesn't work for two offers, the offers are different — write two one-pagers, not one wider one.

## References to Load

- `references/frameworks-extended.md` — Offer Sharpener and Sharp Ask Builder.
- `references/mental-models.md` — Promise vs. Process, The Sharp Ask, Cost of Inaction.
- `references/anti-patterns.md` — Broad Help, Vague Buyer Syndrome, Strategy Without Distribution.
- `templates/offer-one-pager.md` — fillable one-pager.
- `outreach/pre-sale-ask-language.md` — six-part anatomy + four pre-sale patterns.

## Self-Check (before sending)

- [ ] Rung-5+ evidence cited with named buyer.
- [ ] All five fields filled (Buyer, Moment, Promise, Mechanism, Ask).
- [ ] The Ask is a pre-sale pattern, not "book a call."
- [ ] Promise is measurable or visible — banned phrasings absent.
- [ ] One-pager fits one screen (~200 words).
- [ ] Three actions for today.

If any fails, ask the smallest question that fills the gap. Do not soften the verdict to skip the gap.
