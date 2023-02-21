
#### Name:
MoGym

#### Application domain/field:
Statistical model checking
Decision-making agents
Reinforcement learning

#### Type of tool (e.g. model checker, test generator):
Framework?

#### Expected input thing:
- Formal representation of a decision-making problem
- Reach-avoid objective

#### Expected input format:
[JANI](../../Formats/JANI.md)

#### Expected output:
Trained decision-making agent.
The trained agent can be verified w.r.t. reach-avoid objectives.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses a variant of [modes](../../Tools/Checkers/modes.md) for statistical model checking. This variant has been extended with new resolution strategies for non-determinism.

Based on [[Momba]]

#### Comments:
-

#### URIs (github, websites, etc.):
- Additional information about Momba Gym API: https://momba.dev/gym/.
- Artifact: https://doi.org/10.5281/zenodo.6510840
- Repository: https://github.com/koehlma/momba

#### Last commit date:
28 November 2022

#### Last publication date:
6 August 2022

#### List of related papers:
[MoGym: Using Formal Models for Training and Verifying Decision-making Agents](https://doi.org/10.1007/978-3-031-13188-2_21) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Probabilistic
:: Model checking
:: PV4 :: verifies reach-avoid objective for trained decision-making agent
:: Source :: https://doi.org/10.1007/978-3-031-13188-2