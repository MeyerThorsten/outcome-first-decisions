# Blind-Spots Register

Tracks the user's habitual evidence-rung skips, recurring anti-pattern occurrences, and calibration drift by category. Memory-dependent.

The register is the most useful artifact in the decision journal once 10+ entries exist. It names the user's specific failure mode rather than re-explaining the Buyer Evidence Ladder every session.

## Schema

```yaml
---
user_id: [stable identifier — name, slug, or email; whatever survives across sessions]
last_updated: 2026-04-28
review_window: rolling 90 days

patterns:
  - rung_skipped: 6              # rung the user habitually does not reach before committing
    frequency: 8/12_predictions  # observed in this many of the last N entries
    domain: validation           # validation | prioritization | pricing | hire | partnership | offer | channel
    note: "Tends to commit to building before any rung-6 evidence."

  - rung_skipped: 5
    frequency: 5/12_decisions
    domain: prioritization
    note: "Skips qualified-conversation step; moves from interest to scope."

recurring_anti_patterns:
  - name: "Polishing Before Proof"
    last_observed: 2026-04-21
    occurrences: 3
    domains: [validation, offer]

  - name: "Sunk-Cost Loyalty"
    last_observed: 2026-04-14
    occurrences: 2
    domains: [prioritization]

calibration_drift:
  - category: validation
    expected_rate: 0.60
    actual_rate: 0.42
    sample_size: 12
    direction: overconfident
    next_adjustment: "Cap stated confidence at 50% in this category for next 90 days."

  - category: pricing
    expected_rate: 0.60
    actual_rate: 0.65
    sample_size: 11
    direction: calibrated
    next_adjustment: "No adjustment."
---
```

## How the Skill Uses This Register

When the user states a new prediction or decision, the agent:

1. **Checks the patterns block.** If the new decision falls in a domain where the user habitually skips a rung, the agent surfaces it: *"You typically commit to building before rung 6. The current case is at rung 3 — make this decision a test, not a build."*
2. **Cites recurring anti-patterns by name.** If the new situation matches a pattern with `occurrences ≥ 3`, the agent names it: *"This is your third Polishing-Before-Proof loop in 6 weeks. The earlier two killed weeks 2 and 4."*
3. **Applies calibration drift.** If `direction: overconfident` in the relevant category, the agent discounts new confidence claims and shows the math.

The register is never quoted to the user verbatim — the agent translates it into specific, current-context language.

## When the Register Updates

After every decision-journal entry receives an outcome (filled `outcome:` and `lesson:` fields), the agent:

1. Recomputes pattern frequencies over the rolling 90-day window.
2. Increments `occurrences` for any anti-pattern observed in the entry's lesson.
3. Updates `calibration_drift` for the entry's category if the rolling sample is ≥ 10.
4. Updates `last_updated`.

## When the Register Is Unavailable

If memory is off or no register exists yet, the agent:

1. Does not invent patterns. The skill operates without citation.
2. Marks responses with `[no calibration data available]` when stating any probability or rung guidance.
3. Asks the user, once per session, whether they want to share recent decision-journal entries to bootstrap the register.

## Hard Rules

- Patterns are observations, not labels. The agent uses them to surface choices, not to scold or define the user.
- The register is the agent's note, not a user dashboard. Don't display the YAML; translate it into specific current-context language.
- If a pattern's frequency drops below 3/N over the rolling window, drop it from the register. Patterns that no longer recur should not generate friction.
- The register has a maximum of 5 active patterns and 5 active anti-patterns. Beyond that, the noise overwhelms the signal — keep the most recent and most frequent.

## Privacy

The register lives wherever the user's decision journal lives. It is no more sensitive than the journal itself. If the user is on a memory-shared platform, recommend they review the register every 90 days and prune anything they don't want surfaced.

## Bootstrapping

For users with an existing decision journal but no register yet:

1. Read the last 10-30 entries.
2. For each entry, note: rung at decision time, the verdict, the actual outcome, any anti-patterns mentioned in the lesson.
3. Tally rung-skips by domain. Any rung skipped in 50%+ of entries in a domain becomes a pattern.
4. Tally anti-pattern mentions. Any anti-pattern with 3+ occurrences in 90 days becomes a recurring entry.
5. Compute calibration drift only when a category has 10+ entries with filled outcomes.

The first register is rarely complete. It improves with use.
