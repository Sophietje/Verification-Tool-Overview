Tool for verifying safety properties of closed-loop systems with NN controllers.

#### Name:
Verisig

#### Application domain/field:
Neural networks
Safety verification

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:

#### Expected input format:

#### Expected output:

#### Internals (tools used, frameworks, techniques, paradigms, ...):
They combine ideas from neural network reachability with ideas from hybrid system verification. They approximate neural networks with Taylor models. Moreover, they note that the reachability computation can be parallelised since each neuron in a layer can be analysed independently.

Uses [Flow\*](Flow*.md)

#### Comments:
The CAV'21 paper refers to a _Verisig 2.0_

License: GPL v3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/Verisig/verisig
CAV '21 artifact: https://github.com/rivapp/CAV21_repeatability_package

#### Last commit date:
verisig: 09 Jun 2021 (default branch)
CAV21_repeatability_package: 27 Apr 2021 (default branch)
09 Jun 2021 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[Verisig 2.0: Verification of Neural Network Controllers Using Taylor Model Preconditioning](https://doi.org/10.1007/978-3-030-81685-8_11) (CAV '21; Verisig 2.0)
[Verisig](https://doi.org/10.1145/3302504.3311806) (HSCC '19)
https://arxiv.org/abs/1811.01828 (arXiv version of the HSCC paper)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '21 paper: [NNV](NNV.md) and [[ReachNN\*]] (and an older version of Verisig)

#### Meta
:: Neural network
:: PV1 :: performs reachability analysis on closed-loop systems with neural network controllers
:: Source :: https://doi.org/10.1007/978-3-030-81685-8 :: https://doi.org/10.1145/3550355.3552426
