# Supplement to LLM and Agent Security in Energy Systems: A Critical Survey

Version 1.1.0, prepared 2026-10-20. Repository: https://github.com/habibullahmanzoor/LLM-and-Agent-Security-in-Energy-Systems. Manuscript submission status is separate.

The primary synthesis uses 23 purposively selected studies (seven attack/risk, six defenses and ten benchmarks). Individual source versions and
original check dates are preserved. The census is an exploratory collection, not the eligibility
population for the synthesis. AI coding agreement is not independent human validation.

| Material | Contents |
|---|---|
| S1 selected_evidence.csv / .json | 23 comparison records, access, authority, endpoints and source locators |
| S2 literature_index.csv | 472 archived retrieved records; 239 provisionally keyword-charted |
| S3 evidence_assessment.csv / .json | Six reporting features for the 23 selected studies |
| S4 related_review_comparison.csv / .json | Eight reviews; five full-source and three abstract/summary checks |
| S5 CLASSIFICATION_SENSITIVITY.md | Census provenance and illustrative scenarios |
| classification_disagreements.csv | All 13 frozen-code/source-pass differences; human adjudication pending |
| evidence_census.csv | 143 records; historical codes preserved, including disagreements with the source pass |
| fulltext_pass.csv | AI source-pass notes; 118 full-text and 25 abstract-only records |
| claim_audit.csv / .json | 17 numerical claims with source locations; not experimental replication |
| metric_dictionary.csv / .json | Eight proposed definitions; not observations |
| evaluation_worksheet.md | Editable paired evaluation plan |
| worked_evaluation_example.md | Invented example counts; excluded from evidence populations |
| CODEBOOK.md, DATA_CARD.md, SEARCH_DETAILS.md | Definitions, scope and historical searches |
| index.html | Local searchable view of the 23-study comparison |

Source PDFs and local source manifests are not redistributed. A source SHA-256 identifies
reviewed bytes without distributing them. A source check is not proof that an experiment is correct.
The Cheng et al. Energy comparison was added after the frozen census and does not change its denominator.

## Regenerate figures

From the repository root, install `requirements.txt` and run
`python scripts/build_publication_figures.py`. See the root README for details.
The manuscript PDF, LaTeX source and manuscript compilation tools are not included.
Historical search details describe the original collection rather than a new live search.

## Reuse and release

Source verification and journal portal declarations remain author responsibilities. The owner-selected MIT license is in the repository root. Repository availability does not imply journal publication, a DOI or author verification. Cite the survey for its synthesis and the original studies for their findings.
