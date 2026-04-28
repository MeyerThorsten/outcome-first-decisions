# Prediction Tracking

Calibration over time. Are the user's predictions actually predicting?

A user who says "I'm 80% sure this will work" should be right 80% of the time when they say that. Most people are not. The gap between stated confidence and actual outcome is the most useful metric in the decision journal.

## Why Track Calibration

- It exposes overconfidence. Most founders rate predictions 70-90% confident; outcomes are usually 40-60%. The gap costs money.
- It exposes underconfidence. Rarer but real — the user under-invests in approaches that consistently work.
- It separates judgment from luck. A 70%-confidence prediction that turns out to be wrong does not mean the call was wrong. The pattern across many predictions tells the truth.

## The Calibration Table

After every decision-journal entry has an outcome, log it here.

| ID                          | Confidence | Outcome correct? | Notes                       |
| --------------------------- | ---------- | ---------------- | --------------------------- |
| 2026-04-28-cohort-presale   | 60%        | yes              | Hit 6 deposits by deadline. |
| 2026-04-21-vendor-x         | 50%        | no               | 0 named intros at day 30.   |
| 2026-04-14-feature-pilot    | 80%        | yes              | 3 LOIs signed.              |
| 2026-04-07-conf-keynote     | 30%        | yes              | Killed; no pipeline.        |

Group entries by stated confidence. Compute the actual hit rate per band.

## The Calibration Bands

| Stated confidence | Should hit | Sample threshold |
| ----------------- | ---------- | ---------------- |
| 90%               | ~9 in 10   | min 10 entries   |
| 80%               | ~8 in 10   | min 10 entries   |
| 70%               | ~7 in 10   | min 10 entries   |
| 60%               | ~6 in 10   | min 10 entries   |
| 50%               | ~5 in 10   | min 10 entries   |
| 40%               | ~4 in 10   | min 10 entries   |
| 30%               | ~3 in 10   | min 10 entries   |

Below 10 entries per band, the data is noise. Above 10, patterns become visible.

## How to Read the Patterns

### Pattern: Overconfident across all bands

90%-confidence predictions hit 70% of the time. 80% hits 60%. Etc.

**Diagnosis:** the user is selling themselves on the upside, not predicting.

**Fix:** reduce all stated confidence by 15-20 points until calibration returns. Start every prediction by writing the strongest case *against* the verdict before stating the probability.

### Pattern: Overconfident at 80-90%, calibrated below

80% predictions hit 60%, but 50% predictions hit 50%.

**Diagnosis:** the user is overconfident specifically when they like the idea.

**Fix:** when about to state 80%+ confidence, name the rung of evidence first. If evidence is below rung 6, cap the prediction at 60%.

### Pattern: Underconfident across all bands

50% predictions hit 70%. 40% predictions hit 60%.

**Diagnosis:** the user is under-investing in their own judgment.

**Fix:** when stating confidence, look at the evidence rung. Rung 6+ evidence supports a prediction above 70%. Stop hedging when the evidence is there.

### Pattern: Calibrated on validation, miscalibrated on prioritization

Validation predictions track well; prioritization predictions don't.

**Diagnosis:** the user has clean evidence for individual ideas but not for compared ones.

**Fix:** force a Worth Filter on every prioritization decision. The forced scoring makes the comparison evidence-based.

## Common Trap: Outcome Reweighting

After a prediction is wrong, the temptation is to rewrite the original confidence ("I knew it was risky"). Don't.

The original probability is the data. Outcome reweighting destroys the calibration record.

If the prediction was wrong, the lesson goes in the **outcome** field of the decision log — not in the prediction field of the calibration table.

## Quarterly Calibration Review

Every 90 days, with at least 30 entries logged:

1. **Compute hit rate per confidence band.** Compare to the expected rate.
2. **Identify the largest gap.** That gap is the next calibration adjustment.
3. **Set the next-quarter rule.** "For the next 90 days, predictions in [domain X] are capped at 70% until calibration improves."
4. **Re-read the lessons from wrong predictions.** Look for the recurring pattern. Update the user's Conversation Rules to address it.

## When Calibration Doesn't Matter

Calibration tracking has overhead. Skip it when:

- The user is making fewer than 5 logged decisions per month. Sample size will not support patterns.
- The user is in a single 90-day sprint with one big decision. Calibration is a long-term tool.
- The user is in a crisis mode where decisions are forced by external constraint, not judgment.

In every other case, the calibration table is the highest-leverage spreadsheet the user keeps.
