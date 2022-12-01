Verifier for recurrent neural networks (RNNs).

#### Name:
PROVER: Polyhedral Robustness Verifier of RNNs

#### Application domain/field:
Recurrent neural networks (RNNs)
Robustness verification
Adversarial perturbations

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The goal of PROVER is to establish the robustness of recurrent neural networks against noise-induced perturbations. They specifically focus on Long Short-Term Memory (LSTMs).

Uses [Gurobi](Solvers/Gurobi.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/eth-sri/prover

#### Last commit date:
29 Jun 2021 (default branch)
29 Jun 2021 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[Scalable Polyhedral Verification of Recurrent Neural Networks](https://doi.org/10.1007/978-3-030-81685-8_10) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
[[POPQORN]]

#### Meta
::  Neural network
:: PV1 :: runs 100 tests through a neural network, testing its noise robustness
:: Source :: https://doi.org/10.1145/3550355.3552426
