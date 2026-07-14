# Architecture and Coordination

## One local Project

Lantern 2 is **local-first** and uses **one local Project** pointing at the downloaded `Lantern` root folder. The folder may live anywhere writable and dependable. No Git repository, GitHub account, database, cloud ChatGPT Project, or fixed `Documents/Lantern` path is required.

```text
Lantern/
├── AGENTS.md
├── START_HERE.md
├── DASHBOARD.md
├── LANTERN_VERSION.md
├── _Lantern/
│   └── Templates/
└── Domains/
    ├── AGENTS.md
    ├── Personal/
    ├── Home/
    ├── Career & Job Search/
    ├── Work, Internships & Volunteering/
    ├── School & Learning/
    ├── Finances/
    ├── Appointments & Admin/
    ├── Health & Wellbeing/
    └── Relationships & Community/
```

Do not create cloud ChatGPT Projects. Do not create a Git repository. Cloud storage is optional backup only.

## Durable domain handoffs

Every domain owns:

- `START_HERE.md` — its purpose;
- `STATUS.md` — confirmed state, dates, blockers, and next action; and
- `INBOX.md` — queued requests from the Life Manager.

The Life Manager reads all domain files because the single local Project points at the Lantern root. A focused task updates its domain `STATUS.md`; the manager later reads it. Tasks do not need to wake or directly message one another.

Use `DASHBOARD.md` as the cross-domain overview. Mark information confirmed, stale, uncertain, blocked, or unknown. Never choose silently between conflicting facts.

## Focused tasks on demand

The Life Manager is the only required task. Start domain coordinator tasks **on demand** when focused work would help. Do not create or pin one task per domain during initial setup.

When a focused task stays at the Lantern root, explicitly read `Domains/AGENTS.md` and the named domain folder. When a task starts inside a domain folder, nested `AGENTS.md` discovery supplies the domain guidance automatically.

## Add or archive domains

Create new domains inside `Domains/` by copying the three files from `_Lantern/Templates/`. Replace placeholders without inventing user facts and add the domain to `DASHBOARD.md`. Preserve files when renaming. Archive or delete only with exact-action approval.

## Recovery

For recovery, read `DASHBOARD.md` plus every relevant `STATUS.md` and `INBOX.md`. Separate confirmed information from stale, conflicting, or unknown information; ask the smallest necessary question; then update the affected files. These durable files replace the old onboarding checkpoint and `_Hub` architecture.

## Portable export and optional backup

The Lantern folder is already a portable export. For a smaller export, copy the latest dashboard, relevant domain status and inbox files, and the instruction files into a new folder. Ask before sharing it outside the user's private workspace.

External drives, Time Machine, OneDrive, Google Drive, and similar services may back up the folder. They are never required as Lantern's live source of truth.
