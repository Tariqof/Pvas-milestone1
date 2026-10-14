# 2. Project charter

_Mirror of report section 5. The .docx is the graded copy._

| | |
|---|---|
| Project | Patient Vitals Alert System (PVAS) |
| Sponsor | Asst. Prof. M. Fatih Mintaş |
| Product owner / manager | Yara Abdalla Abdellatif Seed Ahmed |
| Team | 4 students |
| Duration | 13 weeks |
| Starting baseline | github.com/yaraahmed004/Patient-Vitals-Alert-System |
| Budget | 126 person-hours (4 × 3 h × 10 weeks + 6 h midterm week); cash ₺0, open-source tools only _(see review note 1 in README: report §3 says 252)_ |
| Lifecycle model | Hybrid: fixed milestone gates + two-week Scrum sprints |
| Charter approval date | 28.10.2026 |

## Business case

Missed deterioration in intensive care has serious consequences, and single-threshold alarms generate so many false alerts that staff ignore them. PVAS tests whether combining several vitals with ML can raise fewer but more meaningful alerts. The prototype proves the concept but cannot run reliably, its model quality is unknown, and its live view does not change over time. Benefits: one ranked view and fewer false alarms for users; full-stack ML delivery experience for the team; a project covering every PM stage for the course. Cost: team labour.

## Objectives

| # | Objective | Measure | Deadline |
|---|---|---|---|
| O1 | Reproducible system | Runs from clean clone in ≤ 15 min using only the README | 13 Nov 2026 |
| O2 | Working demo | All Must-have acceptance tests pass; dashboard updates in < 2 s | 11 Dec 2026 |
| O3 | More trustworthy alerts | Critical recall > 0.90 (5-fold CV); Moderate recall 0.58 → 0.70 | 27 Nov 2026 |
| O4 | Meet every milestone | M1, M2, M3 submitted on time | Weeks 4, 7, 13 |
| O5 | Stay within effort budget | Actual effort within ±10% of 126 person-hours | 18 Dec 2026 |

## KPIs

| KPI | Baseline | Target |
|---|---|---|
| Critical-class recall | 0.94 (one split, 35 rows) | ≥ 0.90, stratified 5-fold CV mean |
| Moderate-class recall | 0.58 | ≥ 0.70 |
| Decision Tree macro F1 | 0.87 | ≥ 0.88 |
| False alerts on normal readings | not measured | ≤ 10% |
| New reading → dashboard | 5-s batch, values never change | ≤ 2 s, time-ordered replay |
| Time from clean clone to running | not possible | ≤ 15 min |
| Backend test coverage | 0% | ≥ 70% |
| Test users spotting the critical patient in 10 s | not measured | ≥ 4 of 5 |

## Success criteria

O1, O2 and O4 met; Critical and Moderate recall targets reached; product owner accepts the final increment at the last sprint review; sponsor accepts the Milestone 3 deliverables.

## Roles (as written in report §5.5, to be reconciled with the team table)

| Role | Responsibilities |
|---|---|
| Project manager | Planning, scheduling, weekly EVM, risk register, sponsor/stakeholder communication; also develops |
| Frontend developer / UI designer | React dashboard, alert feed, trend charts, accessibility, usability sessions |
| Backend & ML engineer | FastAPI, WebSocket replay, data pipeline, model training/evaluation, SQLite alert log |
| QA, DevOps & documentation lead | Test plan, pytest/Vitest, GitHub Actions CI, deployment, branching rules, IEEE documentation |

## PM authority and governance

The PM may assign/reassign tasks, re-order the backlog and move features between Should and Could, approve changes of ≤ 4 person-hours that touch no Must-have feature or milestone date, and choose libraries within the stack (C5). Larger changes go to the **Change Control Board** (PM, product owner, technical lead, QA lead); see [`../process/change-control.md`](../process/change-control.md).

## High-level risks

Model quality (tiny Critical class); data availability and licence; misleading safety claims; skill split across Python ML and React/TypeScript; team capacity around midterms (weeks 8-9); scope creep. Full register with probability/impact matrix is a Milestone 2 deliverable.

## Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Project sponsor | Asst. Prof. M. Fatih Mintaş | | |
| Product owner | Yara Abdullah Ahmed | | |
| Project manager | _(to fill)_ | | |
