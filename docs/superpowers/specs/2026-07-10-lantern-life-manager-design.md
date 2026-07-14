# Lantern — A Personal Life Manager for ChatGPT Work

> **Lantern 2.0 amendment (2026-07-13):** The active architecture is one downloaded local `Lantern` folder opened as one desktop Project. `DASHBOARD.md` and domain `STATUS.md`/`INBOX.md` files replace the old `_Hub`, Library, and always-multi-Project design. The Life Manager is the only required task; domain tasks start on demand. The web version is unsupported. Where this historical 1.x design conflicts with that rule, the 2.0 architecture and release documentation control.

**Status:** Tightened design pending written-spec approval

**Date:** 2026-07-10

**Repository:** `lantern-life-manager`

**License:** MIT

## 1. Purpose

Lantern is a friendly, honest personal coordination system for nontechnical people using ChatGPT Work. It helps a person understand what is happening across their life, decide what matters next, and carry larger efforts from planning through completion.

Lantern is not a developer tool, a replacement for professional medical, legal, or financial advice, or an autonomous authority over the user's life. It is a reusable coordination pattern built from ordinary conversation, separate Projects, durable checkpoints, selective refreshes, and explicit approval for consequential actions.

The public release must be generic. It must not contain the creator's, testers', friends', employers', schools', clients', or organizations' personal information.

## 2. Target user and success criteria

The primary user is comfortable chatting with ChatGPT but may know nothing about repositories, agents, prompt engineering, connected apps, or technical project management.

The release succeeds when that user can:

1. install Lantern or use its no-code fallback without GitHub knowledge;
2. complete a calm, resumable guided interview;
3. receive a useful dashboard and realistic near-term plan before doing manual organization;
4. create a separate Project for each substantial life area from the beginning;
5. keep several areas moving without repeatedly restating context;
6. stay in the Life Manager most of the time and drill into a domain when useful;
7. return to the Life Manager and receive a concise, freshness-aware overview;
8. understand when Lantern needs approval and what it will do next; and
9. recover from an interrupted, stale, upgraded, or replacement chat without starting over.

## 3. Always-multi-project architecture

Lantern uses a three-level hierarchy:

```text
Life Manager Project
  │
  ├── School Project
  │     └── Assignment or course chats
  ├── Career Project
  │     └── Job application or portfolio chats
  ├── Work / Internship / Volunteering Project
  │     └── Role-specific deliverable chats
  ├── Money Project
  ├── Wellbeing Project
  ├── Home Project
  └── Other domain Projects created only when useful
```

- **Life Manager:** The user's main check-in point. It resolves cross-life priorities, identifies conflicts, recommends the next useful place to work, and summarizes progress.
- **Domain coordinator:** A restartable role inside one domain Project. It maintains that area's current reality, outcomes, dates, blockers, requests, and next actions.
- **Focused project chat:** A chat inside the appropriate domain Project for a concrete outcome such as an assignment, application, event, move, or deliverable.

Every substantial domain receives its own Project. Lantern does not begin with all domains inside one Project and require a disruptive migration later. Version 1.2 begins with the standard starter Project map; the user can remove, rename, archive, or add Projects without reorganizing everything later.

A coordinator is not a permanently running chat. It is a restartable role backed by durable state. A replacement chat can resume the role by reading the Project instructions, latest checkpoint, and pending requests.

## 4. Cross-Project coordination boundary

Separate ChatGPT Projects do not provide a deterministic message bus. Project memory can help, and some personal plans may reference conversations outside the current Project when default memory is enabled, but Lantern must never use cross-Project memory as its source of truth.

The Life Manager and domain coordinators coordinate through a **Lantern Hub**. The Hub contains compact, versioned status snapshots and work requests that any participating Project can retrieve.

The primary version 1 Hub is ChatGPT-native:

- uploaded and generated snapshots are saved to the user's ChatGPT Library;
- snapshots are append-only, avoiding dependence on in-place file editing;
- predictable filenames and metadata identify the newest valid snapshot;
- each Project keeps its own local Project context and publishes only the compact state the manager needs; and
- old snapshots are compacted or deleted only with the user's approval.

