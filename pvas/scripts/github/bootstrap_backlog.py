#!/usr/bin/env python3
"""Create the PVAS labels, milestones, issues and GitHub Project from backlog/backlog.json.

THIS SCRIPT ACTS ON GITHUB. Run it once, by one team member, after the repository exists.

Prerequisites
  1. GitHub CLI installed:            https://cli.github.com
  2. Logged in:                       gh auth login
  3. Project scope granted:           gh auth refresh -s project
  4. Repository already created and pushed (see docs/milestone-1/github-setup-guide.md)

Usage
  python scripts/github/bootstrap_backlog.py --repo OWNER/REPO --dry-run   # print only
  python scripts/github/bootstrap_backlog.py --repo OWNER/REPO             # do it

Safe to re-run: labels are upserted, existing milestones/issues (matched by title) are skipped,
and an existing project with the same title is reused.

What it does NOT do (GitHub CLI cannot): Iteration field, Status column names, board/table
views, built-in workflows. Do those in the web UI - see docs/milestone-1/05-github-projects-config.md.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

BACKLOG = Path(__file__).resolve().parents[2] / "backlog" / "backlog.json"
PROJECT_TITLE = "PVAS - Product Backlog"


def gh(args, dry, capture=True):
    """Run `gh`; in dry-run mode only print the command."""
    printable = "gh " + " ".join(a if " " not in a and "\n" not in a else repr(a[:60]) for a in args)
    if dry:
        print("[dry-run]", printable)
        return ""
    res = subprocess.run(["gh"] + args, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        sys.exit(f"\nFAILED: {printable}\n{res.stderr.strip()}")
    return res.stdout.strip() if capture else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True, help="OWNER/REPO, e.g. my-team/pvas")
    ap.add_argument("--project-owner", help="user/org that owns the Project (default: repo owner)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    dry, repo = a.dry_run, a.repo
    owner = a.project_owner or repo.split("/")[0]
    data = json.loads(BACKLOG.read_text(encoding="utf-8"))

    # 1. labels (upsert)
    print("\n== Labels ==")
    for l in data["labels"]:
        gh(["label", "create", l["name"], "--repo", repo, "--color", l["color"],
            "--description", l["description"], "--force"], dry)

    # 2. milestones (skip existing)
    print("\n== Milestones ==")
    existing = set()
    if not dry:
        out = gh(["api", f"repos/{repo}/milestones?state=all&per_page=100", "--jq", ".[].title"], dry)
        existing = set(out.splitlines())
    for m in data["milestones"]:
        if m in existing:
            print("exists:", m)
            continue
        gh(["api", f"repos/{repo}/milestones", "-f", f"title={m}"], dry)

    # 3. issues (skip existing titles)
    print("\n== Issues ==")
    have = {}
    if not dry:
        out = gh(["issue", "list", "--repo", repo, "--state", "all", "--limit", "500",
                  "--json", "title,url"], dry)
        have = {i["title"]: i["url"] for i in json.loads(out or "[]")}
    urls = {}
    for i in data["issues"]:
        if i["title"] in have:
            print("exists:", i["title"])
            urls[i["id"]] = have[i["title"]]
            continue
        args = ["issue", "create", "--repo", repo, "--title", i["title"], "--body", i["body"],
                "--milestone", i["milestone"]]
        for lab in i["labels"]:
            args += ["--label", lab]
        urls[i["id"]] = gh(args, dry) or f"https://github.com/{repo}/issues/<{i['id']}>"
        print("created:", i["title"])

    # 4. project
    print("\n== Project ==")
    number = None
    if not dry:
        plist = json.loads(gh(["project", "list", "--owner", owner, "--format", "json", "--limit", "100"], dry) or "{}")
        for p in plist.get("projects", []):
            if p["title"] == PROJECT_TITLE:
                number = p["number"]
                print("reusing project", number)
    if number is None:
        out = gh(["project", "create", "--owner", owner, "--title", PROJECT_TITLE, "--format", "json"], dry)
        number = json.loads(out)["number"] if out else "<N>"
    gh(["project", "link", str(number), "--owner", owner, "--repo", repo], dry)

    # Story Points number field
    fields = {}
    if not dry:
        fl = json.loads(gh(["project", "field-list", str(number), "--owner", owner, "--format", "json"], dry))
        fields = {f["name"]: f["id"] for f in fl["fields"]}
    if "Story Points" not in fields:
        gh(["project", "field-create", str(number), "--owner", owner, "--name", "Story Points",
            "--data-type", "NUMBER"], dry)
        if not dry:
            fl = json.loads(gh(["project", "field-list", str(number), "--owner", owner, "--format", "json"], dry))
            fields = {f["name"]: f["id"] for f in fl["fields"]}
    project_id = ""
    if not dry:
        project_id = json.loads(gh(["project", "view", str(number), "--owner", owner, "--format", "json"], dry))["id"]

    # 5. add issues to project, set Story Points
    print("\n== Adding issues to project ==")
    for i in data["issues"]:
        out = gh(["project", "item-add", str(number), "--owner", owner, "--url", urls[i["id"]],
                  "--format", "json"], dry)
        if i["sp"] is not None:
            item_id = json.loads(out)["id"] if out else "<item>"
            gh(["project", "item-edit", "--id", item_id, "--project-id", project_id or "<project>",
                "--field-id", fields.get("Story Points", "<field>"), "--number", str(i["sp"])], dry)
        print("added:", i["id"], f"(SP {i['sp']})" if i["sp"] is not None else "")

    print("\nDone. Remaining MANUAL steps in the web UI: Iteration field, Status columns, views, workflows.")
    print("See docs/milestone-1/05-github-projects-config.md")


if __name__ == "__main__":
    main()
