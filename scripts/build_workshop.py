"""Build the deterministic, shareable workshop archive from an explicit allowlist."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "dist" / "faculty-ai-workshop.zip"
ZIP_TIMESTAMP = (2026, 10, 16, 10, 0, 0)

# Keep this list explicit so local browser state, credentials, and intermediate
# presentation files cannot enter the shareable archive accidentally.
WORKSHOP_FILES = (
    ".agents/plugins/marketplace.json",
    "README.md",
    "answers/kuali.md",
    "answers/ls-1-outreach.md",
    "answers/ls-2-teaching.md",
    "answers/ls-3-administration.md",
    "answers/ls-4-ta-follow-up.md",
    "answers/workday.md",
    "data/approved_demo_changes.csv",
    "data/assessment_results.csv",
    "data/assignments.csv",
    "data/demo_ta_hours.csv",
    "data/diagnostic_checks.csv",
    "data/diagnostic_responses.csv",
    "data/expected_concept_summary.csv",
    "data/expected_student_summary.csv",
    "data/kuali/00_research_profile_intake.md",
    "data/kuali/00_synthetic_faculty_direction.md",
    "data/kuali/01_synthetic_constraints.md",
    "data/kuali/02_dated_backup_nsf_eccs_2026-08-26.md",
    "data/kuali/03_deliberately_flawed_shortlist.md",
    "data/kuali/04_concept_note_template.md",
    "data/kuali/05_proposal_state.md",
    "data/kuali/06_budget_workbook_summary.csv",
    "data/kuali/07_budget_justification_excerpt.md",
    "data/kuali/08_kuali_record_snapshot.md",
    "data/question_map.csv",
    "data/question_results.csv",
    "data/students.csv",
    "data/workday/01_finance_overview.csv",
    "data/workday/01_finance_overview_README.md",
    "data/workday/02_inbox_snapshot.md",
    "facilitator/MAINTAINING.md",
    "facilitator/PILOT_CHECKLIST.md",
    "facilitator/RUN_OF_SHOW.md",
    "manifest.json",
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
    "plugins/byu-faculty-integrations/skills/byu-learning-suite/SKILL.md",
    "plugins/byu-faculty-integrations/skills/byu-learning-suite/agents/openai.yaml",
    "plugins/byu-faculty-integrations/skills/byu-learning-suite/references/course-planning.md",
    "plugins/byu-faculty-integrations/skills/byu-learning-suite/references/course-setup.md",
    "plugins/byu-faculty-integrations/skills/byu-learning-suite/references/student-data.md",
    "plugins/byu-faculty-integrations/skills/byu-workday/SKILL.md",
    "plugins/byu-faculty-integrations/skills/byu-workday/agents/openai.yaml",
    "plugins/byu-faculty-integrations/skills/byu-workday/references/finance-reports.md",
    "plugins/byu-faculty-integrations/skills/byu-workday/references/inbox-tasks.md",
    "scripts/build_demo.py",
    "scripts/build_workshop.py",
    "scripts/check_answers.py",
    "scripts/check_integrations.py",
    "tests/cli_tools.test.mjs",
    "tutorial/1_SETUP.md",
    "tutorial/2_LEARNING_SUITE.md",
    "tutorial/3_KUALI.md",
    "tutorial/4_WORKDAY.md",
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

    ARCHIVE.parent.mkdir(exist_ok=True)
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
