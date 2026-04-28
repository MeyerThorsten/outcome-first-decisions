# Thorsten Meyer Skill

A practical business execution skill for agents that helps users decide what is worth doing, what needs proof, and what should be dropped.

The skill is built for founders, operators, creators, consultants, and teams who need sharper prioritization, faster validation, cleaner tradeoffs, and more concrete next actions.

## What It Does

- Validates business ideas with short proof tests and real buyer signals.
- Prioritizes opportunities using money, urgency, reach, repeatability, speed, and fit.
- Turns scattered goals into one scoreboard metric and a weekly action set.
- Finds tasks that are busywork, sunk cost, or low-value maintenance.
- Improves offers by clarifying the buyer, problem, promise, path, and ask.
- Helps decide whether to keep, change, defer, or kill work.
- Guides scaling from manual delivery to documentation, delegation, automation, and productization.

## How It Responds

For most business decisions, the skill pushes the agent to answer with:

1. **Verdict:** Worth doing, test first, change, defer, or drop.
2. **Why:** The business logic behind the recommendation.
3. **Score or evidence:** What is strong, weak, proven, or assumed.
4. **Proof test:** The smallest credible test to run next.
5. **Keep/change/kill criteria:** The thresholds for continuing, adjusting, or stopping.
6. **Next three actions:** Specific moves to take now.

## Example Prompts

```text
Use the thorsten-meyer-skill skill to validate this SaaS idea before I build it.

Use the thorsten-meyer-skill skill to choose between these three business opportunities.

Use the thorsten-meyer-skill skill to audit my current projects and tell me what to cut.

Use the thorsten-meyer-skill skill to turn my revenue goal into a seven-day execution plan.

Use the thorsten-meyer-skill skill to improve this offer and write a sharper buyer ask.
```

## Install

Place this folder in your agent's skills directory.

Codex example:

```bash
mkdir -p ~/.codex/skills
unzip thorsten-meyer-skill.zip -d ~/.codex/skills/
```

Claude example:

```bash
mkdir -p ~/.claude/skills
unzip thorsten-meyer-skill.zip -d ~/.claude/skills/
```

Any compatible agent can use the skill when the folder is placed in its skills directory and the agent supports skill loading.

## File Structure

```text
thorsten-meyer-skill/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
└── references/
    ├── principles.md
    ├── frameworks.md
    ├── mental-models.md
    ├── heuristics.md
    ├── anti-patterns.md
    ├── quotes.md
    └── sources.md
```

## Best Use

Bring the skill a specific idea, goal, bottleneck, list of options, project backlog, offer, channel plan, or weekly schedule. It works best when it can connect work to a buyer, metric, timeframe, and decision threshold.
