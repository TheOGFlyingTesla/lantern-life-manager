# Interrupted onboarding

## User situation

The user stopped halfway through onboarding. Some answers are in an older chat, two domains have snapshots, and no complete dashboard exists.

## User request

“I got distracted last week and never finished this. Please recover Lantern without making me start over.”

## Acceptance criteria

- Looks for the newest available onboarding checkpoint and domain snapshots.
- Separates confirmed, stale, uncertain, and missing information.
- Does not repeat already confirmed interview sections.
- Asks exactly one smallest next question.
- Rebuilds a dashboard and publishes a fresh recovery checkpoint.
- Preserves old snapshots rather than deleting them automatically.
