# BYU Kuali and Workday for Codex

This portable Codex plugin adds two workflows to the faculty workshop:

- **BYU Kuali (`$byu-kuali`):** organize proposal development, keep narrative, budget, and attachments synchronized, and carefully update a Kuali record with preview, confirmation, and verification.
- **BYU Workday (`$byu-workday`):** read research-finance reports and inbox tasks and explain them. It is read-only: it never approves, sends back, submits, certifies, or creates transactions.

The Kuali skill and the browser scripts come from the ECEN faculty tutorial's BYU Faculty Productivity plugin (version 0.3.0, revision `e77f6b0`). The Workday skill is new and follows the same safety pattern with stricter read-only limits.

The plugin contains no proposal content, account numbers, balances, student or employee records, passwords, cookies, or browser profiles. Each faculty member supplies their own authenticated browser session. BYU work should use the CES ChatGPT Edu identity and follow the current BYU ChatGPT Edu Data Guidelines.

## Relationship to the Learning Suite Plugin

Learning Suite work in this workshop uses the separately installed BYU Faculty Productivity plugin. This plugin uses the same dedicated Chrome profile location and port, so one dedicated browser window serves Learning Suite, Kuali, and Workday. The Kuali skill is named `byu-kuali` so it does not collide with that plugin's `byu-kuali-proposals` skill.

## Safety Pattern

1. inspect the current state;
2. create a human-readable plan, summary, or diff;
3. verify the target and resolve material ambiguity;
4. preview the exact change (Kuali only);
5. obtain confirmation immediately before the live write;
6. apply a small change set;
7. verify that it persisted.

Certification, routing, approval, and submission in Kuali, and every approval or transaction in Workday, remain with the faculty member and authorized institutional staff.

## Requirements

- Codex CLI with local-file access, including Codex CLI in VS Code's integrated terminal.
- Node.js 22 or newer and Google Chrome for live browser work.
- Your own access to the relevant Kuali proposal or Workday reports.

## Example Prompts

- "Use `$byu-kuali` to read this solicitation and build a compliance matrix and proposal workspace."
- "Use `$byu-kuali` to compare my local upload files and budget with this Kuali record. Preview any needed replacements but do not apply them yet."
- "Use `$byu-workday` to run my budget-versus-actuals overview with its current defaults, then explain which balances have restrictions or end dates I should watch."
- "Use `$byu-workday` to list my inbox tasks by due date. Do not open any task or approve anything."

## Tests

From the repository root: `node --test tests/cli_tools.test.mjs`.
