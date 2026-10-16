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

    subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_answers.py")],
        cwd=ROOT,
        check=True,
    )

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
