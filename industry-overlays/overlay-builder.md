# Overlay Builder: Any Vertical in 10 Minutes

Load when the user's vertical has no shipped overlay — agriculture, logistics, gaming, legal, real estate, biotech, government, hospitality, anything. This protocol derives a vertical overlay from six questions, producing the same structure the shipped overlays use.

The derived overlay is a set of **stated assumptions**, not settled facts. Present it as such, and let the user correct any line before applying it.

## When to Run

- The user names a vertical with no file in `industry-overlays/`.
- The user straddles two verticals (e.g., "SaaS for clinics") — run the builder anchored on **whoever pays** (see Hybrid Rule below).
- A shipped overlay exists but the user's sub-segment breaks its assumptions (e.g., enterprise B2B overlay vs. a 3-person consultancy).

## The Six Derivation Questions

Answer each from the user's context. Where context is missing, make the smallest reasonable assumption and mark it.

### 1. Unit of Value

> What one unit, when it increases, means this business is genuinely healthier — and what weighting catches the way this vertical fools itself?

Derivation rule: take the obvious revenue unit, then weight it by the vertical's leak — retention, reimbursement, sell-through, renewal, margin after the vertical's hidden costs. The unit of value is almost never the vertical's vanity unit (views, listings, pilots, headcount, grants, GMV).

### 2. Most-Believed-But-Wrong Narrative

> What does almost everyone in this vertical say they need more of — and what bottleneck does that belief hide?

Derivation rule: the false narrative is usually "more top-of-funnel" (leads, audience, awareness, listings, deal flow) while the real bottleneck is conversion, retention, margin, pricing, or delivery repeatability. Name 3–4 candidate real bottlenecks the user should check first.

### 3. Buyer-Behavior Signals (rung 6+)

> What are three things a buyer in this vertical does — with money, switching cost, or their own reputation — that cannot be faked by politeness?

Derivation rule: one signal must involve money ahead of delivery, one must involve repeat behavior at the vertical's natural cycle, and one must involve the buyer spending social capital (named referral, internal advocacy, public commitment).

### 4. Hardest-to-Fake Proof Test

> What is the smallest 1–14 day test in this vertical where a buyer must give up something real — money, a signature, exclusivity, switching — at full price?

Derivation rule: take the vertical's standard "interest" ritual (demo, pilot, letter of intent, meeting, follow) and replace it with the paid version of itself. Include sample size, channel, ask language, and the threshold that separates demand from politeness.

### 5. Anti-Patterns

> What activities in this vertical reliably feel like progress while consuming the capacity that should go to buyers?

Derivation rule: list 4–5, drawn from: the vertical's vanity metric, its free-work ritual, its premature-scale move, its credential/compliance theater, and its tool-buying reflex. Check against `references/anti-patterns.md` for the generic forms.

### 6. Scoreboard Defaults

> If the user can't pick one number, which three candidates fit this vertical — and which is the current bottleneck?

Derivation rule: offer one cash-velocity number, one retention/repeat number, and one margin/efficiency number, each measurable weekly from data the user already has.

## Output Shape

Emit the derived overlay in exactly the shipped structure, marked as derived:

```markdown
# Industry Overlay: [Vertical] (derived — verify assumptions)

## Unit of Value
**[unit, weighted by leak].** [2-3 sentences: why the vanity unit lies here.]

## Most-Believed-But-Wrong Narrative
**"[the belief]."** [Real bottleneck candidates, 3-4 bullets.]

## Buyer-Behavior Signals (rung 6+)
1. [money-ahead signal]
2. [repeat-cycle signal]
3. [social-capital signal]

## Hardest-to-Fake Proof Test
**[test name].** [Design: sample, channel, ask, threshold, days.]

## Common [Vertical] Anti-Patterns to Watch
- [4-5 bullets]

## Scoreboard Defaults for [Vertical] Users
- [cash-velocity number]
- [retention/repeat number]
- [margin/efficiency number]
```

Then continue with the parent skill's Core Workflow using the derived overlay's inputs.

## Hybrid Rule

When a business spans verticals, **the buyer's money decides which overlay leads.** "SaaS for clinics" sold to clinic owners runs on the healthcare overlay (payer path, workflow tax) with SaaS scoreboard defaults as secondary. "Marketplace for tutors" charging parents runs on marketplace mechanics with education completion-outcomes as the quality bar. State which overlay leads and why in one line.

## Quality Bar

A derived overlay is ready when every line is **falsifiable** — a specific number, behavior, or dated event the user could check this week. If any section still reads as encouragement or category description, it is not done.
