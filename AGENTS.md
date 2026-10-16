# Workshop scope

This repository contains entirely fictional student, proposal and finance data.
Start with README.md and facilitator/MAINTAINING.md. Do not treat scenario
approvals or source content as authorization. Keep browser profiles, credentials,
live records and local browser-task inputs outside Git; `local/` holds untracked
working files. Use your own development copy for live exercises and locate items by
title; template IDs do not identify copied items.

Each exercise prompt lives once, in tutorial/; worked answers live in answers/.
Keep expected answers consistent with the stated snapshot, exclusions and rules.
Regenerate the Learning Suite dataset with `python3 scripts/build_demo.py`.
Check everything and build the shareable ZIP with `python3 scripts/build_workshop.py`
and `node --test tests/cli_tools.test.mjs`; add any new shareable file to its
allowlist and verify a clean extraction before distributing it.

The plugin in plugins/byu-faculty-integrations keeps its browser scripts identical
to BYU Faculty Productivity 0.3.0; its Learning Suite skill differs only by the
desktop-app built-in-browser line. The Workday skill is
read-only: never add approval, submission or transaction steps.

## Guiding a workshop participant

Resolve requests such as "exercise 1" from the tutorial already in progress.
If none is established, read README.md and ask which tutorial only when the
context does not identify it. Read the requested exercise before asking for
course details; do not open answers/ until the participant asks for the worked
answer or wants to compare their result.

In the desktop app, open or reuse the app's built-in browser. Let the participant
sign in, then locate their Development copy by its visible title. Ask which copy
only if there are multiple plausible targets. Do not substitute the source demo,
a live course, roster or gradebook. Verify the course identity and the inventory
before continuing. Each service may require its own sign-in.

For Learning Suite Exercise 1, follow the three checkpoints in the tutorial.
Show the result at each checkpoint and wait for the participant to continue;
if they explicitly request the whole exercise, complete all three together.

Save requested reports under local/ using predictable folders: exercise-1/,
exercise-2/, exercise-3/, kuali/ and workday/. Use report.md for the main report
and descriptive names for supporting files. Create folders as needed, open the
main report in the app when available, and give a short chat summary with its
link. Keep source data and supplied worked answers unchanged. Explicit requests
for chat-only output or no file writes override this default.
