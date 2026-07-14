# Lantern

### A friendly way into agentic AI for everyday life

Lantern turns the ChatGPT desktop app into a practical Life Manager. It helps you see what matters, coordinate school, work, job searching, money, home, appointments, wellbeing, and relationships, and move forward without learning developer tools or agent architecture.

Think of Lantern as a light in the dark when AI sounds powerful but you do not know where to begin. Download one ready-made folder, open it as one local Project, type `Start Lantern`, and follow four short setup steps.

Lantern is free, open source, and designed for non-technical people managing real lives.

> Lantern is an unofficial community project. It is not affiliated with or endorsed by OpenAI.

## Install Lantern

Lantern 2 has one supported setup:

1. Download **`lantern-desktop-v2.0.0.zip`** from the [newest release](https://github.com/TheOGFlyingTesla/lantern-life-manager/releases/latest).
2. Extract it and move the complete `Lantern` folder somewhere you want to keep it.
3. In the ChatGPT desktop app, add that folder as **one local Project**.
4. Start one task and type:

> Start Lantern.

That is the entire activation process. Do not install a Skill, Git, GitHub, Python, or developer tools. You do not need to create a Project or task for every domain.

Read the friendly [installation guide](docs/INSTALL.md) for illustrated-in-words macOS and Windows steps.

Lantern 2 is intentionally desktop-only. It is **not supported on the web** because the web interface cannot provide the same dependable local file coordination.

## How Lantern works

The download already contains:

- one Life Manager instruction file;
- a starter dashboard;
- nine common life-domain folders;
- durable status and request files for every domain; and
- templates Lantern can use to add new domains later.

The Life Manager is the only required task. It reads the domain files, notices conflicts or stale information, and keeps the dashboard useful. Focused domain tasks are created on demand when School, Career, Home, or another area needs dedicated work.

All tasks in the local Project can work with the same folder. A domain task updates its own `STATUS.md`; the Life Manager reads that file later. They do not need fragile cross-Project memory or direct chat-to-chat messaging.

## What can it help with?

- balance deadlines across school, work, internships, volunteering, caregiving, and home;
- find jobs and tailor a truthful résumé for each posting;
- prepare applications while stopping for approval before submission;
- plan homework and studying within academic-integrity rules;
- organize appointments, routines, budgets, errands, and household work;
- research options and turn them into realistic next actions;
- prepare messages, documents, spreadsheets, and presentations; and
- recover after plans change or a task is replaced.

## Everyday use

Stay in the Life Manager for questions such as:

- “What should I do next?”
- “Give me a realistic plan for the next three days.”
- “What is stale, blocked, or competing for my time?”
- “Add a domain for caregiving.”

Ask for a focused task when one area needs concentrated work. Lantern can create or guide that task when the current desktop interface supports it; otherwise, continue in the Life Manager without losing functionality.

Read [How to use Lantern](docs/USING_LANTERN.md).

## Privacy and control

Lantern's source-of-truth files live in the local folder you selected. Chats and files may still be processed or retained according to your ChatGPT account, workspace, and Data Controls settings. Cloud storage is optional backup, not Lantern's source of truth.

Lantern treats personal information as internal by default. It asks immediately before sending, submitting, booking, buying, publishing, deleting important information, moving money, or sharing private material. It never needs passwords, authentication codes, government identifiers, or full account numbers.

Review [Privacy and safety](docs/PRIVACY_AND_SAFETY.md).

## Recover, export, update, or remove Lantern

- Say **Help me recover Lantern** to rebuild the dashboard from domain files.
- Say **Export my Lantern setup** to prepare a smaller private copy.
- Keep the entire folder together when moving it.
- Back up the folder like any other personal document folder.
- Delete the local Project connection to stop using Lantern; delete the folder only if you also want to delete its information.

See [Troubleshooting](docs/TROUBLESHOOTING.md).

## Advanced optional Skill

The release also includes `lantern-skill-v2.0.0.zip` for experienced users who specifically want Lantern as an installed Skill. It augments an existing Lantern desktop workspace; it does not include or replace the `lantern-desktop-v2.0.0.zip` workspace. It is not needed for the normal setup and is not the recommended starting point for new users.

## Current platform notes

Documentation was checked on **July 13, 2026** against OpenAI's current guidance for [Projects, chats, and tasks](https://learn.chatgpt.com/docs/projects), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), and [ChatGPT Work](https://learn.chatgpt.com/docs/get-started-with-work).

Product availability can vary by plan, workspace, device, and rollout. Lantern surfaces missing capabilities rather than pretending they worked.

## Contributing and security

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md). For security issues or accidental private information, follow [SECURITY.md](SECURITY.md) and do not post sensitive details publicly.

Lantern is released under the [MIT License](LICENSE).
