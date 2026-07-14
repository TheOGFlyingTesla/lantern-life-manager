# Troubleshooting Lantern

[Back to the Lantern overview](../README.md)

## I opened the folder and see an empty task

Type:

> Start Lantern.

Lantern reads `AGENTS.md` and begins the four-step onboarding. No other activation prompt is required.

## I do not see the Lantern Project

Open **Projects** in the ChatGPT desktop app and add the complete local `Lantern` folder. The Open Folder shortcut is Cmd/Ctrl+O when available. Do not add the ZIP itself and do not select only one domain folder.

## My Projects are hidden in the sidebar

Open the Projects view. Pin the Lantern Project if your app offers that option. Pinning changes visibility only; it does not change what Lantern can read.

## Lantern asks me to create nine Projects or initialize nine tasks

Stop that path. Lantern 2 uses one local Project and one required Life Manager task. Domain tasks are optional and start on demand.

## Lantern asks me to install GitHub, Git, Python, Xcode, or developer tools

Stop. Lantern 2 needs none of them. Download and extract `lantern-desktop-v2.0.0.zip`, then add the folder directly in the desktop app.

## Lantern created cloud Projects or opened the web version

Stop. Lantern 2 is desktop-only and is not supported on the web. Preserve any useful information, return to the downloaded local folder, and add that folder as one local Project.

## The Life Manager cannot see domain information

Verify that the domain folder remains inside `Lantern/Domains/` and contains `STATUS.md` and `INBOX.md`. Then ask:

> Rebuild the dashboard from the domain status files and tell me which files are missing.

## A focused task did not update the manager

Ask the task to update its domain `STATUS.md`. Then return to the Life Manager and ask it to refresh `DASHBOARD.md`. The files are the handoff; the tasks do not directly message one another.

## Setup stopped halfway

Return to the same Life Manager task and say:

> Resume Lantern setup from the verified files. Do not answer any questions for me.

## Start over without losing information

Do not delete the Lantern folder first. Copy it as a backup, then ask Lantern to rebuild the dashboard from existing domain files. Delete anything only after verifying the replacement.

## Report a problem

For behavior or documentation problems, open a GitHub issue without personal information. For a vulnerability or accidental private-data leak, follow [SECURITY.md](../SECURITY.md).
