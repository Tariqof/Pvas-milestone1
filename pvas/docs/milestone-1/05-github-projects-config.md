# 5. GitHub Projects configuration (evidence that tooling matches the model)

Target: Hybrid model with Scrum execution, so the board needs **two-week iterations** and **story points** (course requirement for Week 4).

## Target configuration

| Item | Setting |
|---|---|
| Project name | `PVAS - Product Backlog` (linked to the team repository) |
| Items | 28 issues: F1-F19 (features), D1-D6 (course deliverables), C1-C3 (setup chores) |
| Story Points | Number field, Fibonacci 1, 2, 3, 5, 8. Features only; total 60 (Must 31 / Should 21 / Could 8) |
| Iteration | Iteration field, **2-week duration, first iteration starts Mon 19 Oct 2026**, named Sprint 0 … Sprint 3 |
| Status columns | Backlog → Sprint Ready → In Progress → In Review (PR open) → Done |
| Labels | Priority: `Must` `Should` `Could`. Area: `frontend` `backend` `ml` `docs` `devops`. Type: `feature` `baseline` `deliverable` `chore` `change-request` `bug` |
| Milestones | Milestone 1 (Week 4), Milestone 2 (Week 7), Release 1.0 (Week 12), Milestone 3 (Week 13) |
| WIP | Not used (Scrum uses sprint capacity; WIP limits are the Kanban setting) |

## Who does what

| Step | How | Done by |
|---|---|---|
| Labels, milestones, issues, project, link to repo, Story Points field, add all issues, set story points | `scripts/github/bootstrap_backlog.py` | Script (run by one member) |
| Iteration field (2 weeks, start 19 Oct 2026, 4 sprints) | GitHub web UI only; CLI cannot create it | **You, on GitHub** |
| Rename Status options to the five columns | GitHub web UI | **You, on GitHub** |
| Assign each item to a sprint (proposal in `backlog/backlog.md`) | Web UI, table view | **You, on GitHub** |
| Board view, Table view, Roadmap view | Web UI | **You, on GitHub** |
| Built-in workflows (item closed → Done, PR merged → Done, new items → Backlog) | Project → ⋯ → Workflows | **You, on GitHub** |

Step-by-step UI instructions are in [github-setup-guide.md](github-setup-guide.md), Part C.

## Evidence to attach (fill in after setup)

Save screenshots in `assets/screenshots/` and reference them here:

- [ ] `board-view.png`: Board grouped by Status showing the five columns
- [ ] `table-view.png`: Table with Story Points and Iteration columns visible
- [ ] `iteration-settings.png`: Iteration field settings (2-week duration, 19 Oct 2026 start)
- [ ] `roadmap-view.png`: Roadmap by Iteration (optional)

Project URL: `https://github.com/orgs-or-users/<owner>/projects/<n>` _(paste here)_
Repository URL: `https://github.com/<owner>/<repo>` _(paste here)_
