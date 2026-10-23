# AI workflow and reproducibility limits

Tools recorded: OpenAI Codex and Anthropic Claude through Claude Code. Exact model builds,
complete per-pass prompting and sampling histories are not consistently established in the
retained release records; they must not be inferred from tool names or reconstructed as fact.

The archive collected candidate metadata through Crossref, arXiv and targeted seeds on 13 October
2026. OpenAlex journal queries and citation chasing were run on 15 October 2026. Query strings,
ranking caps and collection counts are in SEARCH_DETAILS.md. The 143-record census is a separate
exploratory collection from the 23-study purposive comparison. It is not a systematic eligibility set.

Historical coding included a same-model repeat, a shuffled-abstract pass from a fresh AI instance
and source-reading batches. Source access was full text for 118 records and abstracts for 25.
The original pass-2/source-pass comparison agreed on 120/143 (83.9%); the final-majority/source-pass
comparison agrees on 130/143 (90.9%). The latter leaves 13 disagreements, all retained in
classification_disagreements.csv. Neither comparison estimates coding accuracy or human reliability.

Selected study fields were charted from source passages and appraised by reporting feature.
Numerical checks locate reported numeric anchors with interpretation limits. Individual original
check dates are retained. CritBench was added to detailed comparison on 20 October 2026 after an
AI-assisted full-source check. EnergyAgentBench's archived PDF matches the official arXiv v2
SHA-256: 5a90ed6c5d27cd1b4eda0cb4ba592d96f6e4b3f1a373176e6efc17b4be5cb14f.
LLM-GridEval remains abstract-based context outside the source-charted subset.

Figures are programmatically drawn with Python; conceptual diagrams report proposed relationships
and the census flow reports collection counts. No new benchmark experiments were performed.
Human source confirmation, author sign-off and experimental replication have not been completed
by this workflow. Validator checks cannot substitute for those activities.
