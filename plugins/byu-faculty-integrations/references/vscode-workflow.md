# VS Code Workflow

When the user works in VS Code, distinguish the Codex IDE sidebar from Codex CLI in the integrated terminal.

- The IDE extension does not currently support plugins, so do not claim the department skills are loaded there.
- The integrated terminal can run Codex CLI, which supports this plugin. Treat that as ordinary CLI mode.
- Follow [CLI Browser Mode](cli-browser.md) for the dedicated Chrome session.
- For prompt-driven interactive work, follow [Adaptive Browser Task Scripts](browser-task-scripts.md).

Accept natural-language outcome prompts. For a request such as changing one quiz date in Learning Suite or replacing one Kuali attachment:

1. identify the visible course by title, term, section, and origin, or the proposal by number, title, principal investigator, sponsor, and origin;
2. identify the exact item, field, or attachment and its current value;
3. present the current and proposed values and any related effects;
4. obtain explicit confirmation immediately before the write;
5. apply only the approved change through the authenticated browser-task runner;
6. reopen or reread the item and verify persistence.

Use the shared browser-task runner rather than looking for a one-off command named after the user's request. Generate the smallest task-specific script in the workspace, default to preview, and use `--apply` only after explicit confirmation. Do not bypass the runner's safeguards with cookies, storage, direct network calls, or the user's normal Chrome profile.

Workday work is read-only. Use preview-mode task scripts to read rendered content; the only permitted Workday `--apply` run executes a report after its parameters are confirmed.
