# S5 Exploratory census and classification sensitivity

Prepared 20 October 2026. No human coding or experimental replication is claimed.

The 143-record census and its historical AI codes are preserved without silent correction.
The main synthesis uses a separately selected set of 22 studies. Primary-purpose stream
membership is not a validated scientific eligibility decision; a benchmark can also test attacks.

| Scenario | T | C | D | T+C+D | V | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| Archived majority assignment | 8 | 7 | 17 | 32 | 7 | Historical AI codes |
| Classify ElecBench by its security component | 9 | 7 | 17 | 33 | 6 | Benchmark versus threat/risk boundary |
| Exclude the small transformer trained from scratch | 8 | 7 | 16 | 31 | 7 | Strict pre-trained LLM scope; B becomes 4 |
| Apply both changes | 9 | 7 | 16 | 32 | 6 | Same total, different membership |

These scenarios change membership, not the 143 collected records. They are not confidence
intervals or exhaustive sensitivity bounds. Further author adjudication can change other codes.

## ElecBench

Record arxiv:2407.05365v2. The archived stream is V; the later full-text pass assigned T.
Source: https://arxiv.org/html/2407.05365v2, Section 2.6.3 (jailbreak, prompt injection and hybrid
attacks), Appendix A.5 (security scores), Appendix B.5 (examples). Checked 20 October 2026.
Its primary benchmarking purpose does not justify excluding its security component from an
exhaustive claim about adversarial energy-LLM studies. The former headline 'only three' is retired.
Exact attack construction and denominators require further source/data inspection before treating
this as an attack-success-rate study comparable with the NERC assistant benchmark.

## Small transformer detector

Record arxiv:2501.16453v1, Detecting Zero-Day Attacks in Digital Substations via In-Context Learning.
The archived stream is D; the full-text coding pass assigned B and recorded a small GPT-2-style
transformer trained from scratch on packet features. This is a documented scope dispute, not a
new independently verified exclusion. A strict pre-trained foundation-model definition would
exclude it; a broader language-model-style architecture definition may retain it.

## Coding provenance

See evidence_census.csv for all historical codes and fulltext_pass.csv for the later source pass.
The first repeat used the same AI model and was not independent. A later fresh AI instance
worked from shuffled abstracts; five further instances worked on blinded source batches.
The original same-model repeat agreed on 95.1% of nine-stream codes (kappa 0.94); a fresh-instance
abstract pass agreed on 90.2% (kappa 0.88); the source pass agreed on 83.9% (kappa 0.80).
Source access was full text for 118 records and abstract-only for 25. Majority voting can retain
an abstract error despite a contradictory full-text pass. These statistics measure AI consistency,
not accuracy, independent human reliability or systematic-review completeness.

An interview study combining energy with other infrastructure sectors, generic IDS benchmarks
in energy-framed papers, and conceptual governance proposals also require explicit author judgment.
Do not use the 32-record primary-purpose total as a verified denominator for the field.

## Complete disagreement register (20 October 2026)

All 13 disagreements between frozen majority codes and the later source-pass code are in `classification_disagreements.csv`. This is distinct from the earlier pass-2 comparison (120/143, 83.9%). The final-majority/source-pass comparison agrees on 130/143 (90.9%). Neither is a human reliability statistic. The two scenarios above are illustrative, not an exhaustive disagreement resolution. No historical code was changed.
