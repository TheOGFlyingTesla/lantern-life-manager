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

## Setup asks me to install Git, Python, Xcode, or Apple developer tools

Lantern itself does not need them. The manual Skill-upload and Project Kit paths work without a developer toolchain. Codex-assisted setup can have separate Codex or macOS prerequisites. Say:

> Stop before installing. Try direct download and Codex's bundled runtimes first. If Codex itself still requires this platform tool, explain its download and disk impact and offer the Project Kit alternative.

If Codex verifies that Xcode Command Line Tools or Apple developer tools are genuinely required, the user may choose to install them. That is a Codex platform decision, not a Lantern requirement. On Windows, Apple tooling is irrelevant; use the available Codex runtime or Project Kit.

## Setup asks me to install GitHub or create a GitHub account

Stop that path. Lantern's public ZIP files use anonymous download. Do not install GitHub Desktop, do not install the GitHub CLI, do not install Git, and do not create or sign in to a GitHub account for Lantern setup. Open the [newest release](https://github.com/TheOGFlyingTesla/lantern-life-manager/releases/latest) in a browser and download the Skill ZIP or Project Kit ZIP directly.

## Lantern says a ChatGPT browser tab is open, but I cannot see it

The signed-in Work app and a controlled browser session can be different. Lantern must open the actual page and verify it before asking you to sign in. It must not claim a tab is open when it is not visible.

Ask Lantern to stay in the Work app for app-native setup. If a browser is truly required, say:

> Open the actual page in the browser session, verify what is visible, and then explain whether that separate browser session needs sign-in.

If Computer Use cannot control the signed-in desktop app, it should use the verified browser page instead. Complete only the browser sign-in yourself; after that, Lantern should create and configure the Projects rather than handing the clicks back to you.

If no page opens, use the app-native or manual fallback instead of repeating a sign-in instruction.

## Setup stopped with only part of the framework

Say:

> Finish Lantern's framework-first setup before domain drilldown. Prepare every remaining artifact, then show the framework-ready checklist and one consolidated list of actions I must perform.

Lantern should preserve what already exists, complete or mark every required framework item, and only then begin detailed work in a domain.

## The recommended model is unavailable

Use the closest available route and narrow the task. For important work, add a separate review pass. Do not assume a different model is equivalent without evidence.

## There are too many Projects

Ask Lantern to review the structure. Archive completed or inactive domains and keep only substantial ongoing areas as Projects. Do not merge active domains merely to hide complexity.

## Start over without losing everything

Do not delete Projects first. Ask each active domain for a current snapshot, export the dashboard and open requests, then create replacement chats or Projects. Delete old content only after verifying the replacement.

## Report a problem

For behavior or documentation problems, open a GitHub issue without personal information. For a vulnerability or accidental private-data leak, follow [SECURITY.md](../SECURITY.md).
