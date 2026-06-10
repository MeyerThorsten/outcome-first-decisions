# Decision Ontology

A shared object model for running a whole business through this skill — not one decision at a time, but every outcome, bet, test, and capacity block as linked, queryable objects in plain files.

The decision journal (`decision-journal/decision-log-format.md`) records verdicts. The ontology adds the objects *around* a verdict, so an agent can answer operating questions across the entire business: *Which bets target the stalled outcome? What evidence justifies this bet, and how old is it? Where is capacity going, and which kill would free the most?*

Everything stays markdown + YAML. No database, no server. Objects live wherever the user keeps notes; the schema is what makes them queryable.

## The Eight Object Types

| Object | One-line definition | Lives until |
| --- | --- | --- |
| **Outcome** | A business result with a number, target, and deadline | Hit, missed, or replaced |
| **Buyer Segment** | A named group that can pay, with an active problem and a reachable channel | Disproven or merged |
| **Bet** | A commitment of capacity toward an Outcome via a Buyer Segment | Decided (keep/change/kill) |
| **Proof Test** | A 1–14 day experiment that moves evidence up the ladder | Deadline reached |
| **Evidence** | One observed buyer behavior, with rung and provenance | Superseded or stale |
| **Decision** | A keep/change/kill/test verdict — the journal entry, unchanged | Outcome captured |
| **Capacity Block** | A recurring slice of hours or money allocated to a Bet | Reallocated |
| **Risk** | A named way a Bet dies that evidence does not yet rule out | Retired by evidence |

## ID Convention

Every object gets a stable ID: `type:date-slug`.

```
out:2026-06-weekly-revenue        bet:2026-06-clinic-pilot
seg:2026-05-solo-clinic-owners    test:2026-06-paid-pilot-ask
ev:2026-06-08-renewal-call        dec:2026-06-10-kill-webinar
cap:2026-06-tue-thu-mornings      risk:2026-06-payer-path
```

Journal entries keep their existing `id:` field; the `dec:` prefix applies when referenced from other objects.

## Object Schemas

### Outcome

```yaml
id: out:2026-06-weekly-revenue
metric: weekly_revenue            # one scoreboard number (One Number Map)
current: 3200                     # with provenance — see operations/metrics-bridge.md
target: 6000
deadline: 2026-08-31
season_rationale: "Cash covers runway; growth bets resume above $6k/wk"
```

One **primary** Outcome at a time. Secondary outcomes may exist but cannot justify a Bet on their own.

### Buyer Segment

```yaml
id: seg:2026-05-solo-clinic-owners
who: "Owner-operators of 1-3 chair dental clinics, <10 staff, DACH region"
active_problem: "No-show rate 15%+ eats 1 day/week of chair capacity"
channel: "Dental supplier newsletter + 2 trade groups"
evidence: [ev:2026-05-22-interview-4, ev:2026-06-01-presale-1]
status: active                    # active | disproven | merged
```

A segment without at least one Evidence object at rung 4+ is a hypothesis, not a segment.

### Bet

```yaml
id: bet:2026-06-clinic-pilot
statement: "Paid no-show-reduction pilots for solo clinics reach $2k/wk by August"
outcome: out:2026-06-weekly-revenue
segment: seg:2026-05-solo-clinic-owners
evidence: [ev:2026-06-01-presale-1]      # what justifies running this bet
tests: [test:2026-06-paid-pilot-ask]
capacity: [cap:2026-06-tue-thu-mornings]
risks: [risk:2026-06-payer-path]
kill_date: 2026-07-04                    # the date a verdict is forced
kill_criterion: "<3 paid pilots by kill date → kill, capacity to retainer offer"
status: open                             # open | kept | changed | killed
decision: null                           # dec:… once verdict exists
```

The Bet is the central object. **Hard rule: a Bet missing `kill_date` or `kill_criterion` is not a Bet — it is drift with a name.**

### Proof Test

The Cash Proof Sprint template (`templates/cash-proof-sprint.md`) is the long form. The object form:

