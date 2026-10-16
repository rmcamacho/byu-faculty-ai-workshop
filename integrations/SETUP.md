# Set Up the Kuali and Workday Tutorials

The Kuali and Workday skills are part of the same workshop plugin as Learning Suite, **BYU Learning Suite, Kuali and Workday** (`byu-faculty-integrations`). If you followed step 3 of the [setup guide](../tutorial/SETUP.md#3--install-the-workshop-plugin), they are already installed.

## If You Have Not Installed the Plugin

Complete steps 1–3 of the [setup guide](../tutorial/SETUP.md): download this repository, install and sign into Codex CLI with your institution-approved account, and install the plugin. Node.js 22+ and Google Chrome are needed only for live browser work. The synthetic exercises (Parts A and B of each tutorial) need only Codex.

If you previously installed the August BYU Faculty Productivity plugin, see the note in step 3 about removing it so you don't have two Learning Suite skills.

## Check the Skills

Start a **new** Codex session after installing, then:

> Use $byu-kuali and $byu-workday. Without opening a browser, confirm both skills loaded and summarize what each will and will not do. Stop if either is unavailable.

## Choose a Tutorial

- [Kuali proposals](kuali/TUTORIAL.md): research direction → verified opportunity → concept, then find every discrepancy between a proposal workspace and a Kuali record.
- [Workday finances and tasks](workday/TUTORIAL.md): interpret a balance report correctly and triage an inbox without approving anything.

## Live Use

Live Kuali and Workday steps are optional and use your own access. The same dedicated Chrome window used for Learning Suite serves both; sign in yourself and never give the assistant passwords, Duo codes, cookies, or browser profiles. Run Codex in a local terminal so Chrome opens on your own computer. Check the current [BYU data guidance](https://ai.byu.edu/chatgpt-edu-data-restrictions-page) before using AI on live records, especially Workday pages that show other people's information.

## Validation Status

The plugin's browser helpers pass the original nine tests (`node --test tests/cli_tools.test.mjs`), and installation from a clean extraction of the workshop ZIP was tested with Codex CLI 0.153 on Linux. The Kuali and Workday skills have not yet been exercised end to end against live BYU Kuali or Workday pages from a participant's machine; treat live steps as a pilot.
