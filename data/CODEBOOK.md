# Classification codebook

The tuple is **surface, mechanism, attacker control, action authority, consequence; evidence**. It is an author-proposed synthesis instrument, not a validated standard. A study can have several components and codes. NR means not reported, not recorded or not established for that field; it never means zero.

| Dimension | Values and decision rule |
|---|---|
| Surface | Model/artifact, user input, retrieved content, numerical data, tool metadata/output, human workflow. Record the manipulated or checked object rather than every topic mentioned. |
| Mechanism | Instruction redirection, numerical corruption, persistent poisoning/backdoor, disclosure, non-adversarial error. Distinguish substituted numbers from malicious instructions, and reliability from adversarial manipulation. |
| Attacker control | Query-only, content insertion/replacement, tool/server control, training/artifact control, no adversary, NR. Preserve knowledge, write access and budgets where supplied. |
| Authority | A0 answers/recommendations; A1 simulated/sandboxed tool execution; A2 operational proposal requiring separate authorization; A3 real operational execution. Code demonstrated authority, not a proposed deployment. Developer-host compromise does not automatically map to energy A3. |
| Consequence | Task/answer error, disclosure, financial error, physical violation, service/equipment impact. Separate measured outcomes from prospective consequences. |
| Evidence | E0 conceptual; E1 text/answer testing; E2 tool/workflow testing; E3 physics-evaluated simulation; E4 operational evidence. These describe endpoints, not rigor or a numerical quality rank. Formal claims and physical-laboratory components are described separately. |

## S1 field interpretation

`id`, `arxiv`, `bibkey`, `title` identify the study. `comparison` assigns the main displayed table; `evidence_stream` distinguishes direct energy, conceptual, capability, privacy and general security sources. These streams are editorial classifications, not original automated RQ labels.

`surface`, `mechanism`, `attacker_control`, `authority` and `evidence` implement the tuple. `model_setting` records the tested setup at the granularity used by the comparisons; it is not a complete registry of every experimental model/API version. `metric_result` preserves the selected reported result and condition; `measured_consequence` names its endpoint. Quantities are original-study reports, not measurements reproduced here. Classification accuracy, ASR, membership AUC, detector accuracy and unsafe acceptance have different denominators and must not be pooled.

`source_locators` uses one-based PDF page numbers, including front matter, unless expressly identified as HTML sections. `reviewed_version`, `source_url` and `source_sha256` distinguish an arXiv release from the bytes inspected. A DOI in BibTeX may point to a published version different from the source-checked preprint; users should recheck any claim changed between versions.

`archive_retrieved_keys` joins to S2 when the study belongs to its 472 archived retrieved records. An empty value does not exclude a study from S1: targeted supplementary sources are explicitly labeled in `provenance` and do not change the archived flow. `review_status` and `checked_on` document the AI-assisted field check. Independent author review remains pending.

## S2 field interpretation

S2 keeps one row per archived retrieved **record key**, not necessarily one per underlying research study. The original workflow's deduplication rules and any residual metadata/version ambiguity still apply. `archived_year`, `authors`, `venue`, `doi` and `arxiv` preserve collected metadata. `rq_labels_automated`, `priority_tier`, `keyword_charted`, `layers_automated`, `threats_automated` and `defenses_automated` are provisional automated outputs. `substantive_eligibility` explicitly declines to turn retrieval/readability into scientific inclusion. `selected_evidence_id` and `source_checked_scope` identify the narrower S1 check.

To upgrade this package to a systematic evidence atlas, retain these automated fields, add independent eligibility decisions, resolve versions at study level, code investigated relationships from full text, document uncertainty/disagreement and publish a decision trail. No independent agreement statistic is currently available.

## S3: critical reporting appraisal

Six independent features are recorded: victim-aware attack refinement, clean/attacked comparison, legitimate utility, outcome oracle, physical checker mismatch and reproduction artifacts. They do not replace the surface/authority/endpoint tuple or create a study-quality ranking. D means described/evaluated in the checked source; L means limited/component-specific; NE means not established in checked passages; NA means not applicable. D does not mean independently reproduced, and NE is not a universal absence claim.

An attack-method baseline is distinct from a benign workload. Numerical corruption is distinct from instruction injection. Describing a judge does not make it independent or correct. A reported code release is distinct from an independently exercised reproduction package. A conceptual paper can legitimately have NA experimental features; these should not lower an invented numerical score.

Each row has an interpretation note, source locator, reviewed version and assessment status. No validated risk-of-bias instrument, author-independent review, artifact execution or pooled causal estimate is claimed.

## S4: related-review scope comparison

Positive overlap is recorded for eight reviews. `check_basis` distinguishes five full-source-passage checks from three abstract/summary/metadata checks. `reviewed_edition` prevents mixing preprint and published counts or features. The Antonesi preprint inspected here reports 99 included articles; that count is not asserted for its separately cited published edition.

The scope comparison does not score coverage omissions, infer a search cutoff from publication year, establish review quality from self-described methodology, or independently verify all experiments cited by a review. Source locations and fingerprints identify the material actually inspected.

## Numerical claim audit

The 16 claim records preserve source conditions and endpoints. One-based PDF pages and numeric anchors help locate quantities; anchors are matched after Unicode normalization and thousands-separator removal. They are a navigation/consistency check, not proof of semantic interpretation. AgentDojo is checked by HTML version/section rather than local PDF matching. Claim interpretation remains AI-assisted and requires independent author verification.

## Proposed evaluation guidance (outside S1-S4)

`metric_dictionary.csv` has `id`, `metric`, `unit`, `numerator`, `denominator` and `qualification`. Its JSON records the recommendation status and synthesis basis. These definitions are for proposed future evaluations and are not source measurements, review-quality scores or evidence of benchmark integration. The blank `evaluation_worksheet.md` records intended claims, authority, attacker access, independent oracles, four paired conditions and raw outcome accounting. A zero denominator is undefined, not zero; policy authorization and physical admissibility must be evaluated separately.


## S5: exploratory census and sensitivity

See CLASSIFICATION_SENSITIVITY.md. Primary-purpose stream assignment is separate from scientific
eligibility: benchmarks may test attacks. Historical codes remain frozen; later corrections
must be recorded separately with source evidence. The T+C+D total is not a verified count of all
direct energy-LLM security studies. No independent human coding agreement is currently available.