```yaml
id: test:2026-06-paid-pilot-ask
bet: bet:2026-06-clinic-pilot
design: "25 clinics contacted, $490 60-day paid pilot, conversion clause at $190/mo"
rung_sought: 7
deadline: 2026-06-24
threshold: "3+ paid → keep; 1-2 → change offer; 0 → kill"
result: null                      # filled at deadline, becomes Evidence
```

### Evidence

```yaml
id: ev:2026-06-01-presale-1
observed: "Clinic owner paid $490 pilot invoice within 48h of ask"
rung: 7                           # Buyer Evidence Ladder 1-8
source: "Bank transaction 2026-06-01"   # provenance, per metrics-bridge
as_of: 2026-06-01
stale_after: 2026-09-01           # evidence expires; default 90 days
supports: [bet:2026-06-clinic-pilot, seg:2026-05-solo-clinic-owners]
```

Evidence is **observed behavior, one event per object**. Opinions can be logged but never above rung 2, and never as the sole support of a Bet.

### Decision

The journal entry schema, unchanged. Two optional linking fields extend it:

```yaml
bet: bet:2026-06-clinic-pilot     # which Bet this verdict closes or renews
frees: [cap:2026-06-tue-thu-mornings]  # capacity released by a kill — must be reallocated by name
```

### Capacity Block

```yaml
id: cap:2026-06-tue-thu-mornings
what: "Tue+Thu 08:00-12:00, ~8h/wk"   # or money: "ad budget $500/mo"
allocated_to: bet:2026-06-clinic-pilot
review: 2026-07-04                     # same date as the bet's kill_date
```

Capacity is finite and named. Work that consumes hours but maps to no Capacity Block is invisible drain — surface it in every Kill List Audit.

### Risk

```yaml
id: risk:2026-06-payer-path
bet: bet:2026-06-clinic-pilot
statement: "Clinics expect insurers to pay for no-show tooling, not their own P&L"
would_retire: "2+ pilots paid from clinic operating budget"
status: open                      # open | retired | realized
```

## Relations (the graph)

```
Outcome ←targets— Bet —serves→ Buyer Segment
                   │
        justified-by→ Evidence ←produces— Proof Test
                   │
         consumes→ Capacity Block
                   │
       threatened-by→ Risk
                   │
          ends-in→ Decision —frees→ Capacity Block
```

Reading the graph answers the operating questions:

- **"Why are we doing this?"** Bet → Outcome + Evidence (with rungs and dates).
- **"What would change our mind?"** Bet → kill_criterion + open Risks.
- **"Where is the week going?"** Capacity Blocks → Bets → Outcome.
- **"What did we learn from the last kill?"** Decision → lesson, Evidence retained.

## Query Patterns

With objects in files, agents answer portfolio questions with grep — no tooling required:

```bash
grep -rl "status: open" --include="*.md" .            # all undecided bets
grep -rl "rung: [1-3]" --include="*.md" .             # weak evidence in play
grep -rB2 "kill_date: 2026-06" .                      # verdicts due this month
grep -rl "allocated_to: null" .                       # unallocated capacity
grep -rA1 "stale_after" . | grep "2026-0[1-5]"        # expired evidence
```

Agents with memory should maintain the live join: every session, surface (1) bets past kill_date, (2) bets resting on stale or rung-1–3 evidence, (3) capacity mapped to no open bet.

## Adoption Path

Do not front-load the ontology. Adopt in this order, stopping where the business size stops paying for the next step:

1. **Decision only** (the journal — where every user starts).
2. **Decision + Bet** (adds kill dates and capacity honesty).
3. **+ Evidence with provenance** (claims become checkable).
4. **+ Outcome, Capacity, Risk** (full operating picture — feeds the Portfolio Command Deck, `operations/portfolio-command-deck.md`).

A solo founder with one bet needs stage 2. A business running four bets across two segments needs stage 4 — that is the point where memory fails and the file graph starts outperforming intuition.
