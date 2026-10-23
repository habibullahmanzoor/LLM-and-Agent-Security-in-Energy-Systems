# Evaluation design worksheet

Companion to the survey's claim-to-evidence guide and metric dictionary, draft v0.5.1, 14 October 2026. Copy and fill this form for a proposed study. This is an author-proposed synthesis of the selected literature, not a validated standard, a new benchmark or experimental data. Empty fields below are intentional.

## 1. State the claim and its limits

- Intended claim:
- Demonstrated authority: A0 advice / A1 simulated execution / A2 operational proposal / A3 real execution:
- Intended endpoint: answer / protected-data exposure / authorization / physical constraint / complete trajectory:
- Legitimate task and authorized role:
- Attacker goal, controlled object, insertion point, knowledge and budget:
- Explicitly excluded claims (for example, no physical execution or no confidentiality test):

Choose instruments for the endpoint, not their names. SafeRAG and EnergyAgentBench supply different context manipulations; AgentDojo and InjecAgent supply general tool-attack cases; PowerAgentBench supplies energy workflow or physical checks; TwinGridShield supplies bounded runtime-authorization and mismatch evidence. Retrieval-membership work addresses a different confidentiality endpoint. Recheck the reviewed source and its restrictions in S1 before adaptation. These components have not been integrated or validated by this survey.

## 2. Pin the system and distinguish the oracles

| Item | Fill in |
|---|---|
| Model/API version and access date | |
| Prompts, agent framework, persistent memory and artifact hashes | |
| Tool schemas/server versions, roles and read/write permissions | |
| Data snapshot, provenance, protected items and attacker write access | |
| Task-quality judge and independence from the evaluated agent | |
| Attacker-goal judge and treatment of refusals/aborts | |
| Authorization policy and independent enforcement point | |
| Physical reference: AC/DC/dynamic scope, topology/state/ratings | |
| Checker mismatch and freshness assumptions | |
| Sequence/terminal invariants, recovery and rollback scope | |
| Seeds, repeated runs, task sampling and retry/query/action budgets | |

Authorization and physical admissibility are separate predicates. A physically safe action can still be unauthorized. A released proposal may never execute. A read-only assistant can still disclose protected information.

## 3. Compare matched conditions

Use the same pinned task set and access budgets where feasible. Keep attack optimization separate from the evaluation set and disclose adaptive budgets. Record any unavoidable differences rather than labeling conditions matched.

| Condition | Defense | Attack | Primary purpose |
|---|---|---|---|
| Clean | Off | Absent | Baseline task quality and completion |
| Attacked | Off | Present | Effect of attacker access |
| Defended-clean | On | Absent | Utility cost and false blocks |
| Defended-attacked | On | Present | Protection and residual consequences |

For each condition, record attempted tasks, attack trials, proposed/accepted/released/executed actions, completions, blocks, timeouts and missing outcomes. Retain complete traces. Never silently discard failed runs.

## 4. Predeclare denominators

The accompanying `metric_dictionary.csv` supplies eight proposed operational definitions. Copy only applicable metrics, preserving observation units. Report raw numerator/denominator, uncertainty and aggregation alongside rates; zero-denominator rates are undefined. Identify aborted or unevaluable trials and provide a sensitivity analysis if their classification changes the conclusion.

| Metric | Numerator | Denominator | Oracle/judge | Abort/missing treatment | Uncertainty/aggregation |
|---|---|---|---|---|---|
| Attacker-goal success | | | | | |
| Authorized-task completion | | | | | |
| Unsafe release per attack trial | | | | | |
| Unsafe execution per executed action | | | | | |
| Unsafe-proposal interception | | | | | |
| Safe-proposal false block | | | | | |
| Membership TPR at declared FPR | | | | | |
| Disclosure exposure | | | | | |

Also record task quality, latency, cost, number/sensitivity of disclosed items and severity/duration of physical violations where relevant. A low unsafe-release rate with near-zero completion is not sufficient evidence of useful protection. Membership inference is not equivalent to extraction, and detector accuracy is not agent-level protection.

## 5. Bound the conclusion

- What the evaluated endpoint supports:
- What remains untested (different authority, access, physical model, data distribution or sequence length):
- Failure traces and counterexamples:
- Exact source/benchmark editions and deviations:
- Reusable artifacts, access restrictions and reproducibility instructions:
- Independent reviewer, date and unresolved interpretation questions:

When writing results, cite the original study for its experiment and the survey for the comparison or proposed design guidance actually used. Do not attribute the original experiments to this survey. No study has been run by filling or distributing this blank form.

See `worked_evaluation_example.md` for a filled illustrative design with invented arithmetic; it supplies no experimental results.
