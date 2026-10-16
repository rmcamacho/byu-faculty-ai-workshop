"""Build the deterministic, shareable workshop archive from an explicit allowlist."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "faculty-ls-workshop-v2.zip"
ZIP_TIMESTAMP = (2026, 10, 16, 10, 0, 0)

# Keep this list explicit so local browser state, credentials, and intermediate
# presentation files cannot enter the shareable archive accidentally.
WORKSHOP_FILES = (
    "README.md",
    "manifest.json",
    "build_demo.py",
    "data/approved_demo_changes.csv",
    "data/assessment_results.csv",
    "data/assignments.csv",
    "data/demo_ta_hours.csv",
    "data/expected_concept_summary.csv",
    "data/expected_student_summary.csv",
    "data/question_map.csv",
    "data/question_results.csv",
    "data/students.csv",
    "examples/01_OUTREACH.md",
    "examples/02_TEACHING.md",
    "examples/03_ADMINISTRATION.md",
    "examples/04_ASSISTANT_BONUS.md",
    "scripts/build_workshop.py",
    "scripts/check_answers.py",
    "tutorial/COPY_COURSE.md",
    "tutorial/PARTICIPANT_PILOT.md",
    "tutorial/PRESENTER_RUN_OF_SHOW.md",
    "tutorial/SETUP.md",
    "tutorial/START_HERE.md",
    ".agents/plugins/marketplace.json",
    "integrations/README.md",
    "integrations/SETUP.md",
    "integrations/kuali/ANSWERS.md",
    "integrations/kuali/TUTORIAL.md",
    "integrations/kuali/workspace/00_research_profile_intake.md",
    "integrations/kuali/workspace/00_synthetic_faculty_direction.md",
    "integrations/kuali/workspace/01_synthetic_constraints.md",
    "integrations/kuali/workspace/02_dated_backup_nsf_eccs_2026-08-26.md",
    "integrations/kuali/workspace/03_deliberately_flawed_shortlist.md",
    "integrations/kuali/workspace/04_concept_note_template.md",
    "integrations/kuali/workspace/05_proposal_state.md",
    "integrations/kuali/workspace/06_budget_workbook_summary.csv",
    "integrations/kuali/workspace/07_budget_justification_excerpt.md",
    "integrations/kuali/workspace/08_kuali_record_snapshot.md",
    "integrations/workday/ANSWERS.md",
    "integrations/workday/TUTORIAL.md",
    "integrations/workday/workspace/01_finance_overview.csv",
    "integrations/workday/workspace/01_finance_overview_README.md",
    "integrations/workday/workspace/02_inbox_snapshot.md",
    "plugins/byu-faculty-integrations/.codex-plugin/plugin.json",
    "plugins/byu-faculty-integrations/README.md",
    "plugins/byu-faculty-integrations/references/browser-task-scripts.md",
    "plugins/byu-faculty-integrations/references/cli-browser.md",
    "plugins/byu-faculty-integrations/references/vscode-workflow.md",
    "plugins/byu-faculty-integrations/scripts/browser_task_runner.mjs",
    "plugins/byu-faculty-integrations/scripts/chrome_cdp.mjs",
    "plugins/byu-faculty-integrations/scripts/chrome_session.mjs",
    "plugins/byu-faculty-integrations/skills/byu-kuali/SKILL.md",
    "plugins/byu-faculty-integrations/skills/byu-kuali/agents/openai.yaml",
    "plugins/byu-faculty-integrations/skills/byu-kuali/references/kuali-live-updates.md",
    "plugins/byu-faculty-integrations/skills/byu-kuali/references/proposal-workspace.md",
    "plugins/byu-faculty-integrations/skills/byu-workday/SKILL.md",
    "plugins/byu-faculty-integrations/skills/byu-workday/agents/openai.yaml",
    "plugins/byu-faculty-integrations/skills/byu-workday/references/finance-reports.md",
    "plugins/byu-faculty-integrations/skills/byu-workday/references/inbox-tasks.md",
    "scripts/check_integrations.py",
    "tests/cli_tools.test.mjs",
)


def archive_entry(relative_path: str) -> ZipInfo:
    info = ZipInfo(relative_path, ZIP_TIMESTAMP)
    info.compress_type = ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def main() -> None:
    missing = [name for name in WORKSHOP_FILES if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit(f"Missing workshop files: {', '.join(missing)}")

    manifest = json.loads((ROOT / "manifest.json").read_text())
    if manifest.get("synthetic") is not True:
        raise SystemExit("Refusing to package a workshop not marked synthetic")

    for check in ("scripts/check_answers.py", "scripts/check_integrations.py"):
        subprocess.run([sys.executable, str(ROOT / check)], cwd=ROOT, check=True)

    with ZipFile(ARCHIVE, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for relative_path in WORKSHOP_FILES:
            contents = (ROOT / relative_path).read_bytes()
            archive.writestr(
                archive_entry(relative_path),
                contents,
                compress_type=ZIP_DEFLATED,
                compresslevel=9,
            )

    print(
        json.dumps(
            {
                "archive": str(ARCHIVE),
                "files": len(WORKSHOP_FILES),
                "sha256": sha256(ARCHIVE.read_bytes()).hexdigest(),
                "checks": "passed",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
