# 3. High-level scope, assumptions and constraints

_Mirror of report sections 6 and 7. The full feature table with SP and sprint proposal is in [`../../backlog/backlog.md`](../../backlog/backlog.md)._

## Product scope

Release 1.0: a reliable ICU vitals monitoring and alerting demo on synthetic data, with a live dashboard, understandable alerts and a reproducible model evaluation. 19 features prioritised with MoSCoW, **60 story points** (Must 31, Should 21, Could 8). F1-F5 are baseline (exist in the prototype, need verification), F6-F19 are new.

| Priority | Features |
|---|---|
| Must | F1 lookup, F2 live dashboard, F3 classification, F4 anomaly detection, F5 alert with reasons, F6 reproducible setup, F7 time series replay, F8 consistent alert rules, F9 rigorous model evaluation, F10 alert feed, F11 cleanup |
| Should | F12 trend view, F13 alert history, F14 staff login, F15 tests and CI, F16 demo deployment |
| Could | F17 filters, F18 per-patient thresholds, F19 ensemble trial |

## Project scope

Project management artefacts (charter, WBS, CPM/PERT, Gantt, estimation, risk register, weekly EVM, change control); environment and tools (repo with branch protection, GitHub Projects, Actions CI, local environments, demo hosting); ML work (licence check, exploration, training and evaluation scripts, evaluation report); quality activities (code review on every PR, test plan, usability tests with 5 users); documentation and handover (README, OpenAPI docs, IEEE documentation, SCM audit, oral defence, retrospective).

## Deliverables

| Deliverable | Due |
|---|---|
| Milestone 1 report and GitHub Projects backlog | Week 4 |
| Milestone 2 planning package | Week 7 |
| Model evaluation report | Week 10 |
| Release 1.0 and demo deployment | Week 12 |
| Repository (code, training scripts, tests, CI, README) | Continuous; final Week 12 |
| Test plan, results, usability notes | Week 12 |
| Milestone 3 package | Week 13 |

## User acceptance criteria (summary)

AC1 all Must features pass tests · AC2 clean-clone run ≤ 15 min · AC3 Critical recall ≥ 0.90, Moderate ≥ 0.70, false alerts ≤ 10% · AC4 new reading on dashboard ≤ 2 s, values change in recorded order · AC5 same status in every view · AC6 every alert shows a reason and can be acknowledged · AC7 ≥ 4 of 5 test users find the critical patient within 10 s · AC8 "not for clinical use" on every screen; no real patient data.

## Out of scope

Real patient data or hospital integrations (HL7/FHIR, EHR); clinical use, validation or certification; SMS/pager/phone notifications; deep learning or new datasets; native mobile apps and multi-hospital administration; paid hosting after the course. Requests to add any of these go through change control.

## Assumptions

| ID | Assumption | If false |
|---|---|---|
| A1 | ~3 h/week per member (~1.5 in midterm week) | Drop Could features first, then re-plan Should |
| A2 | Instructor approval to build on an existing project holds for all milestones | Confirm in writing; re-scope |
| A3 | IEEE DataPort dataset can be downloaded by every member and used for the course | Use another open synthetic dataset or a documented generator |
| A4 | Critical class (~0.75%) is large enough for stratified CV | Class weighting/resampling; report confidence limits |
| A5 | A clinical advisor gives ≥ 2 short sessions | Use published early-warning thresholds; ask Asst. Prof. Al-Hubaishi |
| A6 | Free tiers support FastAPI with WebSockets | Demo locally; record a backup video |
| A7 | Requirements stable after Milestone 2 | Change request; re-baseline and log in EVM report |

## Constraints

| ID | Type | Constraint |
|---|---|---|
| C1 | Schedule | M1 Week 4, M2 Week 7, M3 and defence Week 13 (14-18 Dec 2026) |
| C2 | Schedule | Republic Day (29 Oct) and midterm week reduce capacity |
| C3 | Budget | ₺0 cash; open-source tools and free tiers |
| C4 | Team | Exactly 4 part-time students |
| C5 | Technology | Keep React/TypeScript, FastAPI, scikit-learn |
| C6 | Process | Git with documented branching, PR reviews, weekly effort logs |
| C7 | Documentation | IEEE format for final documentation |
| C8 | Data and safety | Synthetic data only; "not for clinical use" on every screen |
