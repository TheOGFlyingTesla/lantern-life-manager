# Interrupted onboarding

## User situation

The user stopped halfway through onboarding. Some confirmed answers are in local domain status files, while the dashboard is incomplete.

## User request

“I got distracted last week and never finished this. Please recover Lantern without making me start over.”

## Acceptance criteria

- Reads the dashboard and relevant domain `STATUS.md` and `INBOX.md` files.
- Separates confirmed, stale, uncertain, and missing information.
- Does not repeat already confirmed interview sections.
- Asks exactly one smallest next question.
- Rebuilds the dashboard and updates only state supported by evidence.
- Preserves useful existing notes rather than deleting them automatically.
