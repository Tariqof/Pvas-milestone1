# 4. Software lifecycle model

_Mirror of report section 2._

## Selected model: Hybrid (Water-Scrum-Fall)

The outer frame is predictive: the three course milestones are fixed phase gates (Initiation Week 4, Planning baseline Week 7, Closure Week 13). Inside it, execution is Scrum in four two-week sprints (Sprint 0-3), each ending with a sprint review and working demo.

| Sprint | Dates | Focus |
|---|---|---|
| 0 | 19 Oct - 30 Oct 2026 | Spike: rebuild pipeline, reproduce baseline metrics (F6, F9, F11); repo/board setup |
| 1 | 2 Nov - 13 Nov 2026 | Core engine: replay, consistent alert logic (F3-F5, F7, F8). O1 due 13 Nov |
| 2 | 16 Nov - 27 Nov 2026 | Dashboard and alerts, tests/CI (F1, F2, F10, F15). O3 due 27 Nov |
| 3 | 30 Nov - 11 Dec 2026 | Should-haves, deployment, stretch Could-haves. O2 due 11 Dec |

(Sprint contents are a proposal for Sprint 0 planning; see `backlog/backlog.md`.)

## Technical justification

- **Requirements:** core behaviour (look up, monitor live, raise alerts) is defined by the prototype, but alert rules and dashboard workflow depend on usability-tester feedback and must be refined by trying them. Scrum sprints absorb this; the scope baseline is frozen at Milestone 2.
- **Architectural risk:** the largest risks are in the ML layer (do the models detect critical patients reliably; can the dataset be used as planned). Following the risk-driven idea of Boehm's Spiral model, Sprint 0 is a time-boxed spike that rebuilds the pipeline and measures baseline quality before feature work depends on it.
- **Delivery cadence:** course deadlines are fixed and members work ~6 h/week. Two-week sprints give regular demos for the product owner, align with EVM checkpoints, and are long enough for full vertical slices (data, API, UI).

## Alternatives considered

| Model | Why not chosen alone |
|---|---|
| Pure Waterfall | Model quality unknown up front; late discovery forces expensive rework |
| Pure Scrum | Ignores the fixed, document-heavy course gates (charter, WBS, CPM, IEEE docs) |
| Kanban | No timeboxes makes planning against milestones and EVM measurement hard |

## Tooling must match the model

Required by the course: "Your squad's tracking setup in Jira or GitHub Projects must match your selected process model". For this Hybrid/Scrum model that means **2-week iterations and story points**. Exact configuration: [05-github-projects-config.md](05-github-projects-config.md).