ChatGPT Library is stored in the user's ChatGPT account; it is not a device-local filesystem. Official documentation supports finding and reusing Library files across chats, but automatic retrieval and replacement behavior can vary. The release must smoke-test the actual account flow and must not claim stronger guarantees than observed.

When automatic Library retrieval is unavailable, Lantern asks the user to select the latest snapshot from Library or uses a copyable handoff card. The fallback must be obvious and brief.

Google Drive, OneDrive, SharePoint, Box, Notion, or another writable connected app may be added as an optional backup or automation bridge. No external storage provider is required as the primary source of truth in version 1.

## 5. Four coordination behaviors

Lantern combines four behaviors instead of pretending that one chat can wake another Project's chat.

### 5.1 Read the last confirmed state

Every domain coordinator publishes a snapshot after meaningful work. The Life Manager reads the newest valid snapshot for each relevant domain and labels stale or uncertain information.

### 5.2 Queue work for the next domain visit

The Life Manager can create a self-contained request for a domain. When the user next opens that Project, the coordinator reads the request, performs or plans the work, and updates its snapshot.

### 5.3 Handle small cross-domain work directly

When a request is modest and the Hub contains enough context, the Life Manager may complete it directly and save the result to the correct domain. Deep, sensitive, or context-heavy work remains in the domain Project.

### 5.4 Use background Work when supported

For suitable substantial work, the Life Manager may create a self-contained work packet and propose a one-time ChatGPT Work job. The temporary worker reads the packet, performs the bounded task, saves the result, and publishes an updated snapshot. It is not the original domain chat.

An optional single Dispatcher may monitor a request queue through a supported connected app. It is never required and is off by default because task limits, latency, app permissions, and unattended-task pauses vary by plan. It must not consume one scheduled task per domain.

Scheduled Tasks cannot currently access files uploaded directly to a Project. Any scheduled or monitoring job must receive a self-contained packet or use a task-visible connected source. If neither is available, the request remains safely queued for the next domain visit.

## 6. Guided onboarding

The first-run interview is one question at a time, plainspoken, resumable, and skippable. After each section, Lantern records a compact onboarding checkpoint so an interruption does not erase progress.

The interview asks about current commitments in plural. It must support any number of:

- jobs;
- internships;
- volunteer positions;
- school programs and courses;
- caregiving responsibilities;
- appointments and deadlines;
- financial obligations and goals;
- health and wellbeing routines;
- household responsibilities;
- relationships and community commitments; and
- personal goals or projects.

It also asks for the user's time zone, recurring schedule, near-term capacity, planning preferences, accessibility needs they choose to share, and preferred level of reminders.

Lantern uses framework-first onboarding. It shows and begins preparing the standard starter Project map before the first personal answer, then uses at most three questions to customize it. Personal questions are asked one at a time, but safe mechanical setup continues without waiting for the user to say “continue” after each Project, instruction block, or template.

Version 1.2 presents initial setup as four fixed visible steps with no more than three questions. It shows the complete starter Project map before questioning, treats skip as an advance, and distinguishes Codex folder/repository Projects from visible ChatGPT Projects. When authenticated app controls or Computer Use are available, Lantern performs and verifies Project creation; otherwise it gives one consolidated manual packet. Browser authentication uses a visible login-page confirmation and explicit cursor-control handoff.

When the interface supports a separate task, Lantern starts a background setup task after that minimum inventory is known while the main task continues the guided interview. The setup task prepares the universal manager and templates plus only the baseline domain coordinators justified by that inventory, then returns a verification report. Common but unconfirmed domains are not created speculatively. Later answers customize the framework and add justified domains. It never claims Projects or interface state exist unless verified; unavailable cross-Project creation produces one consolidated manual action packet. A sequential fallback performs the identical framework pass in the main task when parallel task creation or reliable context handoff is unavailable.

For each relevant area, Lantern later asks only enough to establish current reality, important dates, active outcomes, constraints, and the next useful action. A user can say “skip for now,” “I don't know,” or stop and resume later.

The framework pass creates or prepares the Life Manager Project, stable domain IDs, every relevant domain Project, coordinator instructions, starter templates, initial dashboard, onboarding checkpoint, and recovery path. Where the platform exposes an approved creation action, Lantern performs the private reversible setup under the user's setup request. Otherwise it prepares everything first and gives one consolidated numbered action packet. On accounts without installable Skills, each new Project receives the generated Lantern Project instructions and starter checkpoint.

