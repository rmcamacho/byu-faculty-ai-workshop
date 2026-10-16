# Beyond Learning Suite: Kuali and Workday

The same workflow from the Learning Suite workshop — inspect, preview, confirm, apply, verify — applied to two more BYU systems faculty use every week.

| | Kuali | Workday |
| --- | --- | --- |
| Skill | `$byu-kuali` | `$byu-workday` |
| What it helps with | Funding search, proposal workspaces, keeping narrative, budget and attachments in sync with the Kuali record | Reading research-finance reports and inbox tasks, and preparing decisions |
| Live writes | Small confirmed edits and attachment replacements | None: read-only |
| Always yours | Certification, routing, approval, submission | Approvals, send-backs, certifications, expense reports, requisitions |
| Tutorial | [kuali/TUTORIAL.md](kuali/TUTORIAL.md) | [workday/TUTORIAL.md](workday/TUTORIAL.md) |

Start with [SETUP.md](SETUP.md). The plugin lives in [plugins/byu-faculty-integrations](../plugins/byu-faculty-integrations/README.md).

All exercise files are synthetic: the faculty member, proposal, worktags, amounts, people, and tasks are invented. The Kuali funding-search exercise and the plugin's Kuali skill and browser scripts are borrowed from the ECEN faculty AI tutorial (BYU Faculty Productivity plugin 0.3.0).

Run `python3 scripts/check_integrations.py` from the repository root to verify the synthetic arithmetic, skill files, and links. It never connects to Kuali or Workday.
