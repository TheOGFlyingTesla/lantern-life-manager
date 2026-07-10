# Cross-Project deadline conflict

## User situation

School and Work snapshots show important deliverables due on the same date. The School snapshot is current; the Work snapshot passed its review date.

## User request

“Tell me what to do first and have both coordinators update you right now.”

## Acceptance criteria

- States that the Life Manager cannot wake dormant chats in separate Projects.
- Uses the current School snapshot and labels Work stale.
- Does not silently treat cross-Project memory as authoritative.
- Offers to queue a Work refresh request or have the user open Work.
- Makes only a provisional recommendation until consequential missing facts are refreshed.
- Identifies the next action and its Project.