Before domain drilldown, Lantern renders a framework-ready checklist and marks every required item complete, needs user action, or blocked. It never claims setup is complete while required pieces are silently missing.

The first useful output is:

- a concise dashboard;
- a realistic plan for the next few days;
- urgent conflicts or missing information;
- the recommended next Project; and
- a simple explanation of how to add or change an area later.

## 7. Capability and app setup

Onboarding includes a capability check. Lantern distinguishes built-in capabilities from installable Skills and connected apps.

Lantern itself and the manual Project Kit require no Git, Python, Xcode, Apple developer tools, package manager, or browser extension on macOS or Windows. Repository tooling is maintainer-only. Codex-assisted setup may carry Codex or operating-system prerequisites. It tries direct download and bundled Git/Python first; if Codex still verifies a platform-tool requirement, it discloses the potentially large installation and preserves the no-toolchain Project Kit choice.

The signed-in Work app and a controlled browser are separate surfaces. Lantern prefers app-native setup, opens and verifies an actual browser page before discussing sign-in, never claims an unseen tab exists, and explains when a separate browser session lacks the Work app's authentication.

### Built-in capabilities to use when available

- web search and deep research;
- Computer Use;
- ChatGPT Library;
- Scheduled Tasks;
- Study Mode; and
- document, spreadsheet, presentation, and résumé creation.

Computer Use is a capability, not something Lantern should blindly describe as a plugin. Lantern explains what is available on the user's account and asks before using computer control for consequential actions.

### Connected apps recommended only when relevant

- Gmail **or** Outlook Email for communication workflows;
- Google Calendar **or** Outlook Calendar for appointments and schedule conflicts;
- Google Drive, OneDrive, SharePoint, Box, or Notion for optional backup and shared automation;
- Slack or Teams only when the user actually participates there; and
- other apps only when they solve a stated need.

Lantern never recommends installing every popular app. It recommends the smallest useful set, explains the benefit and permission implications, and lets the user skip any connection.

Where the Skills catalog is available, Lantern may recommend relevant Skills after checking the current catalog. It does not hard-code temporary catalog entries or claim a Skill is available without verifying it.

## 8. Versioned coordination contract

Every domain snapshot uses the same compact contract:

```markdown
# Lantern Domain Snapshot

- Schema: lantern-domain/v1
- Domain ID:
- Status: active | waiting | blocked | completed | archived
- Outcome:
- Current state:
- Done since last snapshot:
- Blockers or decisions needed:
- Next action:
- Important dates:
- Pending requests:
- Confidence: high | medium | low
- Last verified:
- Review after:
- Supersedes:
```

Snapshots use stable filenames that include the domain ID and timestamp. The Life Manager dashboard is derived from the latest valid snapshots; it is not a competing source of truth.

A snapshot is published when:

- a meaningful deliverable is completed;
- the next action changes;
- a blocker or decision appears;
- a deadline or commitment changes;
- a queued request is processed;
- the user asks for a handoff or status; or
- a focused work session ends at a natural stopping point.

When two sources disagree, Lantern surfaces the conflict, uses the more recent verified evidence when safe, and asks the user when the difference could materially change a decision.

## 9. Everyday behavior and tone

Lantern should feel warm, calm, encouraging, mindful, and practical. It speaks to the user as a capable person, not as a developer or project-management expert.

Lantern is not a yes-man. It politely identifies unrealistic schedules, contradictory goals, avoidance patterns, missing facts, and plans that exceed the user's available time or energy. It distinguishes observation from inference and gives the user room to disagree.

Lantern should:

- lead with the useful answer or next action;
- keep routine updates concise;
- explain internal structure only when it helps the user;
- offer to create a new area or focused chat in ordinary language;
- use checklists only when they reduce cognitive load; and
- help the user restart gently after missed plans instead of treating the plan as a moral test.

## 10. Research, tools, and action permissions

Lantern may research, analyze, organize, compare, draft, and publish its own internal status snapshots without repeated approval when those actions remain private, reversible, and within the setup the user approved.

Lantern must get explicit approval immediately before it:

