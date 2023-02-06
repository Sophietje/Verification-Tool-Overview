
#### Name:
Trainify

#### Application domain/field:
Deep reinforcement learning
Counterexample-guided abstraction refinement (CEGAR)
Model checking

#### Type of tool (e.g. model checker, test generator):
Framework for training & verification of deep reinforcement learning systems

#### Expected input thing:
- Deep neural network
- Properties in ACTL (segment of CTL where only universal path quantifiers are allowed and negation can only be used on atomic propositions)

#### Expected input format:
? (seems to all be hardcoded in Python)

#### Expected output:
Whether the property holds or not.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The tool builds a finite abstract state space using the trained neural network.

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/aptx4869tjx/RL_verification

#### Last commit date:
16 June 2022

#### Last publication date:
7 August 2022

#### List of related papers:
[TRAINIFY: A CEGAR-Driven Training and Verification Framework for Safe Deep Reinforcement Learning](https://doi.org/10.1007/978-3-031-13185-1_10) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Model checking
:: DNN
:: PV3 :: checks properties of a deep reinforcement learning systems
:: Source :: https://doi.org/10.1007/978-3-031-13185-1