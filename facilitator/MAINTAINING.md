# Maintaining the Workshop

## Checks

```text
python3 scripts/build_workshop.py
node --test tests/cli_tools.test.mjs
```

`build_workshop.py` runs both answer checkers (`scripts/check_answers.py` for Learning Suite, `scripts/check_integrations.py` for Kuali, Workday, the plugin's skills and every Markdown link), then writes `dist/faculty-ai-workshop.zip` from an explicit allowlist. That ZIP is the attachment for the LS course's Start Here page; participants otherwise download the repository from GitHub. Add any new shareable file to the allowlist, inspect the archive, and test a clean extraction before uploading it. Nothing here connects to Learning Suite, Kuali or Workday.

`python3 scripts/build_demo.py` deterministically regenerates the Learning Suite CSVs, expected summaries and `manifest.json` (24 students, 192 assessment records, 552 question-part records, plus three original diagnostic checks and 72 diagnostic-response records), with assertions on joins, scaling and denominators. Diagnostic responses are original synthetic follow-up work, separate from the copied LS assessments, and do not affect grades.

## Provenance

- **Learning Suite course:** the development course *Agentic AI Faculty Demo - Synthetic* contains copies of five homework sets, Unit Quizzes 1–3, the syllabus, Lectures and Extra Course Help from Ryan's Fall 2026 combined 240/301 course. Course and exam copying were enabled and verified on October 11, 2026. See the [BYU course-setup documentation](https://softwaresupport.byu.edu/learning-suite/instructor/setup-and-basics/course-setup) (Copy Course Information and Development Course).
- **Plugin:** `plugins/byu-faculty-integrations`. Its browser scripts are byte-identical, and its Learning Suite skill identical apart from one added line choosing the desktop app's built-in browser, to the ECEN tutorial's BYU Faculty Productivity plugin 0.3.0 (github.com/rmcamacho/byu-faculty-productivity, revision `e77f6b0`). The Kuali skill comes from the same plugin, renamed `byu-kuali` with two added rules. The Workday skill is new and read-only.
- **Kuali exercise:** files `00`–`04` in `data/kuali/` and Part A of `answers/kuali.md` are adapted from the ECEN tutorial's grant-development exercise. Files `05`–`08` are new.
- **Copyright:** course questions and slide decks are not in this repository. Do not redistribute them without permission.

## Validation Status

- Tested: answer checkers; the nine browser-helper tests on Linux with Node 24; plugin installation from a clean ZIP extraction with Codex CLI 0.153 on Linux; the course copy settings on the owner account.
- Tested October 16, 2026 by the owner: the ChatGPT desktop app path. The repository marketplace appeared in Plugins with the workshop folder open, without the CLI, and the workflow ran in the app's built-in browser (Codex first tried an external Chrome until told otherwise).
- Not yet tested: a participant's Mac or Windows install and browser launch; a second faculty account copying the course end to end; that account's Google Slides access; the Kuali and Workday skills against live pages from a participant's machine. Use [PILOT_CHECKLIST.md](PILOT_CHECKLIST.md) before presenting the setup as fully tested.

## Traffic History

GitHub keeps only 14 days of clone and view counts. The **Record traffic** workflow (`.github/workflows/traffic.yml`) runs `scripts/record_traffic.py` daily and commits the results to the `traffic-data` branch, so the history outlives that window:

- `traffic/clones.csv` and `traffic/views.csv`: one row per day (`count` = total, `uniques` = distinct visitors). The newest fetch of a day wins, because the current day is partial.
- `traffic/referrers.csv` and `traffic/paths.csv`: dated snapshots of GitHub's 14-day top referring sites and most-viewed pages.
- `traffic/repository.csv`: daily stars, forks and watchers.

Read it on GitHub (switch the branch selector to `traffic-data`) or locally with `git fetch origin traffic-data` and `git show origin/traffic-data:traffic/views.csv`. The branch is public like the rest of the repository; it holds only aggregate counts and referring sites.

**Limits.** "Download ZIP" clicks are not counted anywhere by GitHub. Clones include automated and maintainer clones. Days before the workflow's first run are recoverable only while they are still inside GitHub's 14-day window.

**One-time setup.** The workflow's built-in token cannot read traffic, so it uses a fine-grained personal access token:

1. On GitHub: **Settings > Developer settings > Personal access tokens > Fine-grained tokens > Generate new token**.
2. Name it (for example *byu-faculty-ai-workshop traffic*) and choose an expiration. Under **Repository access**, choose **Only select repositories** and pick `byu-faculty-ai-workshop`.
3. Under **Permissions > Repository permissions**, set **Administration** to **Read-only**. Nothing else is needed.
4. Generate the token and store it as the repository secret `TRAFFIC_TOKEN`, either under **Repository Settings > Secrets and variables > Actions > New repository secret**, or with `gh secret set TRAFFIC_TOKEN -R rmcamacho/byu-faculty-ai-workshop` (it prompts for the value, so the token never lands in a file or your shell history).
5. Open **Actions > Record traffic > Run workflow** once to confirm it works and to capture the current 14 days.

**Upkeep.** When the token expires, the daily run fails and GitHub emails you; create a new token and replace the secret. GitHub also disables scheduled workflows in public repositories after 60 days without repository activity, with an email warning first; re-enable it from the Actions tab.
