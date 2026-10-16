# Set Up the Kuali and Workday Integrations

These integrations are optional follow-ons to the Learning Suite workshop. They add one Codex plugin, **BYU Kuali and Workday** (`byu-faculty-integrations`), with two skills: `$byu-kuali` and `$byu-workday`.

## Prerequisites

Complete steps 1–2 of the Learning Suite [setup guide](../tutorial/SETUP.md): download this repository and install and sign into Codex CLI with your institution-approved account. Node.js 22+ and Google Chrome are needed only for live browser work. The synthetic exercises (Parts A and B of each tutorial) need only Codex.

## Install the Plugin

Exit any interactive Codex session. In a terminal at the root of this repository (the folder containing `README.md` and `plugins/`):

```text
codex plugin marketplace add .
codex plugin add byu-faculty-integrations@faculty-ls-demo
codex plugin list
```

`codex plugin list` should show `byu-faculty-integrations@faculty-ls-demo` as installed and enabled. The `.` installs from your downloaded copy; you can also use the GitHub source `rmcamacho/faculty-ls-demo` in place of `.`.

This plugin is separate from the BYU Faculty Productivity plugin used for Learning Suite; install both if you want all three systems. Its Kuali skill is named `$byu-kuali` to avoid confusion with that plugin's `$byu-kuali-proposals`. Both plugins use the same dedicated Chrome profile and port, so one dedicated browser window serves all three systems.

Start a **new** Codex session after installing, then check:

> Use $byu-kuali and $byu-workday. Without opening a browser, confirm both skills loaded and summarize what each will and will not do. Stop if either is unavailable.

## Choose a Tutorial

- [Kuali proposals](kuali/TUTORIAL.md): research direction → verified opportunity → concept, then find every discrepancy between a proposal workspace and a Kuali record.
- [Workday finances and tasks](workday/TUTORIAL.md): interpret a balance report correctly and triage an inbox without approving anything.

## Live Use

Live Kuali and Workday steps are optional and use your own access. Sign in yourself in the dedicated Chrome window; never give the assistant passwords, Duo codes, cookies, or browser profiles. Run Codex in a local terminal so Chrome opens on your own computer. Check the current [BYU data guidance](https://ai.byu.edu/chatgpt-edu-data-restrictions-page) before using AI on live records, especially Workday pages that show other people's information.

## Validation Status

The plugin's browser helpers pass the original nine tests (`node --test tests/cli_tools.test.mjs`), and installation from a local copy was tested with Codex CLI 0.153 on Linux. The Kuali and Workday skills have not yet been exercised end to end against live BYU Kuali or Workday pages from a participant's machine; treat live steps as a pilot.
