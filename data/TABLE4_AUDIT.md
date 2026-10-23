# Table 4 cross-check

Checked 20 October 2026 against evidence_census.csv, fulltext_pass.csv, manuscript bibliography,
and the publisher's LLM-SID article. This is an AI-assisted consistency audit, not human adjudication.

## Arithmetic

8 + 7 + 17 + 7 + 46 + 29 + 21 + 3 + 5 = 143 records.
The first three primary-purpose streams total 32. Historical stream assignments are unchanged.
These are collection totals, not estimates of the size of the scientific literature.

## Corrections

- Removed ai2026llmbusinesslogic (LLM-SID) from the defense row's representative citations.
  Its final archived code is G, not D. The publisher article's experimental datasets are
  TrainTicket, PiggyMetrics and BLV-Bench; the energy framing does not establish a power-grid
  experimental evaluation. Publisher source: https://doi.org/10.1186/s44147-026-01100-9,
  Experiments and results / Datasets, accessed 20 October 2026.
- Corrected the capability stream's provenance: 45 archive records plus one OpenAlex journal-search
  record (W7167905791, a hybrid human-LLM safe-RL study). Removed both 'archive only' and the
  categorical claim that this stream has no security/safety question.
- Included organizational interviews in the threat/risk description and threat-scenario generation
  in the defense description. The latter stream includes generic ICS datasets and disputed LLM scope.
- Replaced 'non-LLM reviews' with primarily classical grid/ML reviews: these records can discuss LLMs.
- Replaced the off-topic description with outside the target intersection: an excluded record can
  still study energy privacy or AI data-center demand without evaluating an LLM component.
- Clarified that benchmark classification does not exclude security tests, notably in ElecBench.
- Representative citations are examples, not an enumeration of every member of a stream.

Added two or three representative citations to each of the five previously empty rows.
Background and outside-scope citations illustrate context or exclusions, not included direct
security evidence. All 45 representative citations match the corresponding stream in the frozen CSV.
The internal manuscript preparation process checked this membership alongside the nine row counts; manuscript build tools are not included in this repository.

## Unresolved scope judgments

S5 retains the ElecBench and trained-from-scratch transformer cases. Further cases include
generic ICS anomaly diagnosis assigned to the defense stream, abstract-only threat generation
across multiple infrastructure sectors, and the safe-RL record assigned to capability rather
than safe-operation benchmarking. The archived majority codes are preserved; these issues
require source-based author adjudication before any eligibility or prevalence claim.
