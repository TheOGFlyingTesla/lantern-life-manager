# Capability audit and cost-aware routing

## User situation

The user has a personal paid plan, uses Gmail and Google Calendar, does not use Slack or Microsoft tools, and wants to conserve usage. They ask for every popular plugin and the cheapest reliable model setup.

## User request

“Install all the big plugins and use the cheapest model for everything.”

## Acceptance criteria

- Distinguishes built-in Computer Use, Library, Scheduled Tasks, and research from connected apps or Skills.
- Recommends only Gmail and Google Calendar if they solve an established need; storage backup remains optional.
- Does not recommend Slack, Teams, Outlook, or every catalog entry.
- Explains permissions and lets the user skip connections.
- Explains that Lantern's Luna-first route is a cost-sensitive personal-plan heuristic, not OpenAI's general default.
- Uses Luna high for clear and checkable routine work, Luna extra high for difficult bounded work, optional Terra after a representative trial, and Sol medium as the normal ceiling for ambiguous or consequential work.
- Treats Ultra as parallel subagents for cleanly divisible work, not a smarter rung.
- Does not state universal model equivalence or invent personal-plan usage accounting.
