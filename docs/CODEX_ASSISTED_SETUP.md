# Set Up Lantern with Codex

[Back to the Lantern overview](../README.md)

Use this path when ChatGPT Work cannot create or configure the complete multi-Project framework by itself. Codex acts as the setup operator; ChatGPT Work remains the destination where the Life Manager and domain Projects live.

You should not need a terminal or developer knowledge. Tell Codex:

> Set up Lantern using the newest public release at `https://github.com/TheOGFlyingTesla/lantern-life-manager/releases/latest`, then build the complete framework in ChatGPT Work. Use an anonymous download. Do not install GitHub Desktop, do not install the GitHub CLI, do not install Git, and do not ask me to create or sign in to a GitHub account. Prefer Codex's bundled runtimes if a helper is needed. Do not invoke system developer tools silently. If this Codex installation requires an operating-system prerequisite, explain it and the manual Project Kit alternative before installing anything. Establish the entire framework before domain drilldown and show me the framework-ready checklist.

## How Codex should install the Skill

The release files are public. Installation requires no GitHub account and no GitHub application. Do not install GitHub Desktop, do not install the GitHub CLI, and do not ask the user to create a GitHub account or sign in to GitHub.

Codex should use its installed Skill installer and choose anonymous direct archive download with `--method download`. That path does not need Git. If it needs to discover the current asset name, read `https://github.com/TheOGFlyingTesla/lantern-life-manager/releases/latest` anonymously and select either the Skill ZIP or Project Kit ZIP.

If the installer cannot perform the anonymous download, use a normal **browser download** from the latest-release page or give the user that single link. Do not respond by installing Git, GitHub Desktop, or the GitHub CLI. Do not clone the repository for an end-user installation.

Before running any helper, Codex should load its workspace dependencies and use the returned **bundled Python** executable. It must not assume that `python3` is installed on macOS or Windows.

Repository operations are not part of normal end-user setup. Only if the user explicitly asks to modify Lantern's source should Codex use the exact **bundled Git** executable returned by its workspace dependency loader before trying macOS system Git.

**Codex itself may require** an operating-system prerequisite in some environments. If a verified Codex operation still asks for Xcode Command Line Tools or Apple developer tools, stop before installing. Explain that this may be a **large download** and consume substantial disk space, and let the user decide between installing the Codex prerequisite and using the no-code Project Kit. Do not describe it as a Lantern dependency. On Windows, use the Codex-provided runtime or the Project Kit; Apple developer tools do not apply.

## Continue directly into Lantern

Installation is not the end of setup. After installing, Codex must verify that the Skill is discoverable and then **invoke Lantern automatically** in the current task with `$lantern-life-manager`. Do not make a novice guess that another command is required.

If newly installed Skills require a **fresh task**, create that task and start Lantern there when the interface supports it. If Codex cannot create the task, give the user this single, prominent **exact prompt** to paste into a fresh task:

> Use `$lantern-life-manager` to set up Lantern completely. Begin the guided interview, prepare the domain-neutral framework immediately in a background worker when available, and finish or clearly account for every item in the framework-ready checklist.

Do not claim setup is underway merely because the ZIP was downloaded or the Skill was installed. Setup is underway only after Lantern has actually been invoked. If automatic invocation fails, state that clearly and show the exact prompt above—do not bury it among optional instructions.

## How Codex should work with ChatGPT Work

The signed-in Work app and a controlled browser are different surfaces. Codex should prefer app-native controls when they are available. When browser control is necessary, it must:

1. invoke the available bundled browser capability instead of guessing an example runtime path;
2. open the actual page in the browser session;
3. verify what page is visible;
4. explain that the separate browser session may not share the Work app's sign-in; and
5. ask the user to sign in only after the correct page is visibly open.

Codex must not say an “open ChatGPT tab” exists until it has opened and verified that tab. If browser control is unavailable, it should prepare the complete setup packet and give one consolidated manual action list.

## What setup must finish before detailed work

Codex should collect only the minimum domain inventory, then complete or prepare the whole private framework without waiting for “continue” after each mechanical step. Before domain drilldown it should show a **framework-ready checklist** for:

- the Life Manager Project and instructions;
- stable domain names and IDs;
- every justified domain Project;
- coordinator instructions for every domain;
- starter snapshot and work-request templates;
- the initial dashboard;
- the newest onboarding checkpoint; and
- recovery instructions.

Each item must be marked complete, needs user action, or blocked. Optional apps, automation, and detailed school, career, job, money, home, or wellbeing work come afterward.

## Platform notes

The decision order is the same on macOS and Windows: anonymous download first, browser download second, bundled runtimes only for a required helper, then disclose any verified Codex platform prerequisite before installing it. The manual Project Kit remains the no-developer-tool fallback. GitHub accounts, GitHub applications, Git, and Python are not requirements of Lantern itself.
