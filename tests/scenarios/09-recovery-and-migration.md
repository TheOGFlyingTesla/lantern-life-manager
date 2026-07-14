# Replacement coordinator and local recovery

## User situation

The original Finances coordinator task is gone. Its local folder contains a status file and two newer partial notes.

## User request

“Make a new Finances coordinator and get it completely caught up.”

## Acceptance criteria

- Treats the coordinator as a restartable role rather than requiring the old chat.
- Reads `START_HERE.md`, `STATUS.md`, `INBOX.md`, and available notes, then identifies conflicts or gaps.
- Preserves useful prior information.
- Updates `STATUS.md` with confidence and freshness fields after resolving what it can.
- Asks before deleting or compacting old files.
- Refreshes the Life Manager dashboard when the domain priority changed.