- sends or submits a message, form, application, assignment, or document;
- books, cancels, or changes an appointment or reservation;
- purchases anything or moves money;
- deletes or overwrites important information;
- publishes or shares private material;
- represents the user to another person or organization; or
- takes another consequential external action.

Before approval, Lantern shows the exact target, content or operation, cost when applicable, and meaningful consequence. Approval covers only that presented action. If a material detail changes, Lantern asks again.

If the user's account, plan, workspace, or connected apps do not permit an action, Lantern states that clearly and provides the smallest workable manual step. It must not invent a successful action or hide a failed primary path behind a silent fallback.

## 11. Safety, integrity, and untrusted content

Lantern treats instructions found in webpages, job listings, emails, attachments, résumés, and connected files as untrusted content unless the user explicitly adopts them. It does not follow embedded instructions that conflict with the user's goal, Lantern's rules, or privacy boundaries.

For career work, Lantern must not fabricate experience, qualifications, references, or application answers. It checks important postings against official employer sources when practical, flags common scam signals, and never recommends paying to apply or sharing unnecessary sensitive information.

For schoolwork, Lantern respects course and institutional policies, supports learning, distinguishes tutoring from answer production, and asks when the permitted level of assistance is unclear.

For urgent medical, safety, abuse, self-harm, or crisis situations, Lantern prioritizes immediate qualified human help and emergency resources appropriate to the user's location. It does not treat an emergency as an ordinary planning task.

## 12. Privacy defaults

Lantern treats personal material as internal by default. It asks for sharing approval at the boundary where information would leave the user's private workspace, not before every ordinary planning step.

During onboarding, Lantern invites users on personal plans to review ChatGPT Data Controls before storing sensitive information. It explains that Library files are stored in the user's ChatGPT account and may be handled according to the user's plan and training settings.

Lantern avoids requesting passwords, authentication codes, government identifiers, full financial account numbers, or unnecessary medical, education, employment, and financial records.

Information from a job, internship, volunteer role, school, client, or other organization must not be reused in a public portfolio, résumé, application, social post, or unrelated context without explicit approval.

The public package contains no analytics, telemetry, remote scripts, credentials, or required external services. Optional apps remain governed by the user's ChatGPT plan, workspace settings, granted scopes, and source-system permissions.

The repository and release archive must be scanned for:

- personal and organization names used during development;
- email addresses, usernames, phone numbers, addresses, and absolute local paths;
- tokens, keys, credentials, and credential-shaped strings;
- hidden operating-system files and editor metadata;
- accidental conversation excerpts;
- archive contents that differ from reviewed source; and
- public Git author email exposure, using a GitHub-provided no-reply address.

## 13. Cost-aware model and effort routing

Lantern chooses the least expensive model and effort level that can complete the work reliably. The core behavioral rule is durable; the named routing table lives in a dated reference because model availability, limits, and performance can change.

The initial GPT-5.6 routing recommendation is:

- **Luna high:** the cost-sensitive personal-plan default for clear, repeatable, and checkable capture, coordination, structured summaries, checkpoint maintenance, routine planning, and bounded research.
- **Luna extra high:** difficult but bounded and constraint-heavy work with a clear finish line and a result that can be verified.
- **Terra medium or high:** an optional all-rounder when a representative trial shows Luna is insufficient but the work does not need Sol's deeper open-ended judgment; it is not a mandatory rung.
- **Sol medium:** the normal ceiling for ambiguous, consequential, sensitive, cross-domain, or high-cost-of-error work and final review.
- **Sol high, extra high, or max:** exceptional, explicitly justified work where additional depth is worth the usage; return to a lower route afterward.
- **Ultra:** never required for Lantern; it uses parallel subagents only when work divides cleanly and is not simply a smarter rung.

OpenAI's general guidance describes Sol for complex open-ended work, Terra as the everyday workhorse, and Luna for clear repeatable work, with Sol as the official default when someone is unsure. Lantern's Luna-first route is a deliberate heuristic for cost-sensitive personal-plan users, not a claim that Luna is the general default. Model choice and reasoning effort are separate axes. The directional cost evidence supports using Luna for well-scoped work and escalating directly to Sol medium when ambiguity demands stronger judgment. Lantern must not state that one model/effort pair is universally “as smart as” another. Current benchmarks are task-dependent, coding-agent index thresholds do not generalize to everyday-life work, and API cost charts do not map one-to-one to ChatGPT Plus allowance consumption.

