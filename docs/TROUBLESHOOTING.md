# Troubleshooting Lantern

[Back to the Lantern overview](../README.md)

## I do not have a Skills menu

Use the Project Kit. Skills availability varies by plan, workspace, and rollout. The Project Kit implements the same manager and coordinator behavior through Project instructions.

## The Life Manager cannot see another Project

That is expected with some memory settings and plans. Lantern should use the newest domain snapshot from ChatGPT Library.

1. Open Library.
2. Search for `lantern-` followed by the domain ID.
3. Choose the newest timestamped snapshot.
4. Add it to the Life Manager chat.

If that is inconvenient, ask the domain coordinator for a **copyable manager handoff** and paste it into the Life Manager.

## A coordinator did not update the manager

A separate Project cannot wake or directly message the Life Manager. Open the domain Project and say:

> Publish a fresh Lantern snapshot and tell me whether Library saving succeeded.

Then return to the Life Manager.

## Information conflicts or looks stale

Say:

> Help me recover Lantern. Separate confirmed, stale, uncertain, and conflicting information before making a plan.

Lantern should preserve old snapshots, compare dates and evidence, ask only consequential questions, and publish a new recovery snapshot.

## Background Work did not run

Scheduled and background capabilities vary. Tasks can pause, have plan limits, and may not access files uploaded directly to Projects. Lantern should keep the work request queued and show the smallest manual alternative.

## An app is unavailable

Continue with ChatGPT Library snapshots. External storage and communication apps are optional. If the missing app was needed for an external action, Lantern must say the action did not happen.

## The recommended model is unavailable

Use the closest available route and narrow the task. For important work, add a separate review pass. Do not assume a different model is equivalent without evidence.

## There are too many Projects

Ask Lantern to review the structure. Archive completed or inactive domains and keep only substantial ongoing areas as Projects. Do not merge active domains merely to hide complexity.

## Start over without losing everything

Do not delete Projects first. Ask each active domain for a current snapshot, export the dashboard and open requests, then create replacement chats or Projects. Delete old content only after verifying the replacement.

## Report a problem

For behavior or documentation problems, open a GitHub issue without personal information. For a vulnerability or accidental private-data leak, follow [SECURITY.md](../SECURITY.md).
