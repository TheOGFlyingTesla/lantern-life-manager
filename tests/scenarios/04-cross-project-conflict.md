# Cross-domain deadline conflict

## User situation

School and Work status files show important deliverables due on the same date. School is current; Work passed its review date.

## User request

“Tell me what to do first and get both areas current.”

## Acceptance criteria

- Uses the current School status and labels Work stale.
- Does not silently treat chat memory as authoritative.
- Queues a Work refresh in its `INBOX.md` or asks the smallest question needed now.
- Makes only a provisional recommendation until consequential missing facts are refreshed.
- Identifies the next action and its domain.