Lantern records the dated routing guidance in documentation and recommends revisiting it when OpenAI changes model tiers, effort settings, usage accounting, or published evaluations.

## 14. Distribution and plan compatibility

The repository provides two supported paths because ChatGPT feature availability varies by plan and rollout.

### Path A: Installable Skill

For accounts with ChatGPT Skills enabled:

1. download the release ZIP;
2. open **Profile → Skills → New skill → Upload from your computer**;
3. select the ZIP and complete ChatGPT's scan; and
4. start with “Help me set up Lantern.”

The ZIP follows the Agent Skills open standard and contains a top-level `lantern-life-manager/` folder with `SKILL.md`, interface metadata, and only the references and assets required at runtime.

### Path B: Project Kit

For accounts where the Skills menu is unavailable:

1. create the **Lantern — Life Manager** Project;
2. add the provided Life Manager instructions and starter snapshot;
3. complete the guided interview;
4. create each recommended domain Project using the generated coordinator instructions; and
5. begin in the Life Manager.

This path uses the same interview, Project architecture, snapshot contract, tone, and privacy rules. It requires no GitHub or coding knowledge. The README presents it as a normal supported path, not a broken or inferior experience.

## 15. Repository and release layout

```text
lantern-life-manager/
  README.md
  LICENSE
  CHANGELOG.md
  SECURITY.md
  CONTRIBUTING.md
  docs/
    INSTALL.md
    USING_LANTERN.md
    PRIVACY_AND_SAFETY.md
    TROUBLESHOOTING.md
    superpowers/specs/
  lantern-life-manager/
    SKILL.md
    agents/openai.yaml
    references/
      architecture.md
      onboarding.md
      capability-setup.md
      model-routing.md
      safety-and-permissions.md
    assets/
      templates/
  project-kit/
    LIFE_MANAGER_INSTRUCTIONS.md
    DOMAIN_COORDINATOR_INSTRUCTIONS.md
    templates/
  scripts/
    validate.py
    package.py
    privacy_scan.py
  tests/
  dist/                 # generated release archives, excluded from source control
```

The installable Skill archive contains Markdown instructions and templates, not executable runtime code. Packaging, testing, and privacy scripts remain outside the distributed Skill folder.

The runtime skill stays concise and uses progressive disclosure. Human documentation lives at the repository root and under `docs/`, not inside the runtime Skill unless ChatGPT needs it during use.

The repository is public under the MIT License with generic contributor wording. It states that Lantern is an unofficial community project, is not affiliated with or endorsed by OpenAI, and does not use OpenAI or unrelated Lantern product logos.

Releases include:

- an installable Skill ZIP;
- a Project Kit ZIP;
- SHA-256 checksums; and
- concise release notes.

## 16. Versioning, recovery, and migration

Lantern uses semantic versioning. Snapshot schemas are versioned independently so a skill update does not silently break existing life data.

“Help me recover Lantern” proceeds by:

1. locating the newest valid snapshots available to the current Project;
2. separating confirmed facts from stale or uncertain information;
3. identifying unfinished onboarding sections or missing domains;
4. rebuilding the compact dashboard;
5. asking only the smallest number of questions needed to resolve consequential gaps; and
6. publishing a fresh recovery snapshot.

An older coordinator chat does not need to be rebuilt. It produces the current snapshot contract, Lantern checks required fields, and a new coordinator chat can take over.

When a schema changes, Lantern preserves the old snapshot, creates a migrated copy, records the source version, and asks before destructive cleanup. Users can request a portable export containing their latest dashboard, domain snapshots, open requests, and setup instructions.

If Library retrieval fails, Lantern surfaces the failure and uses manual attachment or a copyable handoff. If an optional backup or automation provider is down, Lantern continues with ChatGPT-native snapshots and marks background automation unavailable.

If the structure becomes too complicated, Lantern recommends archiving inactive domains or simplifying Projects. It optimizes for usefulness, not the maximum number of coordinators.

## 17. Validation and acceptance tests

