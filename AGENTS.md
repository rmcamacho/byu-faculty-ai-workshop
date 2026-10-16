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
