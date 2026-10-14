# Contributing to PVAS

Process constraint C6: Git with a documented branching strategy, pull-request reviews and weekly effort logs.

## Branching strategy

- `main` is always demonstrable. **No direct pushes**; changes arrive by pull request only (branch protection - see `docs/milestone-1/github-setup-guide.md`).
- Work on short-lived branches cut from `main`:

| Prefix | Use | Example |
|---|---|---|
| `feature/` | Backlog feature | `feature/F7-timeseries-replay` |
| `fix/` | Bug fix | `fix/status-label-mismatch` |
| `docs/` | Documentation / course deliverable | `docs/m1-charter` |
| `chore/` | Tooling, config, cleanup | `chore/ci-workflow` |

- Branch names start with the backlog ID where one exists (`F7`, `D2`, `C1`).

## Commit messages

Imperative present tense, short subject, ID in front where relevant:

```
F8: use one status mapping for REST and WebSocket endpoints
docs: add stakeholder register to milestone 1
```

## Pull requests

1. Open a PR from your branch to `main` using the PR template; write `Closes #<issue>` so the issue moves to Done on merge.
2. At least **one other member** reviews and approves. Authors do not merge their own unreviewed work.
3. From Sprint 3, CI (F15) must pass before merge.
4. Squash-merge, then delete the branch.

## Definition of done (feature)

- Acceptance criteria on the issue are all checked
- Reviewed and merged via PR
- Tests added or updated where the area has tests
- README/docs updated if behaviour changed
- No real patient data; the "not for clinical use" notice is intact (AC8)

## Change control

Anything outside agreed scope is logged as a **change request** issue (template provided) and decided by the Change Control Board: project manager, product owner, technical lead (backend & ML) and QA lead. The project manager alone may approve changes of up to 4 person-hours that touch no Must-have feature or milestone date. Changes to alert logic must show Critical-class recall does not drop. See `docs/process/change-control.md`.

## Board workflow

Backlog → Sprint Ready → In Progress → In Review (PR open) → Done. Move your own card; keep Story Points and Iteration up to date.
