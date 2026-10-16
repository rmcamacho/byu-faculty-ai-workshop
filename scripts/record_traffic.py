"""Append GitHub traffic for this repository to CSV files that outlive GitHub's 14-day window.

Run daily (see .github/workflows/traffic.yml). Daily clone and view counts are merged
by date, so overlapping windows never double-count; the newest fetch of a day wins
because today's count is partial until tomorrow. Referrers and popular paths are
14-day aggregates, so each run stores them as a dated snapshot. Needs a token that
can read repository administration data, in TRAFFIC_TOKEN or GH_TOKEN.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import urllib.request

API = "https://api.github.com"


def get(repo: str, route: str, token: str):
    request = urllib.request.Request(
        f"{API}/repos/{repo}{route}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "record-traffic",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write_rows(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def merge_daily(path: Path, entries: list[dict]) -> None:
    """Merge per-day counts by date; a newer fetch replaces an older one."""
    by_date = {row["date"]: row for row in read_rows(path)}
    for entry in entries:
        date = entry["timestamp"][:10]
        by_date[date] = {"date": date, "count": entry["count"], "uniques": entry["uniques"]}
    write_rows(path, ["date", "count", "uniques"], [by_date[d] for d in sorted(by_date)])


def replace_snapshot(path: Path, key: str, today: str, entries: list[dict]) -> None:
    """Store a dated copy of a 14-day aggregate, replacing any earlier run today."""
    rows = [row for row in read_rows(path) if row["snapshot_date"] != today]
    rows += [
        {"snapshot_date": today, key: entry[key], "count": entry["count"], "uniques": entry["uniques"]}
        for entry in entries
    ]
    write_rows(path, ["snapshot_date", key, "count", "uniques"], rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"), help="owner/name")
    parser.add_argument("--out", type=Path, required=True, help="directory for the CSV files")
    args = parser.parse_args()
    token = os.environ.get("TRAFFIC_TOKEN") or os.environ.get("GH_TOKEN")
    if not args.repo or not token:
        raise SystemExit("Set --repo (or GITHUB_REPOSITORY) and TRAFFIC_TOKEN (or GH_TOKEN).")

    today = datetime.now(timezone.utc).date().isoformat()
    clones = get(args.repo, "/traffic/clones?per=day", token)
    views = get(args.repo, "/traffic/views?per=day", token)
    referrers = get(args.repo, "/traffic/popular/referrers", token)
    paths = get(args.repo, "/traffic/popular/paths", token)
    repo = get(args.repo, "", token)

    merge_daily(args.out / "clones.csv", clones["clones"])
    merge_daily(args.out / "views.csv", views["views"])
    replace_snapshot(args.out / "referrers.csv", "referrer", today, referrers)
    replace_snapshot(args.out / "paths.csv", "path", today, paths)

    totals = [row for row in read_rows(args.out / "repository.csv") if row["date"] != today]
    totals.append({
        "date": today,
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "watchers": repo["subscribers_count"],
    })
    write_rows(args.out / "repository.csv", ["date", "stars", "forks", "watchers"], totals)

    print(json.dumps({
        "repo": args.repo,
        "snapshot": today,
        "clones_14d": clones["count"],
        "views_14d": views["count"],
        "referrers": len(referrers),
    }))


if __name__ == "__main__":
    main()
