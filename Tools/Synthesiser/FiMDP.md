#### Name:
FiMDP: Fuel in MDP

#### Application domain/field:
Strategy synthesis
Controller synthesis
Resource-constrained systems
Probabilistic systems

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
- a Consumption Markov Decision Process
- Capacity $cap$
- Set of accepting states $T$

#### Expected input format:
- *CMDP*: either as a [PRISM](../Checkers/PRISM.md) model, [Storm](../Checkers/Storm.md) model, or it can be constructed in Python.
- $cap$: passed as an argument when calling the algorithm in Python
- $T$: passed as an argument when calling the algorithm in Python

#### Expected output:
If it exists, then it returns a strategy $\sigma$ such that when starting with resource level $d$, the resource level never drops below 0 and the system infinitely often visits some state in $T$

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This technique focuses on synthesizing controllers for resource-constrained Markov decision processes (MDPs). This controller must ensure that (1) some linear-time property is satisfied and (2) that the system's operation is not compromised by lack of resources (e.g. power). Consumption Markov Decision Processes (CMDPs) are used to represent the resource-constrained MDPs.

#### Comments:

#### URIs (github, websites, etc.):
Repository: 
https://github.com/FiMDP/FiMDP

#### Last commit date:
11 Nov 2021 (default branch)
16 Aug 2022 (last activity)

#### Last publication date:
14 July 2020

#### List of related papers:
[Qualitative Controller Synthesis for Consumption Markov Decision Processes](https://doi.org/10.1007/978-3-030-53291-8_22)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Synthesis
:: PV2 :: synthesises a controller for a resource-constrained Markov Decision Process
:: Source :: https://doi.org/10.1145/3550355.3552426
