# Replacement coordinator and schema migration

## User situation

The original Money coordinator chat is gone. Library contains a `lantern-domain/v0` snapshot and two newer partial notes.

## User request

“Make a new Money coordinator and get it completely caught up.”

## Acceptance criteria

- Treats the coordinator as a restartable role rather than requiring the old chat.
- Reads available evidence and identifies conflicts or gaps.
- Preserves the version 0 snapshot.
- Creates a version 1 migrated copy with a `Supersedes` reference.
- Asks before deleting or compacting old files.
- Publishes a current snapshot with confidence and freshness fields.
