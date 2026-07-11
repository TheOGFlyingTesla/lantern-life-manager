# Install Lantern

[Back to the Lantern overview](../README.md)

You do not need GitHub knowledge. **Lantern itself does not require Git** and **Lantern itself does not require Python**; manual Skill upload and the Project Kit require no developer software on macOS or Windows.

The downloads are public: you do not need a GitHub account, GitHub Desktop, the GitHub CLI, or a repository clone. Open the newest release page in an ordinary browser and download the ZIP you need.

## First: check for a Skills menu

1. Open ChatGPT.
2. Select your profile.
3. Look for **Skills**.

If you see it, use the Skill path. If you do not, use the Project Kit path. Both implement the same Lantern behavior.

## Path A: install the Lantern Skill

1. Download `lantern-life-manager-v1.1.1.zip` from the newest release.
2. In ChatGPT, open **Profile → Skills → New skill → Upload from your computer**.
3. Choose the ZIP without unzipping it.
4. Review ChatGPT's scan result. Stop if ChatGPT blocks the package or shows an unexpected capability.
5. Create a new Project named **Lantern — Life Manager**.
6. Start a chat inside it and say **Help me set up Lantern.**

The Skill is reusable across the separate Projects Lantern creates. After the minimum domain inventory, Lantern should prepare and verify the complete justified framework before drilling into any one domain.

## Path B: use the Lantern Project Kit

Use this path when the Skills menu is absent.

1. Download `lantern-project-kit-v1.1.1.zip` from the newest release.
2. Unzip it by opening the downloaded file.
3. Open `START_HERE.md`.
4. Create a new ChatGPT Project named **Lantern — Life Manager**.
5. Copy all of `LIFE_MANAGER_INSTRUCTIONS.md` into that Project's instructions.
6. Upload the four template files or add them from ChatGPT Library.
7. Start a chat inside the Project and say **Help me set up Lantern.**

### Open the Project Kit on macOS or Windows

- **macOS:** double-click the ZIP in Downloads. Finder creates an extracted folder. Open `.md` instruction files in TextEdit or another plain-text editor, press **Command-A**, then **Command-C**.
- **Windows:** right-click the ZIP, choose **Extract All**, and open the extracted folder. Open `.md` instruction files in Notepad or another plain-text editor, press **Ctrl-A**, then **Ctrl-C**. Do not try to upload files from inside the compressed ZIP view.

In ChatGPT, open the target Project's **Project settings**, find its instructions field, and paste the entire instruction file. Replace `[DOMAIN NAME]` and `[DOMAIN ID]` before saving a domain Project. Upload each template to the Project that owns it and confirm the filename appears in that Project's files.

To **verify the Project**, start a new chat there and ask: “What Lantern role, domain name, and domain ID do you have?” The Life Manager should identify itself as the Life Manager; a domain Project should report the values you entered. If it cannot, recheck the Project instructions before continuing.

Lantern will recommend one Project per substantial active life area. It should prepare the complete Project list, stable domain IDs, coordinator instructions, templates, dashboard, and checkpoint before detailed domain work. For each domain Project, copy `DOMAIN_COORDINATOR_INSTRUCTIONS.md` into its Project instructions and replace the two bracketed domain fields. Then upload `domain-snapshot.md` and `work-request.md` to each domain Project, or paste their contents into a starter chat there. A separate domain Project cannot see files uploaded only to the Life Manager Project. If manual actions are required, Lantern should give one consolidated numbered list and then verify the framework-ready checklist—not stop after every file and wait for “continue.”

## During onboarding

- Answer one question at a time.
- Say **skip for now** for anything you do not want to answer.
- Say **I don't know** when information is uncertain.
- Stop whenever you want. Say **Help me recover Lantern** when you return.

Lantern should produce a useful dashboard and next-few-days plan before asking you to connect optional apps.

## Optional: automate setup with Codex

If ChatGPT Work cannot create the complete Project structure directly and you already use Codex, follow [Set up Lantern with Codex](CODEX_ASSISTED_SETUP.md). Codex should try direct download and its bundled runtimes first.

The optional **Codex-assisted setup may require** prerequisites belonging to Codex or macOS. If Codex asks for Xcode Command Line Tools or Apple developer tools, it must explain the potentially large download before installation and offer the Project Kit as the no-toolchain alternative.

Lantern's manual setup should not ask you to install Git, Python, Xcode, Apple developer tools, Homebrew, or another developer toolchain. Codex should try direct download and bundled workspace tools first. If Codex itself genuinely requires a platform prerequisite, it should explain the cost and offer the Project Kit before installing anything.

## Optional capabilities and apps

Lantern may recommend built-in Computer Use, web research, Library, Scheduled Tasks, Study Mode, or document tools. It may suggest Gmail or Outlook, a calendar, storage backup, Slack, or Teams only if those match your life.

You can skip every optional connection. Ask Lantern what an app can read or change before connecting it.

## Update Lantern

1. Download the newest matching ZIP.
2. Keep your existing Project chats and snapshots.
3. Replace the installed Skill, or replace the Project instructions with the new copies.
4. Say **Check my Lantern setup after this update.**

Lantern preserves old snapshots and creates migrated copies when its snapshot schema changes.

## Remove Lantern

- Skill path: uninstall or delete Lantern from the Skills page.
- Project Kit path: remove the Lantern instructions from each Project.
- Delete Projects or Library files only if you also want to delete your content.
- Disconnect optional apps from ChatGPT Settings when you no longer want them connected.

Removing Lantern does not automatically delete your chats, Projects, Library files, or third-party data.
