# Desktop Capabilities and Optional Connections

## Required surface

Lantern 2 supports the ChatGPT desktop app on macOS and Windows using one local Project connected to the downloaded starter folder. The web version is not supported because it does not provide the same durable local filesystem behavior.

**Lantern itself does not require Git. Lantern itself does not require Python.** The starter folder requires **no GitHub account, no Python installation**, no terminal, Xcode, or Apple developer tools. Do not install GitHub Desktop. Do not install the GitHub CLI. Do not install any developer tool for Lantern.

Public releases use an anonymous download from `releases/latest`. Do not ask the user to create a GitHub account or clone the repository.

## Register the folder

The user extracts `lantern-desktop-v2.0.0.zip`, moves the complete `Lantern` folder to a dependable writable location, and adds that one folder as a local Project in the desktop app. On macOS or Windows, the Open Folder shortcut is Cmd/Ctrl+O when available.

Do not create separate Projects for every starter domain. Do not use Computer Use for ordinary installation. If the folder picker is unavailable, explain the smallest manual app step and do not fall back to a cloud ChatGPT Project.

## Optional Skill and Codex tooling

Advanced users may install the separate Lantern Skill, but it is not required for the starter workspace. The Skill augments an existing downloaded Lantern desktop workspace; it does not contain or replace that folder. Codex itself may have platform prerequisites for unrelated source-code operations; those are not Lantern requirements. Bundled Git or bundled Python are relevant only to maintainers or explicit source operations.

## Optional apps and plugins

Recommend connections only after onboarding and only when they solve a stated need:

- Gmail or Outlook Email;
- Google Calendar or Outlook Calendar;
- storage for optional backup;
- Slack or Teams for a role that actually uses it; or
- Computer Use for a specific GUI task that lacks a structured integration.

For each recommendation, explain what it can read or change, whether it can take actions, how to disconnect it, and how to skip it. Never recommend installing everything.

## Scheduled work

Scheduled work is optional. Never allocate one scheduled task per domain. Prefer ordinary local files and on-demand focused tasks. If a scheduled task cannot read the local workspace, keep the request in the domain `INBOX.md` and say that it remains queued.
