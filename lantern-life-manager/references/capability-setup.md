# Capability and App Setup

## Audit before recommending

Check what the user's plan, region, device, and workspace actually expose. Do not claim a capability exists because it is popular or newly announced. If availability cannot be verified, give the user the shortest place to check.

## Separate Lantern requirements from Codex requirements

**Lantern itself does not require Git** and **Lantern itself does not require Python**. The manual Skill-upload and Project Kit paths require no Xcode, Apple developer tools, Homebrew, package manager, or browser extension on macOS or Windows. Git and Python in this repository are maintainer tooling.

**Codex-assisted setup may require** prerequisites belonging to Codex or macOS rather than Lantern. First attempt direct download and use the **bundled Git** and Python runtime reported by the Codex workspace. If that Codex installation still presents a verified requirement for Xcode Command Line Tools or Apple developer tools, explain before installation that it can be a large download and consume substantial disk space. Let the user choose between installing the Codex prerequisite and using Lantern's no-code Project Kit path. Never present it as a hidden Lantern dependency. On Windows, use the Codex-provided runtime or manual Project Kit; Apple tooling does not apply.

## Built-in capabilities

Use when available without describing them as plugins:

- web search or deep research for current information;
- Computer Use for approved browser or desktop interaction;
- ChatGPT Library for saved snapshot reuse;
- Scheduled Tasks for limited reminders or monitoring;
- Study Mode for learning-centered school support; and
- document, spreadsheet, presentation, résumé, and job-search tools.

Computer Use is a capability. Explain what will be controlled and obtain exact-action approval before consequential clicks, uploads, messages, or submissions.

## Work app, browser, and sign-in

Treat the signed-in ChatGPT Work app and any controlled browser session as separate surfaces. Prefer the current Work app for Skills, Projects, Library, and ordinary Lantern setup. Do not open a browser merely to reproduce an app-native action.

When browser control is genuinely required, invoke the available bundled browser capability instead of guessing an example installation path. Open the actual page first and verify the expected page is visible before mentioning sign-in. Do not claim a tab is open when it has not been opened and verified.

A browser session may not share the Work app's authentication. If the verified page is signed out, explain that it is a separate browser session and either open the correct sign-in page or offer an app-native/manual fallback. Never tell the user to use an “open ChatGPT tab” unless that tab has actually been opened and verified.

## Connected apps

Recommend only apps that solve a stated need:

- Gmail **or** Outlook Email—not both unless the user uses both;
- Google Calendar **or** Outlook Calendar;
- Google Drive, OneDrive, SharePoint, Box, or Notion for optional backup or automation;
- Slack or Teams only for an active role that uses it.

For each recommendation, state:

1. what it enables;
2. what information it may access;
3. whether it can write or take actions;
4. whether the user can skip it; and
5. where to disconnect it later.

Prefer least privilege. Never recommend installing every popular app.

## Skills and plugins

Where a current Skills or plugin catalog is available, search it at the time of setup. Recommend a Skill only when it materially improves an established workflow and is available to the user's account. Explain that Skills and plugins do not grant access the user lacks.

Do not hard-code catalog entries that may disappear. If Skills are unavailable, use Lantern's Project Kit and built-in capabilities.

## Scheduled work

Keep scheduled work optional. Plus task limits are scarce, tasks may pause, and Project-uploaded files may be unavailable to them. Prefer one Dispatcher over one task per domain, and only when a task-visible connected source exists.
