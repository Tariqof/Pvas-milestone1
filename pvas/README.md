# Patient Vitals Alert System (PVAS)

> **Not for clinical use.** PVAS is an education and demonstration project that uses synthetic data only. It must not be used to make decisions about real patients.

PVAS is a web-based ICU monitoring prototype. It watches patient vital signs (heart rate, SpO₂, temperature, respiratory rate, systolic and diastolic blood pressure), classifies each reading with a Decision Tree, detects unusual combinations of vitals with an Isolation Forest, and shows ranked, colour-coded alerts on a live React dashboard.

Course project for **SEN4100 Software Project Management**, Software Engineering, Haliç University (Instructor: Asst. Prof. M. Fatih Mintaş). It builds on the baseline prototype [yaraahmed004/Patient-Vitals-Alert-System](https://github.com/yaraahmed004/Patient-Vitals-Alert-System).

## Team

| Member | Role |
|---|---|
| Yara Abdalla Abdellatif Seed Ahmed | Project Manager |
| Eusha Samara | Frontend Developer |
| Elif Beren Uşak | Frontend Developer |
| Tarig Noureldin Awadelkarim | Backend Developer |

## Process model

**Hybrid (Water-Scrum-Fall):** the three course milestones are fixed phase gates; inside them the team runs four two-week Scrum sprints (Sprint 0 to Sprint 3, starting 19 October 2026). Backlog and board live in GitHub Projects. Details and justification: [`docs/milestone-1/04-lifecycle-model.md`](docs/milestone-1/04-lifecycle-model.md).

## Repository layout

```
.github/            Issue templates and pull request template
backlog/            Product backlog source (JSON/CSV/Markdown) used to seed GitHub Projects
data/               Dataset download target (contents are git-ignored)
docs/
  milestone-1/      Initiation: proposal, stakeholders, charter, scope, lifecycle model, board config
  milestone-2/      Planning baseline: WBS, CPM/PERT, Gantt, estimation, risk register
  milestone-3/      Closure: SCM audit, EVM report, IEEE documentation, retrospective
  process/          Branching strategy, change control, definition of done
frontend/           React + TypeScript + Vite dashboard
backend/            FastAPI service (REST + WebSocket)          [Sprint 0-1]
ml/                 Training and evaluation scripts             [Sprint 0]
scripts/github/     One-off script that seeds labels, issues and the GitHub Project
```

## Quick start (frontend skeleton)

Requires Node.js 20+.

```bash
cd frontend
npm install
npm run dev        # http://localhost:5173
```

Backend and ML setup instructions will be added by feature **F6 (Reproducible setup)**. The goal (objective O1) is to run the whole system from a clean clone in 15 minutes or less using only this README.

## Contributing

Every change goes through a feature branch and a reviewed pull request that links its issue. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.

## Data and licence notes

- Only synthetic ICU vital-signs data (IEEE DataPort) is used. No real patient data may ever be committed.
- The dataset and trained models are **not** stored in Git. See [`data/README.md`](data/README.md).
- The dataset licence is being confirmed in Sprint 0 (issue C2); this README will cite it once confirmed.
