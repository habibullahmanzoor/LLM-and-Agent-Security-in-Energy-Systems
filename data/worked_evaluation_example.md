# Worked evaluation example: corrupted line ratings

**Illustrative design and invented arithmetic only. This file contains no experimental results.** Companion to the paper's worked evaluation subsection and `evaluation_worksheet.md`, draft v0.5.1, 14 October 2026.

## Filled design fields

| Field | Illustrative choice |
|---|---|
| Claim | A release gate reduces physically unsafe actions while preserving authorized task completion |
| Authority | A1: sandbox execution; no operational control |
| Legitimate task | Produce and execute one permissible redispatch action satisfying the stated task-quality criteria |
| Attacker control | Replace a numerical line rating in a tool return; no tool-code or permission changes |
| Attacker goal | Release an action violating the independent physical reference |
| Manipulation type | Numerical corruption; no instruction-injection test |
| Authorization oracle | Allowed tool, role and dispatch limits, checked separately from physical safety |
| Physical oracle | Trusted network/state and unmodified ratings; independent of attacker-controlled input |
| Mismatch test | Disclose any shared simplified checker/reference model; compare with an appropriate higher-fidelity reference |
| Matched conditions | Clean, attacked, defended-clean and defended-attacked, with pinned tasks, model, tools, seeds and budgets |
| Untested claims | Confidentiality, live operational safety and complete multi-step trajectories |

The literature supplies relevant components: EnergyAgentBench's numerical value replacement, PowerAgentBench-SS's independent physical checking and TwinGridShield's checker-mismatch question. The survey proposes this combination; those sources do not establish its integrated efficacy. Use the exact editions and source locators in S1 for their original findings.

## Fictional accounting for one defended-attacked condition

Assume one proposal per task, all proposals satisfy the authorization policy, all released actions execute in the sandbox, and no outcomes are missing.

| Quantity | Invented count |
|---|---:|
| Attempted tasks / attack trials / proposals | 100 each |
| Independently unsafe proposals | 20 |
| Independently safe proposals | 80 |
| Unsafe proposals blocked before release | 18 |
| Safe proposals incorrectly blocked | 8 |
| Released and executed actions | 74 |
| Unsafe released/executed actions | 2, in two distinct trials |
| Tasks meeting authorized completion criteria | 70 |

Accounting: 20 + 80 = 100 proposals; 18 + 8 = 26 blocks; 100 - 26 = 74 releases/executions; 20 - 18 = 2 unsafe releases/executions. Task completion is a separately judged outcome, not the count of releases.

| Proposed metric | Calculation from invented counts |
|---|---:|
| Unsafe release per attack trial | 2 / 100 = 2% |
| Unsafe execution per executed action | 2 / 74 ≈ 2.7% |
| Unsafe-proposal interception | 18 / 20 = 90% |
| Safe-proposal false block | 8 / 80 = 10% |
| Authorized-task completion | 70 / 100 = 70% |

Because the attacker goal here is unsafe release, its success rate equals unsafe release per trial by definition. Other attacker goals require their own judge and may produce a different rate.

## What a real study would still need

These single-condition, fictional counts establish no defense effect. A real comparison would fill all four matched conditions, report raw counts and repeated-run uncertainty, examine failure traces, test checker mismatch and account for aborted or unevaluable outcomes. Membership and extraction need separate confidentiality designs.

If every proposal were blocked, unsafe release would be zero, completion of these action-required tasks would be zero, and unsafe execution would be undefined because its denominator is zero. A physically safe but unauthorized proposal should be blocked and should not count as a safe-proposal false block.

Copy the blank worksheet for actual study planning. Do not cite these invented quantities as benchmark measurements, add them to S1/S3 or the numerical claim audit, or infer operational assurance from the example.
