# Outcome-First Decisions

A practical business-decision skill that helps users decide what is worth doing, what needs proof, and what should be dropped — using buyer evidence, one scoreboard metric, and written kill criteria.

Built for founders, operators, creators, consultants, and teams who need sharper prioritization, faster validation, cleaner tradeoffs, and more concrete next actions.

## What It Does

- **Validates** business ideas with 7-day Cash Proof Sprints and real buyer signals.
- **Prioritizes** opportunities through the Worth Filter (money, urgency, reach, repeatability, speed, fit).
- **Forces verdicts** — keep, change, kill — with reclaimed capacity allocated to specific work, not freed in the abstract.
- **Maps scattered goals** to one scoreboard number and a three-action weekly plan.
- **Cuts** sunk-cost work, vanity work, and low-value maintenance creep.
- **Sharpens offers** by clarifying the buyer, urgent moment, promise, mechanism, and ask.
- **Guides scaling** through the Leverage Ladder (manual → document → delegate → automate → productize).
- **Tracks predictions** and calibration over time, so judgment improves with evidence.
- **Adapts to any vertical** — 12 industry overlays (SaaS, services/agency, creator, e-commerce, B2B, marketplace, local business, education/coaching, healthcare, fintech, hardware, nonprofit) plus an overlay builder that derives the signals for any unlisted industry.
- **Runs the whole portfolio** — every active bet on one command deck with evidence rungs, capacity allocation, and kill dates, governed by portfolio-level rules.
- **Grounds numbers in source systems** — scoreboard metrics carry provenance (source, as-of date, freshness) instead of being accepted from memory.

## How It Responds

For most business decisions, the skill answers in this shape:

1. **Verdict.** Worth doing, test first, change, defer, or drop.
2. **Why.** The business logic in plain language.
3. **Evidence read.** Strongest and weakest parts of the case, mapped to the Buyer Evidence Ladder.
4. **Proof test.** The smallest test that creates real evidence in 1-7 days.
5. **Keep / change / kill thresholds.** What result means continue, adjust, or stop.
6. **Next three actions.** Specific actions for today or this week.

The skill applies a self-check protocol before sending: every answer must contain a named buyer, one number, a 7-day proof test, a kill criterion, and three actions for today. If any is missing, the answer is not yet ready.

## Voice

The skill is direct, practical, and outcome-first. It does not motivate. It will challenge comfortable low-value work, push for buyer behavior over opinions, and recommend killing ideas plainly when the evidence says so.

## Example Prompts

```text
Use the outcome-first-decisions skill to validate this SaaS idea before I build it.

Use the outcome-first-decisions skill to choose between these three business opportunities.

Use the outcome-first-decisions skill to audit my current projects and tell me what to cut.

Use the outcome-first-decisions skill to turn my revenue goal into a seven-day execution plan.

Use the outcome-first-decisions skill to improve this offer and write a sharper buyer ask.
```

### Slash Commands (Claude Code)

```text
/validate [idea]               — verdict + 7-day proof test + kill criterion
/worth-filter [options]        — scored comparison + verdict per option
/kill-audit [list]             — keep/change/kill table + reclaimed capacity
/sharpen [offer]               — Buyer/Moment/Promise/Mechanism/Ask one-pager + pre-sale ask
/weekly-review [scoreboard]    — retrospective + next-week plan
/portfolio [bets]              — cross-bet command deck + portfolio verdicts
/log-decision [decision]       — open/close journal entries + calibration citation
/crisis-mode [situation]       — collapsed output: verdict + 3 hour-deadline actions + kill threshold
/stuck-to-shipped [load]       — 7-day audit → one number → proof-test protocol
```

## Install

The skill is distributed as a GitHub Release. Each tagged version ships an `outcome-first-decisions.zip` asset. Place the unzipped folder in your agent's skills directory.

Download the latest release:

```bash
gh release download --repo MeyerThorsten/outcome-first-decisions \
  --pattern 'outcome-first-decisions.zip'
```

Or pin a specific version:

```bash
gh release download v1.0.0 --repo MeyerThorsten/outcome-first-decisions \
  --pattern 'outcome-first-decisions.zip'
```

Then unzip into the right directory for your agent:

