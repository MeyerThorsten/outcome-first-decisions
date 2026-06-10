# Metrics Bridge

Ground every scoreboard number in a source system. A verdict computed from remembered numbers inherits the user's optimism; a verdict computed from exports inherits reality.

This protocol defines how numbers enter a session: where they come from, how provenance is recorded, when they expire, and what the skill does when no source exists.

## The No-Naked-Numbers Rule

Any number that drives a **keep/change/kill verdict, a Worth Filter score of 4+, or a commitment above ~10 hours or $1k** must carry provenance. Numbers without provenance are accepted only as `claimed`, and the verdict states that dependency explicitly:

> "Verdict assumes weekly revenue is $3.2k as claimed. If the Stripe export says otherwise, the verdict changes."

Small talk and rough sizing don't need provenance. Verdicts do.

## Provenance Schema

Attach to any metric, in YAML or inline:

```yaml
metric: weekly_revenue
value: 3200
unit: USD/week
source: stripe                 # the system of record, not the person
extraction: "Stripe dashboard > Gross volume, 7-day, exported 2026-06-09"
as_of: 2026-06-09
freshness: 7d                  # how old this may be before re-pull
provenance: exported           # exported | computed | claimed
```

Three provenance grades:

- **exported** — read from a source-system export, screenshot, or report the user provided this session.
- **computed** — derived by the agent from exported inputs (state the formula).
- **claimed** — stated from memory. Usable, but flagged, and never silently upgraded.

## Source Map by Scoreboard Type

Ask for the cheapest authoritative export — most take under two minutes:

| Scoreboard number | System of record | Two-minute extraction |
| --- | --- | --- |
| Revenue, MRR/ARR | Payment processor (Stripe, PayPal), invoicing tool | Gross volume / MRR panel, last 30d |
| Cash collected | Bank account | Statement CSV or balance screenshot |
| Retention / churn | Billing system, subscription dashboard | Cohort or churn panel |
| Activation, usage | Product analytics | Funnel or event count, last 14d |
| Pipeline, win rate | CRM | Stage report export |
| Sell-through, reorders | POS / store backend (Shopify, Square) | Sales by item, last 30d |
| Funding raised | Donor CRM / accounting | Gifts report, YTD |
| Claims collected | Practice management / billing | Collections report, last 30d |
| Traffic, conversion | Web analytics | Landing page conversions, last 14d |

The vertical overlays (`industry-overlays/`) name which of these is the default scoreboard for each vertical.

## Freshness Rules

- Default expiry: **7 days** for cash-velocity numbers, **30 days** for retention/cohort numbers, **90 days** for structural numbers (margin stack, CAC).
- An expired number degrades to `claimed` automatically — the value may still be right, but the session must say it is operating on an old reading.
- Evidence objects (`operations/decision-ontology.md`) carry `stale_after` for the same reason: a rung-7 payment from last year does not justify this quarter's bet.

## Session Protocol

At the start of any session that will produce a verdict:

1. **Ask for the one export that matters** — the scoreboard number's source, nothing else. One screenshot or CSV paste beats a dashboard tour.
2. **Record provenance** in the session (and in memory, where available): value, source, as_of.
3. **Compute, don't accept, derived numbers.** If the user states a conversion rate, ask for numerator and denominator; compute it.
4. **Diff against the last reading.** If memory holds a prior value, state the delta — the delta is the scoreboard.
5. **Proceed on `claimed` when the user can't pull data now** — never block. Mark the dependency in the verdict and make "pull the export" one of the three actions.

## Red Flags the Bridge Catches

- **Round-number drift.** "About $5k" three weeks running, while the export says $3.8k declining.
- **Metric substitution.** Asked for revenue, the user reports bookings, pipeline, or GMV. Name the substitution; use the real number.
- **Cherry-picked window.** "Best week ever" measured over the one good week. Default windows: trailing 7/30 days, not selected ones.
- **Numerator-only claims.** "12 signups!" — of how many visitors, at what cost? Numbers travel in ratios.
- **Optimistic compounding.** Projections built by multiplying three claimed numbers. Each `claimed` input marks the projection as fiction until exported.

## Worked Example

> User: "Revenue's around $5k a week now, so I'm ready to hire a VA."

Bridge applied:

1. Source ask: "Pull Stripe gross volume, trailing 4 weeks — paste the four weekly totals."
2. User pastes: 3,810 / 4,420 / 3,150 / 3,975.
3. Recorded: `weekly_revenue: 3839 (computed, stripe, as_of 2026-06-09, 4wk avg)`.
4. Verdict uses $3.8k, not $5k — and the hire decision flips from "yes" to "test first with 10 delegated hours."

The bridge did not refuse the user's number; it replaced a remembered number with an exported one, and the decision changed. That swing is the entire value of this file.
