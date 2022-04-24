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
License: GPL v3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/Verisig/verisig
CAV '21 artifact: https://github.com/rivapp/CAV21_repeatability_package

#### Last commit date:
9 June 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_11 (CAV '21)
https://doi.org/10.1145/3302504.3311806 (HSCC '19)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '21 paper: [NNV](NNV.md) and [[ReachNN\*]]

#### Meta
:: Neural network