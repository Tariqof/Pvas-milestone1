# Milestone 1 - Initiation (Week 4, 5% of course grade)

**Graded copy:** [`submission/SEN4100_Milestone1_PVAS.docx`](submission/SEN4100_Milestone1_PVAS.docx). The Markdown files here mirror the key sections so they are searchable and reviewable in GitHub. If they ever disagree, the .docx wins; update the Markdown to match.

## Course requirements and where they are covered

| Requirement | Where |
|---|---|
| Project concept proposal and stakeholder analysis | [01-concept-proposal-and-stakeholders.md](01-concept-proposal-and-stakeholders.md) · report §1, §3, §4 |
| Formal project charter (business justification, objectives) | [02-project-charter.md](02-project-charter.md) · report §5 |
| High-level scope definition, assumptions and constraints | [03-scope-assumptions-constraints.md](03-scope-assumptions-constraints.md) · report §6, §7 |
| Documented lifecycle model with formal technical justification (requirements, architectural risk, delivery cadence) | [04-lifecycle-model.md](04-lifecycle-model.md) · report §2 |
| Jira / GitHub Projects setup matches the chosen model (2-week sprints + story points) | [05-github-projects-config.md](05-github-projects-config.md) and the live GitHub Project |
| GitHub repository set up | [github-setup-guide.md](github-setup-guide.md) |

## Submission checklist

- [ ] Repository created, `main` protected, all members added as collaborators
- [ ] Labels, milestones, 28 issues and the GitHub Project created (script or manual)
- [ ] Project fields configured: Story Points, Iteration (2-week, from 19 Oct 2026), Status columns
- [ ] Screenshots of the board, fields and iteration settings saved in `assets/screenshots/`
- [ ] Project link / repository link included in the submitted report
- [ ] Open items from the review notes below resolved
- [ ] Final .docx copied into `submission/`

## Review notes found while building this (resolve before submitting)

1. **Effort budget disagrees with itself.** Section 3 (Schedule, Economic) says **252 person-hours**; the charter (§5) and assumption A1 give **126** (4 × 3 h × 10 weeks + 6 h). The ₺25,200 investment, NPV and ROI are all computed from 252, and objective O5 uses 126.
2. **Roles table has placeholders.** §5.5 still says "[Member 1 Name]" … "[Member 4 Name]", and defines four roles (PM, Frontend, Backend & ML, QA/DevOps) while the team table lists two Frontend developers and no QA/DevOps member. The approval table also has "[Member 1 Name]". The text also refers to "5.4" for the team, which is the Success Criteria section.
3. **Product owner vs project manager.** "Yara Abdullah Ahmed" (product owner) and "Yara Abdalla Abdellatif Seed Ahmed" (project manager) look like the same person with two spellings; the charter row is "Product owner/manager". Decide whether one person holds both roles and spell the name consistently. A PO who is also on the CCB and the PM is a governance point the instructor may ask about.
4. **Section numbering skips** 5.6 and 5.8.
5. **Project concept.** The report describes PVAS (ICU monitoring). If the team's actual project is something else, tell me and I will regenerate the backlog.
