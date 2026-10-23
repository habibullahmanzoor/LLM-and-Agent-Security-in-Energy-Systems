# Full-text checks of census records (15 October 2026)

AI-assisted reading of source PDFs by text search and passage reading. This is a second look at records that were first coded from titles and abstracts. It is not independent human review.

| Record | Source read | What was checked | Result |
|---|---|---|---|
| Saber et al. 2026, LLMs for detecting cyberattacks on protective relays | PDF in corpus | Whether the detector was tested against attacks | Tests combined timestamp and false-data attacks on the measurements, noise and prompt variants; lists adversarial inputs, model poisoning and DoS as further attack surfaces. No adaptive attack on the model. |
| Manzoor et al. 2025, zero-day attacks in digital substations via in-context learning | PDF in corpus | Overall result and failure cases | Over 85% accuracy on zero-day attacks reported; in-context generalization near zero for some attack classes. Model is a transformer trained for ICL, not a pretrained LLM. |
| Kong et al. 2026, LLMs as explainable detectors for ICS | PDF in corpus | Adversarial evaluation | None found in the text. |
| Zaboli et al. 2023, ChatGPT and other LLMs for smart-grid cybersecurity | PDF in corpus | Adversarial evaluation | None found in the text. |
| Woo et al. 2026, system-aware contextual digital twin for ICS anomaly diagnosis | PDF in corpus | Role of the LLM | LLM only explains the output of a conventional detector; authors state raw numeric time series invite hallucination. Data are water-treatment ICS (SWaT, WADI, HAI). |
| Li et al. 2024, risks of LLMs in smart grid | PDF in corpus | Quoted numbers | 93.8% to 43.4% GPT-4 accuracy change and 423 messages confirmed. |
| Hammadia et al. 2026, NERC jailbreak benchmark | PDF in corpus | Quoted numbers | 33.1%, 63.17%, 966 of 2,916 confirmed by text search. |
| Curcio 2026, EnergyAgentBench | PDF in corpus | Adversarial subset | Differences among evaluated models in the adversarial subset not statistically significant (overlapping confidence intervals). |
| Rafy 2026, TwinGridShield | PDF in corpus | Quoted numbers | 30.09% and 500 trials present. |
| Xing et al. 2026, MCP-Guard | arXiv PDF | Quoted numbers | 70,448 samples and 96.01% present. |
| Keppler et al. 2026, CritBench | arXiv 2604.06019 | Results | 81 tasks, five models; GPT-5.1 86.4%, best open-weight model 76.6%, GPT-5 nano 43.3%; accuracy degrades from static to dynamic tasks; domain scaffold improves results. |
| Li et al. 2026 (Informatica), evaluating and securing power systems against LLM vulnerabilities | Journal PDF | Coding | Not an attack evaluation. LSTM/GRU anomaly detection on the HAI dataset plus a TinyLlama packet summarizer. Recoded from threat/risk to grid cyber detection. |
| Li et al. 2026 (J. Cyber Security and Mobility), multimodal LLM power-system threat detection | Journal PDF | Model type and data | BERT, transformer, CNN-LSTM and graph encoders labelled an LLM; 95.4% accuracy on SWaT, power-system and Tennessee Eastman data. |
| Choi et al. 2024, eGridGPT | OSTI report | Evidence type | Design and concept report with no evaluation: local open-source models, human-in-the-loop, digital-twin verification, NERC exam benchmarking. |
| Fu et al. 2026, LLM-GridEval | Abstract only (no open-access PDF found) | - | Quoted figures (37 experiments, 2.25-2.40 times) come from the abstract. |
| Others coded from abstracts only | - | - | Journal and conference records without an open-access PDF found: Halgamuge 2025, Zaboli 2025 (Access), Danso 2025, Ibrahim and Kashef 2026, Rahman 2025, Lee 2025, Boumkheld 2026, Ai 2026, Cai 2025. |

Failure to retrieve a PDF is recorded here and not treated as evidence about the paper.