```bash
# Codex / OpenAI
mkdir -p ~/.codex/skills && unzip outcome-first-decisions.zip -d ~/.codex/skills/

# Claude Code
mkdir -p ~/.claude/skills && unzip outcome-first-decisions.zip -d ~/.claude/skills/

# Cursor
mkdir -p ~/.cursor/skills && unzip outcome-first-decisions.zip -d ~/.cursor/skills/
```

Any compatible agent can use the skill when the folder is placed in its skills directory.

## File Structure

```text
outcome-first-decisions/
├── SKILL.md                          # entrypoint
├── README.md
├── LICENSE
├── PROVENANCE.md                     # authorship and IP hygiene notes
├── references/
│   ├── principles.md                 # decision rules
│   ├── frameworks-core.md            # 6 core frameworks
│   ├── frameworks-extended.md        # supporting frameworks
│   ├── mental-models.md              # interpretive lenses
│   ├── anti-patterns.md              # behaviors to stop
│   └── one-liners.md                 # sharp rules of thumb
├── templates/
│   ├── worth-filter.md               # scoring table
│   ├── cash-proof-sprint.md          # 7-day test design
│   ├── kill-list.md                  # commitment audit
│   ├── weekly-review.md              # 20-min weekly plan
│   ├── offer-one-pager.md            # Buyer/Moment/Promise/Mechanism/Ask
│   └── portfolio-deck.md             # cross-bet command deck
├── examples/
│   ├── validation.md                 # "should I build X?" worked transcript
│   ├── prioritization.md             # 3 opportunities, scored
│   ├── kill-audit.md                 # project list audit
│   ├── crisis-mode.md                # collapsed output under runway pressure
│   └── portfolio.md                  # command deck across 5 bets
├── subskills/
│   ├── validate-idea/SKILL.md        # narrow flow: validate one idea
│   ├── kill-list/SKILL.md            # narrow flow: cut commitments
│   └── offer-sharpener/SKILL.md      # narrow flow: sharpen vague offer
├── workflows/
│   └── stuck-to-shipped.md           # 7-day Stuck-to-Shipped chain
├── operations/
│   ├── decision-ontology.md          # linked bet/evidence/capacity objects
│   ├── metrics-bridge.md             # source-grounded scoreboard numbers
│   └── portfolio-command-deck.md     # cross-bet operating picture
├── industry-overlays/
│   ├── saas.md
│   ├── services-agency.md
│   ├── creator.md
│   ├── ecommerce.md
│   ├── b2b.md
│   ├── marketplace.md
│   ├── local-business.md
│   ├── education-coaching.md
│   ├── healthcare.md
│   ├── fintech.md
│   ├── hardware-physical.md
│   ├── nonprofit.md
│   └── overlay-builder.md            # derive an overlay for any vertical
├── outreach/
│   ├── cold-outreach.md              # 5-sentence templates
│   ├── customer-interview-guide.md   # behavior-asking questions
│   ├── pre-sale-ask-language.md      # patterns for selling before building
│   └── objection-handling.md         # 5-category diagnostic
├── decision-journal/
│   ├── decision-log-format.md        # YAML schema entry format
│   ├── weekly-retrospective.md       # 5-question retro
│   ├── prediction-tracking.md        # calibration over time
│   └── blind-spots.md                # habitual rung-skips register
├── agents/
│   ├── claude.yaml
│   ├── openai.yaml
│   └── cursor.yaml
└── commands/                         # Claude Code slash commands
    ├── validate.md
    ├── kill-audit.md
    ├── worth-filter.md
    ├── sharpen.md
    ├── weekly-review.md
    ├── portfolio.md
    ├── log-decision.md
    ├── crisis-mode.md
    └── stuck-to-shipped.md
```

## Best Use

Bring the skill a specific idea, goal, bottleneck, list of options, project backlog, offer, channel plan, or weekly schedule. It works best when it can connect work to a buyer, metric, timeframe, and decision threshold.

## Provenance

`Outcome-First Decisions` is an independently authored skill by Thorsten Meyer. It is not a third-party persona skill, endorsement claim, or adaptation of another creator's package. See `PROVENANCE.md` for maintenance rules that keep the distributed package free of copied quotes, source lists, branded challenges, and externally named frameworks.

## License

Licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See `LICENSE`.

You may use, modify, and redistribute the skill under the terms of AGPL-3.0. If you run a modified version on a network-accessible service, AGPL-3.0 requires that you offer the modified source to its users.

---

By Thorsten Meyer.
