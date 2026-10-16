# BYU Learning Suite, Kuali and Workday for Codex

This portable Codex plugin provides three workflows that share one browser connection and one safety pattern:

- **BYU Learning Suite (`$byu-learning-suite`):** inspect, plan, copy, configure, and safely update a course through an authenticated browser.
- **BYU Kuali (`$byu-kuali`):** organize proposal development, keep narrative, budget, and attachments synchronized, and carefully update a Kuali record with preview, confirmation, and verification.
- **BYU Workday (`$byu-workday`):** read research-finance reports and inbox tasks and explain them. It is read-only: it never approves, sends back, submits, certifies, or creates transactions.

The Learning Suite skill and the browser scripts are unchanged from the ECEN faculty tutorial's BYU Faculty Productivity plugin (version 0.3.0, revision `e77f6b0`). The Kuali skill comes from the same plugin with two added rules. The Workday skill is new and follows the same pattern with stricter read-only limits.

The plugin contains no course IDs, student records, proposal content, account numbers, balances, employee records, passwords, cookies, or browser profiles. Each faculty member supplies their own authenticated browser session. BYU work should use the CES ChatGPT Edu identity and follow the current BYU ChatGPT Edu Data Guidelines; identifiable student data must be de-identified unless explicitly approved by the institutional AI Executive Committee.

Install it with [tutorial/1_SETUP.md](../../tutorial/1_SETUP.md). It supersedes BYU Faculty Productivity 0.3.0, so don't enable both plugins at once.

## Safety Pattern

1. inspect the current state;
2. create a human-readable plan, summary, or diff;
3. verify the target and resolve material ambiguity;
4. preview the exact change (Learning Suite and Kuali only);
5. obtain confirmation immediately before the live write;
6. apply a small change set;
7. verify that it persisted.

Grading judgments and student messaging in Learning Suite, certification, routing, approval, and submission in Kuali, and every approval or transaction in Workday remain with the faculty member and authorized institutional staff.

## Requirements

- The ChatGPT desktop app with its Chrome plugin and extension, which controls the user's own signed-in Chrome; or
- Codex CLI (including in VS Code's integrated terminal) with Node.js 22 or newer and Google Chrome, which uses a dedicated Chrome profile and the guarded task runner in `scripts/`. The Codex IDE sidebar does not currently load plugins.
- Your own access to the relevant course, proposal, or Workday reports.

## Example Prompts

- "Use `$byu-learning-suite`. In this course, change Quiz 5's due date to October 14, 2026. Show the current and proposed values, wait for my confirmation before saving, and then verify the saved date."
- "Use `$byu-kuali` to compare my local upload files and budget with this Kuali record. Preview any needed replacements but do not apply them yet."
- "Use `$byu-workday` to run my budget-versus-actuals overview with its current defaults, then explain which balances have restrictions or end dates I should watch."
- "Use `$byu-workday` to list my inbox tasks by due date. Do not open any task or approve anything."

## Tests

From the repository root: `node --test tests/cli_tools.test.mjs` and `python3 scripts/check_integrations.py`.
