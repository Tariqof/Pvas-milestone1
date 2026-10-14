# GitHub setup guide (Milestone 1)

Read this first. It separates three kinds of things:

| Tag | Meaning |
|---|---|
| 📄 **Generated** | Already in this folder. Nothing to do except commit it. |
| 🖥️ **You, locally** | Commands you run on your own computer. |
| 🌐 **You, on GitHub** | Things that exist only on github.com and cannot be committed as files. |

## What is already generated 📄

```
README.md  CONTRIBUTING.md  .gitignore
.github/PULL_REQUEST_TEMPLATE.md  .github/ISSUE_TEMPLATE/{user-story,task,bug,change-request}.yml
backlog/{backlog.json,backlog.csv,backlog.md}      28 items: F1-F19, D1-D6, C1-C3
scripts/github/bootstrap_backlog.py                 seeds labels, issues and the Project (Part C)
docs/milestone-1/…                                  charter, scope, lifecycle model, board config, your .docx
docs/milestone-2/  docs/milestone-3/  docs/process/
frontend/  (React + TypeScript + Vite skeleton)     backend/  ml/  data/  (placeholders)
```

## Part A. Create and push the repository

One member (suggest the project manager) does this once.

**A1. 🌐 Create an empty repository on GitHub.** github.com → New repository. Name e.g. `pvas`. Choose **no** README, **no** .gitignore, **no** licence (they already exist locally and would conflict). Visibility: public is simplest; see the note on branch protection below.

**A2. 🖥️ Initialise Git and make the first commit** (from the folder containing this README):

```bash
git init -b main
git config user.name  "Your Name"
git config user.email "you@example.com"
git add .
git status                       # check: no node_modules, no .env, no data files
git commit -m "chore: initial repository structure for Milestone 1"
```

**A3. 🖥️ Connect and push** (copy the URL from the empty repo page):

```bash
git remote add origin https://github.com/<owner>/pvas.git
git push -u origin main
```

**A4. 🖥️ First frontend install** (the lock file could not be generated when this skeleton was created, so create and commit it on a branch, which also practises the workflow):

```bash
git switch -c chore/frontend-lockfile
cd frontend && npm install && npm run build && cd ..
git add frontend/package-lock.json
git commit -m "chore: add frontend lockfile"
git push -u origin chore/frontend-lockfile      # then open a pull request on GitHub
```

If `npm run build` reports an error, fix it on that branch before merging.

## Part B. Repository settings 🌐

1. **Collaborators:** Settings → Collaborators → add the other three members. Add the instructor (Asst. Prof. Mintaş) with Read access if the course requires it.
2. **Branch protection on `main`:** Settings → Branches (or Rules → Rulesets) → add rule for `main`:
   - Require a pull request before merging, **1 approval**
   - Dismiss stale approvals when new commits are pushed
   - Do not allow bypassing the above
   - (From Sprint 3, add the CI check once F15 exists.)
   - *Note:* on a **private** repo under a free personal account GitHub may not offer branch protection. Use a public repo, or claim GitHub Student Developer Pack (Pro) first.
3. **Merge settings:** Settings → General → Pull Requests → allow squash merging; tick "Automatically delete head branches".

## Part C. Create labels, issues and the Project

### C1. 🖥️ Run the bootstrap script (creates most of it)

```bash
gh auth login                    # once
gh auth refresh -s project       # allow Projects access
python scripts/github/bootstrap_backlog.py --repo <owner>/pvas --dry-run   # preview
python scripts/github/bootstrap_backlog.py --repo <owner>/pvas              # run once
```

This acts on GitHub: it creates 14 labels, 4 milestones, 28 issues, a Project named `PVAS - Product Backlog`, links it to the repo, adds a numeric **Story Points** field, adds all issues and sets story points. It is safe to re-run (existing items are skipped). **Only one member should run it.** Organisation-owned repos may need `--project-owner <org>`.

*No GitHub CLI?* Do it by hand: create the labels from `backlog/backlog.json`, then create issues from `backlog/backlog.csv`/the issue bodies in the JSON, then continue with C2.

### C2. 🌐 Finish the Project in the web UI (the script cannot do these)

Open the Project (repo → Projects tab).

1. **Iteration field:** Project → ⋯ → Settings → **New field** → name `Iteration`, type **Iteration**. Set duration **2 weeks**, start date **19 Oct 2026**. GitHub generates iterations; make sure there are four and rename them `Sprint 0`, `Sprint 1`, `Sprint 2`, `Sprint 3` (19 Oct, 2 Nov, 16 Nov, 30 Nov).
2. **Status columns:** Settings → Status → edit options to exactly: `Backlog`, `Sprint Ready`, `In Progress`, `In Review`, `Done`. Set the description of In Review to "pull request open".
3. **Views:**
   - *Board* view grouped by Status (rename it "Sprint board"), filter `iteration:@current` if you like.
   - *Table* view ("Backlog") showing Title, Labels, Story Points, Iteration, Status, Milestone; sort by priority label.
   - Optional *Roadmap* view grouped by Iteration.
4. **Assign sprints:** in the Table view set the Iteration for each item using the proposal in `backlog/backlog.md` (Sprint 0 = F6, F9, F11 + chores; and so on). Put items that will be worked in Sprint 0 in `Sprint Ready`; everything else stays in `Backlog`.
5. **Workflows:** Project → ⋯ → Workflows → enable *Item closed → Status Done*, *Pull request merged → Status Done*, *Item added to project → Status Backlog* (names may differ slightly in the UI). Optionally enable *Auto-add to project* for issues in this repo.
6. **Milestone due dates:** Issues → Milestones → edit each of the four and set its due date (Week 4 / 7 / 12 / 13 dates from your course calendar).
7. **Evidence:** take the screenshots listed in `docs/milestone-1/05-github-projects-config.md`, save them into `docs/milestone-1/assets/screenshots/`, and paste the repository and Project links into that file.

### C3. 🖥️ Commit the evidence

```bash
git switch -c docs/m1-board-evidence
git add docs/milestone-1
git commit -m "docs: add GitHub Projects evidence for Milestone 1"
git push -u origin docs/m1-board-evidence       # open PR, get one review, squash-merge
```

## Sanity checklist before submission

- [ ] Repository visible to all 4 members and (if required) the instructor
- [ ] `main` protected; first PR merged with a review
- [ ] 28 issues exist; features carry `Must`/`Should`/`Could` and an area label
- [ ] Story Points total 60; every feature has an Iteration
- [ ] Iteration field is 2 weeks starting 19 Oct 2026
- [ ] Board shows the five columns
- [ ] Review notes in `docs/milestone-1/README.md` resolved
