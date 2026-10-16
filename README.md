# Agentic AI for Faculty: Learning Suite, Kuali and Workday

A self-guided companion to the October 16, 2026 faculty lunch and learn. You will connect Codex to BYU systems and practice one safe workflow on realistic tasks: **inspect, preview, confirm, apply, verify**.

Repository: https://github.com/rmcamacho/byu-faculty-ai-workshop

## The Path

| Step | Guide | Time | Needs |
| --- | --- | --- | --- |
| 1 | [Set up Codex and the plugin](tutorial/1_SETUP.md) | 15 min, once | Codex, Node.js, Chrome |
| 2 | [Learning Suite](tutorial/2_LEARNING_SUITE.md): student outreach, teaching improvement, course changes | 30 min | Your own LS development copy |
| 3 | [Kuali](tutorial/3_KUALI.md): funding search and keeping a proposal in sync *(optional)* | 25 min | Nothing beyond step 1 |
| 4 | [Workday](tutorial/4_WORKDAY.md): research balances and inbox triage *(optional)* | 15 min | Nothing beyond step 1 |

Step 1 installs one Codex plugin with all three skills: `$byu-learning-suite`, `$byu-kuali` and `$byu-workday`. Every exercise runs from a single Codex session in this folder. Worked answers are in [answers/](answers/); try each prompt before opening them.

## Everything Here Is Synthetic

All students, results, diagnostic answers and working, TA hours, approvals, proposals, worktags, amounts, people and tasks are invented. They are not anonymized or derived from real records, and the `example.invalid` addresses cannot deliver mail. The original diagnostic follow-up questions illustrate specific reasoning mistakes and do not affect the eight-assessment grades. Their cohort patterns are deliberately planted. The Learning Suite teaching materials are real copies of course content, which stay in Learning Suite and Google Slides and are not included here.

Nothing in this repository authorizes a change to a live course, proposal or Workday record. Certification, routing and submission in Kuali, and every approval in Workday, stay with you.

## What's in the Folder

| Folder | Contents |
| --- | --- |
| [tutorial/](tutorial/) | The four guides above |
| [data/](data/) | Exercise inputs: Learning Suite CSVs and [manifest.json](manifest.json), plus [kuali/](data/kuali/) and [workday/](data/workday/) |
| [answers/](answers/) | Worked answers for every exercise |
| [plugins/](plugins/byu-faculty-integrations/README.md) | The Codex plugin installed in step 1 |
| [facilitator/](facilitator/) | Presenter run of show, pilot checklist and maintenance notes |
