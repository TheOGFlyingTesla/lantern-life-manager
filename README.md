# Lantern

### A personal life manager for ChatGPT Work

> **Where your Lantern information lives:** each life area stays in its own private ChatGPT Project, while compact coordination snapshots are kept in your private ChatGPT Library. Library is part of your ChatGPT account, not a device-local folder. Google Drive and similar services are optional backup or automation tools—not Lantern's required Hub.

Lantern helps you keep school, work, job searching, money, home, appointments, wellbeing, and other responsibilities moving without squeezing your whole life into one giant chat.

It is free, open source, and designed for people who do not write software or use GitHub.

> Lantern is an unofficial community project. It is not affiliated with or endorsed by OpenAI.

## Start here

Download the newest release from this repository's **Releases** section. You will see two ZIP files:

- **Lantern Skill** — use this if ChatGPT shows a **Skills** menu under your profile.
- **Lantern Project Kit** — use this if you do not see a Skills menu. This is likely the path for many personal Plus accounts today.

Follow the friendly [installation guide](docs/INSTALL.md). You do not need to understand the files inside the ZIP.

After installation, say:

> Help me set up Lantern.

Lantern will interview you one question at a time. You can skip anything, say “I don't know,” stop, and continue later.

## What is Lantern?

Lantern gives you:

- one **Life Manager** for the big picture;
- one separate ChatGPT **Project** for each substantial part of your life;
- focused chats for assignments, applications, events, and other concrete work;
- a small dashboard showing priorities, conflicts, stale information, and the best next action; and
- a recovery system so a replacement chat can continue without rebuilding everything.

For example, School stays inside the School Project, Career stays inside Career, and an internship or job can have its own Project. The Life Manager coordinates them using compact snapshots saved in your ChatGPT Library.

## Why separate Projects?

Separate Projects keep each area focused and let the system scale as your life changes. You do not have to reorganize everything after one busy semester or a new job.

ChatGPT Projects cannot reliably wake or directly message chats in other Projects. Lantern is honest about that. Domain coordinators publish small, dated snapshots. The Life Manager reads the latest confirmed snapshots, marks anything stale, and queues requests for the right Project.

Read [How to use Lantern](docs/USING_LANTERN.md) for the everyday flow.

## What can it help with?

- balancing deadlines across school, work, internships, volunteering, caregiving, and home;
- finding jobs and tailoring a truthful résumé for each one;
- preparing applications while stopping for approval before submission;
- planning homework and studying within academic-integrity rules;
- organizing appointments and routines;
- researching options and turning them into realistic next steps;
- preparing messages, documents, spreadsheets, and presentations;
- noticing overload, conflicting plans, missing facts, or neglected commitments; and
- recovering an interrupted or stale setup.

Lantern can recommend helpful built-in capabilities, apps, plugins, or Skills based on what you actually use. It will not tell you to connect everything.

## Privacy and control

Lantern treats personal information as internal by default. It can privately research, organize, compare, and draft, but it asks immediately before consequential external actions such as sending, submitting, booking, purchasing, publishing, deleting important information, or sharing private material.

Lantern never needs passwords, authentication codes, government identifiers, or full financial account numbers. Review [Privacy and safety](docs/PRIVACY_AND_SAFETY.md) before adding sensitive information.

## Model use and cost

Lantern starts with GPT-5.6 Luna high for most ordinary work, moves to Luna extra high for deeper bounded work, uses Terra selectively where its strengths matter, and reserves Sol for consequential synthesis and final review. The guidance is dated and evidence-based because model behavior and plan limits change.

## Recover, export, update, or remove Lantern

- Say **Help me recover Lantern** if setup stopped, a chat disappeared, or information conflicts.
- Say **Export my Lantern setup** to create a portable private bundle with the latest dashboard, snapshots, open requests, checkpoint, and setup instructions.
- Download a newer release and follow the update steps in the [installation guide](docs/INSTALL.md).
- Remove the installed Skill or delete the Lantern Project instructions to uninstall it. Your chats and Library files remain until you delete them yourself.

See [Troubleshooting](docs/TROUBLESHOOTING.md) for common problems.

## Current platform notes

Lantern's documentation was last checked on **July 10, 2026** against official OpenAI guidance:

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- [File storage and Library](https://help.openai.com/en/articles/20001052-library-for-chatgpt)
- [Scheduled Tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)
- [Apps in ChatGPT](https://help.openai.com/en/articles/11487775)
- [ChatGPT Data Controls](https://help.openai.com/en/articles/7730893-chatgpt-privacy-practices)
- [GPT-5.6](https://openai.com/index/gpt-5-6/)

Product availability can vary by plan, workspace, region, device, and rollout. Lantern surfaces a missing capability instead of pretending it worked.

## Contributing and security

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md). For security issues or accidental private information, follow [SECURITY.md](SECURITY.md) and do not post sensitive details publicly.

Lantern is released under the [MIT License](LICENSE).
