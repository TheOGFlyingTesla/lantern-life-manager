# Model and Effort Routing

**Guidance verified:** 2026-07-10

Use the least expensive available route that reliably completes the task. Availability, usage accounting, and model performance can change; verify current official guidance before making a lasting recommendation.

## GPT-5.6 starting routes

| Route | Use for |
|---|---|
| Luna high | Default coordination, capture, summaries, ordinary research, reminders, checkpoint maintenance, and most planning |
| Luna extra high | Complex but bounded analysis, drafting, comparison, or planning when high misses constraints |
| Terra medium/high | Selective long-context, finance, science/health, or computer-use work where current evidence or a trial shows a material advantage over Luna |
| Sol medium | Consequential cross-domain decisions, difficult synthesis, sensitive final review, or meaningful cost of error |
| Sol high/max | Rare work where added reliability is worth the usage |
| Ultra | Optional parallel work where available; never required for Lantern |

Do not default to Terra light merely because Terra sits between Luna and Sol. Broadly prefer Luna, then escalate based on task evidence. For many hard tasks, compare Luna extra high with Sol medium rather than automatically using Terra extra high.

## Escalation signals

Escalate when the current route:

- repeatedly misses explicit constraints;
- cannot reconcile conflicting sources;
- loses important long-context details;
- produces a consequential recommendation without adequate support; or
- fails a final verification pass.

Model strength is task-dependent. Never state that one model/effort pair is universally “as smart as” another. API token prices do not prove how a personal ChatGPT usage allowance is consumed.

For routine status updates after a strong snapshot exists, step back down to Luna high.
