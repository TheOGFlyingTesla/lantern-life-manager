# Set Up Lantern with Codex

[Back to the Lantern overview](../README.md)

Use this path when ChatGPT Work cannot create or configure the complete multi-Project framework by itself. Codex acts as the setup operator; ChatGPT Work remains the destination where the Life Manager and domain Projects live.

You should not need a terminal or developer knowledge. Tell Codex:

> Install Lantern from the public `TheOGFlyingTesla/lantern-life-manager` repository, then set up the complete framework in ChatGPT Work. Prefer direct download and Codex's bundled runtimes. Do not invoke system developer tools silently. If this Codex installation requires an operating-system prerequisite, explain it and the manual Project Kit alternative before installing anything. Establish the entire framework before domain drilldown and show me the framework-ready checklist.

## How Codex should install the Skill

Codex should use its installed Skill installer and choose direct GitHub archive download with `--method download`. That path does not need Git.

Before running any helper, Codex should load its workspace dependencies and use the returned **bundled Python** executable. It must not assume that `python3` is installed on macOS or Windows.

If direct download is unavailable and a repository operation is genuinely necessary, Codex should use the exact **bundled Git** executable returned by its workspace dependency loader before trying macOS system Git.

**Codex itself may require** an operating-system prerequisite in some environments. If a verified Codex operation still asks for Xcode Command Line Tools or Apple developer tools, stop before installing. Explain that this may be a **large download** and consume substantial disk space, and let the user decide between installing the Codex prerequisite and using the no-code Project Kit. Do not describe it as a Lantern dependency. On Windows, use the Codex-provided runtime or the Project Kit; Apple developer tools do not apply.

After installation, Codex may need a new turn or a fresh thread before the newly installed Skill appears. It should verify that Lantern is available before claiming installation succeeded.

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

The decision order is the same on macOS and Windows: direct download first, bundled runtimes second, then disclose any verified Codex platform prerequisite before installing it. The manual Project Kit remains the no-developer-tool fallback. Git and Python are maintainer tools for the Lantern repository, not requirements of Lantern itself.
