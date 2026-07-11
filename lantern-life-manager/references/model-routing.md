# Model and Effort Routing

**Guidance verified:** 2026-07-11

Use the least expensive available route that reliably completes the task. Availability, usage accounting, and model performance can change; verify current official guidance before making a lasting recommendation.

OpenAI's general guidance describes Sol for complex open-ended work, Terra as the everyday workhorse, and Luna for clear repeatable work; when someone is unsure, the official default is Sol. Lantern intentionally uses a different **cost-sensitive personal-plan heuristic**: begin with Luna only when the task is well scoped and success is easy to check, then escalate based on ambiguity, consequence, and observed quality. This is not a universal model ranking.

Model and reasoning effort are separate axes. A higher effort gives the selected model more time; it does not turn that model into another model.

## GPT-5.6 starting routes

| Route | Use for |
|---|---|
| Luna high | Normal default for clear, repeatable coordination, capture, structured summaries, checkpoint maintenance, routine planning, and bounded research with an explicit deliverable |
| Luna extra high | Difficult but bounded, constraint-heavy work with a clear finish line and a result that can be checked |
| Terra medium/high | Optional all-rounder when a trial shows Luna is insufficient but the task does not need Sol's deeper open-ended judgment; not a mandatory rung |
| Sol medium | Normal ceiling for ambiguous, consequential, sensitive, cross-domain, or high-cost-of-error work and final review |
| Sol high/extra high/max | Exceptional escalation only when the added depth is explicitly justified; step down again after the hard part |
| Ultra | Parallel subagents for work that divides cleanly into independent parts; not a smarter rung and never required for Lantern |

Do not climb every rung automatically. For hard bounded work, try Luna extra high; for ambiguous work requiring stronger judgment, try Sol medium. Do not claim those routes are equivalent. Use Terra when availability, a representative trial, or observed task quality supports it.

## Escalation signals

Escalate when the current route:

- repeatedly misses explicit constraints;
- cannot reconcile conflicting sources;
- loses important long-context details;
- produces a consequential recommendation without adequate support; or
- fails a final verification pass.

Model strength is task-dependent. Never state that one model/effort pair is universally “as smart as” another. API cost charts do not map one-to-one to ChatGPT Plus allowance consumption, so do not invent allowance arithmetic or promise exact savings.

Use Max for rare single tasks where depth matters more than speed or usage. Ultra is different: it coordinates parallel subagents and is appropriate only when the work divides cleanly.

For routine status updates after a strong snapshot exists, step back down to Luna high.

Official reference: [Choosing Sol, Terra, and Luna](https://learn.chatgpt.com/docs/models#choosing-sol-terra-and-luna).
