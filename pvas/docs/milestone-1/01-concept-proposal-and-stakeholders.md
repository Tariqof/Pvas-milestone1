# 1. Concept proposal and stakeholder analysis

_Mirror of report sections 1, 3 and 4. The .docx is the graded copy._

## Concept

PVAS is a web-based monitoring system that tracks ICU patients' vital signs and notifies staff of abnormalities, combining real-time monitoring with machine-learning classification. It uses heart rate, SpO₂, temperature, respiratory rate and systolic/diastolic blood pressure. A **Decision Tree** assigns a status level (0 Normal, 1 Mild, 2 Moderate, 3 Critical, 4 Outlier) and an **Isolation Forest** flags unusual combinations of vitals. Results appear on a live dashboard with alerts for critical cases.

**Baseline (prior work):** prototype by Yara Ahmed, CEN3001 report. Decision Tree selected at 87.1% accuracy (macro F1 0.87) over Logistic Regression (75.9%) and Linear SVM (76.0%); Isolation Forest chosen over K-Means. Weak spots: Moderate class recall 0.58; Critical class has only 35 test rows; Isolation Forest only checked visually.

**Problem:** alarm fatigue from single-threshold bedside alarms; the prototype cannot be run from a fresh clone, its "live" feed repeats each patient's first reading, two WebSocket endpoints map status codes differently, evaluation is not reproducible, and there is no login, alert acknowledgement, history or tests.

**Solution:** (1) reproducible data/ML pipeline, (2) FastAPI backend with REST + WebSocket replay and one consistent alert logic, (3) React dashboard with live grid, prioritised alert feed with acknowledgement, lookup and trend charts.

**Target users:** ICU nurses (live dashboard, acknowledge alerts) and ICU doctors (lookup, trends, history).

**Technology:** React + TypeScript + Vite + Tailwind + Radix UI; FastAPI; scikit-learn, pandas, joblib; synthetic CSV dataset (IEEE DataPort), SQLite; Git, GitHub, GitHub Projects, GitHub Actions.

## Feasibility (TELOS)

| Dimension | Verdict | Key point |
|---|---|---|
| Technical | Feasible | Working prototype exists; risk is the tiny Critical class |
| Economic | Feasible (strategic) | Cash cost ₺0; notional NPV −₺25,200, justified as a safety-oriented prototype |
| Legal | Feasible with conditions | Synthetic data only; "not for clinical use"; dataset licence to confirm in Sprint 0 |
| Operational | Feasible | Familiar colour-coded severity conventions |
| Schedule | Feasible | 5 of 19 features exist in prototype form; MoSCoW cut line |

## Stakeholder register (Mendelow power-interest)

| Stakeholder | Role and interest | Int./Ext. | Attitude | Power | Interest | Engagement |
|---|---|---|---|---|---|---|
| Asst. Prof. M. Fatih Mintaş (instructor) | Sponsor and evaluator | External | Neutral | High | High | Manage closely |
| Project team (4 students) | Plan, build, test, document | Internal | Supporter | High | High | Manage closely |
| Product owner (Yara Abdullah Ahmed) | Owns backlog priorities, accepts increments | Internal | Supporter | High | High | Manage closely; CCB member |
| Dataset publisher (IEEE DataPort) | Licence holder | External | Neutral | High | Low | Keep satisfied |
| Asst. Prof. Mohammed Al-Hubaishi | Baseline report co-author; ML guidance | External | Supporter | Low | High | Keep informed |
| ICU nurses and doctors (intended users) | Need trustworthy alerts | External | Neutral | Low | High | Keep informed |
| Patients | Most affected by missed/false alerts | External | Neutral | Low | High | Keep informed |

## Communication plan

| Audience | Channel | Frequency | Owner |
|---|---|---|---|
| Project team | Group chat | Continuous | Project manager |
| Product owner | Sprint planning and review | Every two weeks | Project manager |
| Course instructor | Milestone reports | Weeks 4, 7, 13 | Whole team |
| Technical record | GitHub issues, PRs, commits | Continuous | All developers |
