# Using Generative AI Tools - Boon or Bane

Student ID: 50508127

This repository organises the data, analysis, documentation, and outputs for a research project examining the benefits and risks of generative AI tools.

## Project structure

| Folder | Purpose | Access guidance |
| --- | --- | --- |
| `01_literature_review/` | Article notes, search records, and literature synthesis | Shareable within the project team; observe publisher copyright |
| `02_quantitative_analysis/` | Survey instruments, de-identified data, scripts, and results | Raw identifiable survey data must not be committed |
| `03_qualitative_analysis/` | Interview protocols, de-identified transcripts, coding, and insights | Consent forms and identifiable transcripts require restricted storage |
| `04_drafts_and_reports/` | Proposals, paper drafts, and final reports | Team access while drafts are in progress |
| `05_additional_materials/` | Information sheets and approved media | Check consent and licensing before sharing |
| `06_project_management/` | Data-management notes and the project logbook | Team access |
| `journal/` | Applied-class responses and evidence checklist | Student coursework record |

Each folder contains a short README explaining what belongs there. Placeholder files demonstrate the intended naming convention without exposing real or sensitive research data.

## Naming convention

Use lowercase descriptive names with underscores and an ISO date where relevant:

`YYYY-MM-DD_content_description_version.ext`

Examples:

- `2026-09-14_survey_questions_v01.md`
- `2026-09-14_deidentified_survey_sample_v01.csv`
- `2026-09-14_analysis_summary_v01.md`

Avoid spaces, vague names such as `final_final`, and personal identifiers. Increase the version number for significant document revisions; Git records the detailed history.

## How to navigate

Start with this README, then open the README in the relevant numbered folder. Analysis scripts are under `02_quantitative_analysis/scripts/`; generated results belong under `02_quantitative_analysis/results/`. Draft and final written outputs are separated under `04_drafts_and_reports/`.

## Contributing

1. Pull the latest `main` branch.
2. Create a descriptively named branch, such as `analysis/survey-demographics`.
3. Make one logical change at a time and do not commit identifiable or confidential data.
4. Use a meaningful commit message explaining the change.
5. Push the branch and open a pull request.
6. Ask another team member to review the change before merging.
7. Resolve any merge conflicts carefully and verify the final files before merging.

## Data protection

This repository contains only synthetic or de-identified examples. Identifiable participant data, signed consent forms, credentials, and other confidential material must be kept in an approved restricted-access UQ storage system, not in GitHub.

