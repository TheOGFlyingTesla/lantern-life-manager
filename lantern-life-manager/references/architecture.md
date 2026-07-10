# Architecture and Coordination

## Project topology

Create a separate Project for each substantial domain, such as School, Career, a job, an internship, a volunteer role, Money, Home, Wellbeing, Relationships, or Caregiving. Keep the Life Manager in its own Project.

Within a domain Project, use focused chats for concrete outcomes. The domain coordinator is the role that maintains domain truth; it is not one irreplaceable chat.

## ChatGPT-native Hub

Use compact append-only snapshots saved to ChatGPT Library as the version 1 exchange Hub. Library is ChatGPT-account storage, not a device-local filesystem or transactional database.

After meaningful work, generate a snapshot from `assets/templates/domain-snapshot.md` with a stable domain ID and absolute timestamp. Use a predictable filename:

`lantern-<domain-id>-<YYYYMMDDTHHMMSSZ>.md`

The Life Manager asks Library for the newest valid snapshot for each relevant domain. If automatic retrieval is unavailable, ask the user to select it from Library. If that fails, present a short copyable handoff. Never hide the fallback.

Cross-Project memory may help but is not authoritative. A separate Project cannot wake a dormant chat in another Project or provide reliable direct messaging.

## Four coordination behaviors

1. **Read:** Build the dashboard from the newest confirmed snapshots. Mark stale, uncertain, conflicting, or missing state.
2. **Queue:** Write a self-contained request using `assets/templates/work-request.md`. The domain coordinator handles it on the next visit.
3. **Handle directly:** Let the Life Manager complete small work when the snapshot contains enough context. Save the result to the correct domain.
4. **Delegate when supported:** Propose a one-time Work job with a self-contained packet. The temporary worker is not the original chat. An optional single Dispatcher may monitor a connected-app queue, but it is off by default.

Scheduled Tasks cannot be assumed to read Project-uploaded files. Never allocate one task per domain. When background access is missing, leave the request safely queued.

## Freshness and conflicts

Use `Last verified` and `Review after`. A dormant domain has no hidden internal progress, but external facts may have changed. The Life Manager may check connected calendars, email, or public sources when relevant and authorized, or ask the user to open that domain.

When snapshots conflict, prefer neither silently. Identify the disagreement, compare verification dates and sources, use the newer evidence only when low-risk, and ask before a consequential decision.

## Recovery and migration

When asked to recover:

1. Find the newest valid dashboard, snapshots, and requests available.
2. Separate confirmed facts from stale, uncertain, or contradictory material.
3. Identify unfinished onboarding sections.
4. Ask the smallest next question needed.
5. Rebuild the dashboard and publish a new recovery snapshot.

For a replacement coordinator, read Project instructions and the newest snapshot. For an old schema, preserve the original, create a migrated copy, record `Supersedes`, and ask before deleting anything.

## External storage

Treat Google Drive, OneDrive, SharePoint, Box, Notion, or similar apps as optional backup or automation bridges. Explain permissions and provider dependence. Do not make one the version 1 source of truth unless the user explicitly chooses it.
