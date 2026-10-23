# Search and screening details (moved from the manuscript body)

These LaTeX tables were removed from the main text to shorten the paper. They describe the automated collection, not manually verified eligibility.

## tab:queries

```latex
\begin{table}[!htbp]
\caption{Plain-language collection query strings.}\label{tab:queries}
\small
\begin{tabularx}{\textwidth}{@{}XX@{}}
\toprule
\textnormal{large language models smart
grid security} & \textnormal{large language model smart meter} \\
\textnormal{large language model energy systems security privacy} & \textnormal{large language model critical infrastructure} \\
\textnormal{large
language model power systems security} & \textnormal{large language model phishing} \\
\textnormal{large language models electricity grid threats} & \textnormal{energy system phishing social engineering AI} \\
\textnormal{large language models security grid} & \textnormal{prompt injection large language
models} \\
\textnormal{false data injection smart grid machine
learning} & \textnormal{LLM agent security survey} \\
\textnormal{adversarial machine learning power system state estimation} & \textnormal{retrieval augmented generation security} \\
\textnormal{adversarial
attacks load forecasting} & \textnormal{large language model supply chain security} \\
\textnormal{generative AI energy cybersecurity} & \textnormal{model context protocol security} \\
\textnormal{LLM agents power
grid control} & \textnormal{trustworthy large language models safety survey} \\
\textnormal{large language model load forecasting} & \textnormal{EU AI Act large language model
energy compliance} \\
\textnormal{large language model
electricity market} & \textnormal{large language model power system dispatch operations} \\
\textnormal{large language model building energy management} & \textnormal{generative AI critical infrastructure protection energy} \\
\textnormal{large
language model electric vehicle charging smart grid} & \textnormal{AI cybersecurity smart
grid defense} \\
\bottomrule
\end{tabularx}
\end{table}
```

## tab:keywords

```latex
\begin{table}[!htbp]
\caption{Keyword groups and example Boolean combinations used in the search
(adapted per database syntax).}\label{tab:keywords}
\small
\begin{tabularx}{\textwidth}{@{}p{2.9cm}p{5.6cm}X@{}}
\toprule
\textbf{Group} & \textbf{Keywords / terms} & \textbf{Example combination}\\
\midrule
LLM / agent & ``large language model'', ``LLM'', ``foundation model'', ``generative AI'',
``agent'', ``RAG'', ``model context protocol'' & ``large language model'' AND ``smart grid''\\
Energy context & ``smart grid'', ``power system'', ``electricity'', ``load forecasting'',
``electricity market'', ``smart meter'', ``EV charging'', ``energy system'' &
``large language model'' AND ``load forecasting''\\
Security & ``security'', ``attack'', ``false data injection'', ``adversarial'',
``jailbreak'', ``prompt injection'', ``privacy'', ``poisoning'' &
``false data injection'' AND ``smart grid''\\
Offense & ``phishing'', ``social engineering'', ``critical infrastructure'' &
``large language model'' AND ``phishing''\\
Governance & ``EU AI Act'', ``NIST'', ``AI RMF'', ``ISO 42001'', ``NERC CIP'' &
``EU AI Act'' AND ``large language model''\\
\bottomrule
\end{tabularx}
\end{table}
```

## tab:criteria

```latex
\begin{table}[!htbp]
\caption{Eligibility criteria and exclusion reason codes. Rules describe the implemented automated pipeline; they do not establish manually verified eligibility.}\label{tab:criteria}
\small
\begin{tabularx}{\textwidth}{@{}p{1.5cm}X@{}}
\toprule
\textbf{Code} & \textbf{Rule}\\
\midrule
\textbf{Include} & Candidate scope: LLM/agent security in energy; energy deployment and capability studies;
classical grid-security/privacy studies used as background; generic LLM-security and governance
sources relevant to an RQ. Rule-based matching assigned priority tiers rather than confirming all
PCC elements in every record. The collector emphasized 2019--2026; the screening implementation
also admitted historical material from 2015 onward and earlier seminal FDI exceptions.\\
X1 & Not published in English.\\
X2 & Editorial, retraction note, or meeting overview (no primary content).\\
X3 & Before the implemented 2015 lower bound without a seminal FDI exception, or no retrievable year.\\
X4 & General LLM/GenAI topic without security, safety, privacy or energy relevance; or no targeted
concept found.\\
X5 & No research question addressed (adjacent topic only).\\
DUP & Duplicate record across databases or preprint/published version of the same work.\\
F1/F2 & PDF unreadable or flagged by a first-page retraction-wording check; no substantive eligibility decision implied.\\
\bottomrule
\end{tabularx}
\end{table}
```


## Journal-indexed search (OpenAlex), run 15 October 2026

Filter: publication date from 2023-01-01; types article, review, proceedings-article; 50 results per query (relevance-ranked). Records were then kept only if title or abstract matched an LLM term, an energy term and a security/safety term, and the title was not already in the archive.

| Query | Records returned |
|---|---|
| large language model smart grid security | 50 |
| large language model power system cybersecurity | 50 |
| LLM agent power grid attack | 50 |
| prompt injection energy system | 50 |
| jailbreak large language model power grid | 50 |
| large language model false data injection | 50 |
| large language model smart meter privacy | 50 |
| LLM energy management adversarial attack | 50 |
| generative AI smart grid cyberattack detection | 50 |
| large language model substation intrusion detection | 50 |
| LLM agent critical infrastructure energy security | 50 |
| large language model electricity market manipulation | 50 |
| ChatGPT cybersecurity power systems | 50 |
| large language model industrial control system anomaly detection energy | 50 |
| trustworthy large language models power systems | 50 |
| LLM hallucination safety power system operation | 50 |

693 unique records; 52 passed the keyword filter and were read at title/abstract level; 23 were added to `evidence_census.csv` (source = OpenAlex journal search). The search targeted security terms. Later final coding nevertheless assigned one added safe-reinforcement-learning record to capability/deployment; that stream has 45 archive records and one OpenAlex journal-search record.

## Publication years of the 472 retrieved archive reports

| Year | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Reports | 2 | 2 | 5 | 5 | 6 | 11 | 2 | 27 | 99 | 177 | 136 |

## Citation chasing (OpenAlex), run 15 October 2026

Seeds (14 core energy-LLM security studies and reviews, matched by title in OpenAlex): Ruan et al. 2023; Li et al. 2024; Hammadia et al. 2026; Sen et al. 2024; Grid-Agent; TwinGridShield; ElecBench; Saber et al. 2026 (protective relays); Zaboli et al. 2023 (ChatGPT for smart-grid cybersecurity); Zaboli et al. 2025 (EMS multimodal anomaly detection); Kong et al. 2026 (ICS detectors); Majumder et al. 2024; Chen et al. 2026 (power-systems security review); Ibrahim and Kashef 2025.
Method: works citing each seed (up to 200) and works referenced by each seed (up to 100) were retrieved; 437 unique works dated 2023 or later; 49 matched LLM, energy and security terms and were new to the collection; 15 were coded into `evidence_census.csv` (source = OpenAlex citation chasing). Capability and deployment papers, generic LLM papers and one likely duplicate version (a conversational-AI substation paper by the same group as an archived record) were not added.
