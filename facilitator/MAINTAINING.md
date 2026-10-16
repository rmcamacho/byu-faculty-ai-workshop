# Maintaining the Workshop

## Checks

```text
python3 scripts/build_workshop.py
node --test tests/cli_tools.test.mjs
```

`build_workshop.py` runs both answer checkers (`scripts/check_answers.py` for Learning Suite, `scripts/check_integrations.py` for Kuali, Workday, the plugin's skills and every Markdown link), then writes `dist/faculty-ai-workshop.zip` from an explicit allowlist. That ZIP is the attachment for the LS course's Start Here page; participants otherwise download the repository from GitHub. Add any new shareable file to the allowlist, inspect the archive, and test a clean extraction before uploading it. Nothing here connects to Learning Suite, Kuali or Workday.

`python3 scripts/build_demo.py` deterministically regenerates the Learning Suite CSVs, expected summaries and `manifest.json` (24 students, 192 assessment records, 552 question-part records), with assertions on joins, scaling and denominators.

## Provenance

- **Learning Suite course:** the development course *Agentic AI Faculty Demo - Synthetic* contains copies of five homework sets, Unit Quizzes 1–3, the syllabus, Lectures and Extra Course Help from Ryan's Fall 2026 combined 240/301 course. Course and exam copying were enabled and verified on October 11, 2026. See the [BYU course-setup documentation](https://softwaresupport.byu.edu/learning-suite/instructor/setup-and-basics/course-setup) (Copy Course Information and Development Course).
- **Plugin:** `plugins/byu-faculty-integrations`. Its Learning Suite skill and browser scripts are byte-identical to the ECEN tutorial's BYU Faculty Productivity plugin 0.3.0 (github.com/rmcamacho/byu-faculty-productivity, revision `e77f6b0`). The Kuali skill comes from the same plugin, renamed `byu-kuali` with two added rules. The Workday skill is new and read-only.
- **Kuali exercise:** files `00`–`04` in `data/kuali/` and Part A of `answers/kuali.md` are adapted from the ECEN tutorial's grant-development exercise. Files `05`–`08` are new.
- **Copyright:** course questions and slide decks are not in this repository. Do not redistribute them without permission.

## Validation Status

- Tested: answer checkers; the nine browser-helper tests on Linux with Node 24; plugin installation from a clean ZIP extraction with Codex CLI 0.153 on Linux; the course copy settings on the owner account.
- Not yet tested: a participant's Mac or Windows install and browser launch; a second faculty account copying the course end to end; that account's Google Slides access; the Kuali and Workday skills against live pages from a participant's machine. Use [PILOT_CHECKLIST.md](PILOT_CHECKLIST.md) before presenting the setup as fully tested.