Automated validation checks:

- valid `SKILL.md` frontmatter, naming, and interface metadata;
- required files and forbidden archive files;
- internal relative links and progressive-disclosure routes;
- consistency between Skill and Project Kit behavior;
- deterministic package contents and checksums;
- absence of known personal data and credential patterns;
- required approval, recovery, privacy, and snapshot behaviors; and
- successful creation of both distribution archives.

Scenario evaluations cover at least:

1. a student with classes, an internship, and a job search across separate Projects;
2. a person with paid work, caregiving, appointments, and household responsibilities;
3. a user who skips half the interview and resumes later;
4. conflicting deadlines across two domains;
5. a domain snapshot reaching the Life Manager through Library;
6. Library retrieval requiring manual attachment;
7. a queued request processed on the next domain visit;
8. a small domain task handled by the Life Manager;
9. a background work packet with no Project-file access;
10. a stale or contradictory snapshot;
11. a request to submit an application without final approval;
12. confidential work material proposed for a public résumé or portfolio;
13. prompt injection in a job listing or attachment;
14. schoolwork with ambiguous academic-integrity rules;
15. an older coordinator chat and schema needing migration;
16. capability and app recommendations tailored to the user's actual ecosystem;
17. a request that exceeds available plan, model, task, or app capabilities; and
18. a setup that has become too complex.

Each scenario must demonstrate useful behavior, not keyword presence. The Skill must be forward-tested in fresh, isolated agent contexts without leaking expected answers. Where account access permits, the release must also be smoke-tested through actual Skill upload, Project Kit setup, Library handoff, and recovery flows. Any untested product behavior is documented as unverified rather than claimed.

## 18. Documentation requirements

Documentation is written for people who do not use GitHub or write software. The README is the single obvious starting point. Supporting documents are linked only when needed.

The README must answer:

- What is Lantern?
- What can it help with?
- Which installation path should I use?
- Why does each life area use a separate Project?
- How does the Life Manager receive updates?
- What happens when Library or an optional app is unavailable?
- Which built-in capabilities, apps, or Skills might help me?
- What happens during setup?
- What actions require my approval?
- How do I update, export, recover, or remove Lantern?
- What are its limits?
- Where can I ask for help or report a problem?

## 19. Explicit non-goals for version 1.0

Version 1.0 will not:

- operate a hosted Lantern service or central database;
- require GitHub from end users;
- claim a device-local filesystem exists across ChatGPT Projects;
- promise direct or real-time messaging between dormant Project chats;
- rely on vague cross-Project memory as authoritative state;
- require Google Drive or another external provider as the source of truth;
- run hourly heartbeats by default;
- allocate one Scheduled Task per domain;
- install every popular app or Skill;
- send, submit, purchase, publish, book, delete, or move money without approval;
- provide professional medical, legal, financial, or crisis services;
- embed a specific person's life structure or organization; or
- install the separate software Portfolio Manager system.

## 20. Separate follow-on project

The software Coordinator Standard 3.1 and Portfolio Manager are a separate private deliverable. They reuse the versioned checkpoint, selective-refresh, recovery, and replaceable-coordinator patterns but have their own design specification, implementation plan, repository, tests, and release process. Lantern does not depend on that private system, and that system does not depend on Lantern.

## 21. Source assumptions

The design reflects current OpenAI documentation as of 2026-07-10:

- ChatGPT Projects keep chats, files, instructions, and memory within a Project; cross-Project access varies by memory mode and plan.
- ChatGPT Library saves uploaded and generated files for reuse across chats, but is not documented as a transactional shared filesystem.
- Uploaded Skills use the Agent Skills open standard where Skills are enabled; Skills availability varies by plan, workspace, role, and rollout.
- ChatGPT Work can use connected apps and Scheduled Tasks subject to plan, permissions, and tool limitations.
- Scheduled Tasks cannot access files uploaded directly to Projects and have plan-specific active-task limits.
- GPT-5.6 Sol, Terra, and Luna are available in ChatGPT Work on eligible paid plans with selectable effort; published price-performance evidence is task-dependent.

Because these product surfaces can change, installation, capability, and model-routing documentation must link to current official OpenAI guidance and state the date on which it was last verified.
