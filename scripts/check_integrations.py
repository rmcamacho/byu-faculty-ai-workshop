"""Check the Kuali and Workday integration materials; never contacts Kuali or Workday."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/byu-faculty-integrations"
KUALI = ROOT / "data/kuali"
WORKDAY = ROOT / "data/workday"
ANSWERS = ROOT / "answers"
SKILLS = ("byu-learning-suite", "byu-kuali", "byu-workday")


def money(value: str) -> int:
    return int(value.replace(",", ""))


def check_budget() -> None:
    rows = list(csv.DictReader((KUALI / "06_budget_workbook_summary.csv").open()))
    body, total = rows[:-1], rows[-1]
    assert total["category"] == "Total direct costs"
    years = ("year_1", "year_2", "year_3")
    for row in rows:
        assert sum(money(row[y]) for y in years) == money(row["total"]), row["category"]
    for column in (*years, "total"):
        assert sum(money(row[column]) for row in body) == money(total[column]), column

    # The Kuali read-out differs from the workbook only in Year 2 travel.
    snapshot = (KUALI / "08_kuali_record_snapshot.md").read_text()
    kuali = {}
    for line in snapshot.splitlines():
        cells = [cell.strip().strip("*") for cell in line.strip("|").split("|")]
        if len(cells) == 4 and re.fullmatch(r"[\d,]+", cells[1]):
            kuali[cells[0]] = [money(cell) for cell in cells[1:]]
    totals = kuali.pop("Total direct costs")
    for index in range(3):
        assert sum(values[index] for values in kuali.values()) == totals[index]
    workbook = [money(total[y]) for y in years]
    assert [k - w for k, w in zip(totals, workbook)] == [0, 2000, 0]
    assert kuali["Travel"][1] == 6000
    assert f"Cumulative total direct costs shown: {sum(totals):,}." in snapshot

    answers = (ANSWERS / "kuali.md").read_text()
    for figure in ("$97,500", "$99,385", "$69,015", "$265,900", "$267,900", "$31,827"):
        assert figure in answers, figure


def check_finance() -> None:
    rows = list(csv.DictReader((WORKDAY / "01_finance_overview.csv").open()))
    body, total = rows[:-1], rows[-1]
    assert total["worktag"] == "Total"
    columns = ("budget", "actuals", "encumbrances", "remaining_balance")
    for row in body:
        assert money(row["budget"]) - money(row["actuals"]) - money(row["encumbrances"]) == money(
            row["remaining_balance"]
        ), row["worktag"]
    for column in columns:
        assert sum(money(row[column]) for row in body) == money(total[column]), column

    inbox = (WORKDAY / "02_inbox_snapshot.md").read_text()
    lines = [money(amount) for amount in re.findall(r"^  - .*: \$([\d,]+)", inbox, re.MULTILINE)]
    assert lines == [650, 1240, 84]
    assert f"Total: ${sum(lines):,}" in inbox

    answers = (ANSWERS / "workday.md").read_text()
    for figure in ("$490,000", "$336,845", "$14,800", "$138,355", "$109,390", "$2,140", "$1,325", "$166"):
        assert figure in answers, figure


def check_skills() -> None:
    manifest = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    entry = marketplace["plugins"][0]
    assert entry["name"] == manifest["name"] == PLUGIN.name
    assert (ROOT / ".agents/plugins" / ".." / ".." / entry["source"]["path"]).resolve() == PLUGIN.resolve()
    for name in SKILLS:
        text = (PLUGIN / "skills" / name / "SKILL.md").read_text()
        header = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        assert header, name
        assert re.search(rf"^name: {name}$", header.group(1), re.MULTILINE), name
        assert re.search(r"^description: \S", header.group(1), re.MULTILINE), name


def check_links_and_leaks() -> None:
    # Personal paths, live course IDs and private Workday provenance must not
    # reach the plugin or the Kuali/Workday materials.
    forbidden = ("/home/", "/Users/", "cid-", "Burr", "23748$22")
    scanned = [PLUGIN, KUALI, WORKDAY, ANSWERS / "kuali.md", ANSWERS / "workday.md"]
    for base in scanned:
        for path in [base] if base.is_file() else [p for p in base.rglob("*") if p.is_file()]:
            text = path.read_text()
            for token in forbidden:
                assert token not in text, f"{token!r} in {path.relative_to(ROOT)}"

    # Every relative Markdown link in the repository must resolve.
    for path in ROOT.rglob("*.md"):
        if {".git", "local", "dist"} & set(path.relative_to(ROOT).parts):
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" in target or target.startswith("#"):
                continue
            assert (path.parent / target.split("#", 1)[0]).exists(), f"{path.relative_to(ROOT)} -> {target}"


def main() -> None:
    check_budget()
    check_finance()
    check_skills()
    check_links_and_leaks()
    print(json.dumps({"integrations": "kuali, workday", "checks": "passed"}, indent=2))


if __name__ == "__main__":
    main()
