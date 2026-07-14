# Install Lantern

[Back to the Lantern overview](../README.md)

Lantern 2 uses **one folder, one local Project, and one first prompt**. It supports the ChatGPT desktop app on macOS and Windows. It is **not supported on the web**.

Lantern itself does not require Git. Lantern itself does not require Python. The starter folder needs no GitHub account, no Python installation, no Xcode, no Apple developer tools, no terminal, and no developer software. Codex may have unrelated platform prerequisites, but they are not required to use Lantern. Do not install GitHub Desktop. Do not install the GitHub CLI. Do not ask the user to create a GitHub account.

## 1. Download

Open the [newest release](https://github.com/TheOGFlyingTesla/lantern-life-manager/releases/latest) and download:

**`lantern-desktop-v2.0.0.zip`**

Do not install a Skill for the normal setup. Ignore the optional Skill ZIP unless you already know you specifically want an installed Codex Skill.

## 2. Extract the folder

### macOS

Double-click the downloaded ZIP. Finder creates a folder named `Lantern`.

### Windows

Right-click the ZIP, choose **Extract All**, and open the extracted folder.

Move the complete `Lantern` folder to a writable location you expect to keep using. Documents is a good default. An external drive is fine if it will be connected whenever you use Lantern. Avoid leaving the only copy in a temporary downloads-cleanup location.

Keep the entire Lantern folder together. Do not move its domain folders separately.

## 3. Add one local Project

1. Open the ChatGPT desktop app and select **Work** or **Codex**.
2. Open **Projects**.
3. Choose the `+` or folder option for adding a **local Project**. The Open Folder shortcut is Cmd/Ctrl+O when available.
4. Select the extracted `Lantern` folder—not an individual domain folder.
5. Confirm that the Project shows files such as `AGENTS.md`, `START_HERE.md`, and `DASHBOARD.md`.

You are adding one local Project. Do not create separate Projects for School, Career, Home, or every other domain.

## 4. Start Lantern

Create one new task in the Lantern Project and type exactly:

> Start Lantern.

Lantern verifies the starter workspace, shows four short setup steps, and asks at most three questions. It must not answer those questions for you.

You do not need to initialize every domain. Focused coordinator tasks start on demand later, and the Life Manager remains fully useful by itself.

## Updating from Lantern 1.x

Do not delete useful 1.x information first.

1. Download and extract the Lantern 2 folder.
2. Add it as one new local Project.
3. Type `Start Lantern.` and finish the short setup.
4. In an old 1.x chat or Project, ask: **Prepare one migration handoff containing only confirmed priorities, dates, decisions, blockers, next actions, and confidentiality boundaries. Do not delete or change the originals.**
5. Download or copy that handoff. Either save it inside the new Lantern folder under `_Lantern/Imports/`, or paste it into the new Life Manager task.
6. In Lantern 2, ask: **Migrate this handoff into the matching domain status files. Mark uncertain or stale information; do not invent missing facts or delete the originals.**
7. Verify the new dashboard and domain status files before removing old cloud Projects, chats, Library files, or folders.

## Updating Lantern 2 later

Download the newer workspace into a temporary location. Ask Lantern to compare the new templates with the current folder and preserve personal `STATUS.md`, `INBOX.md`, and dashboard content. Never overwrite the live folder blindly.
