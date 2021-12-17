Set-based verification framework for deep neural networks (DNNs) and learning-enabled cyber-physical systems (CPS).

#### Name:
NNV: Neural Network Verification

#### Application domain/field:
Neural network
Deep neural networks
Neural network verification

#### Type of tool (e.g. model checker, test generator):
Neural network verifier

#### Expected input thing:
- Network configuration
- Plant configuration

#### Expected input format:
? (it is a toolbox for Matlab)

#### Expected output:
`SAT` or `UNSAT` which indicates whether the network is safe, i.e. the reachable sets do not violate any of the safety properties. 
If the network is unsafe then it will provide a complete set of counter-examples that show all possible unsafe initial inputs and states.

It is possible for the tool to report `UNK` in case the result is unknown.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
NNV consists of a set of reachability algorithms that can be used to reason about deep neural networks (DNNs), specifically for *sequential* FFNNs (feed forward neural networks) and CNNs (convolutional neural networks), as well as NNCS (neural network control systems) with FFNN controllers. 
These reachability algorithms can be used to compute exact and over-approximate reachable sets of DNNs and neural network control systems (NNCSs).

Uses [[MPT]], [[CORA]], [NNMT](NNMT.md), [[HyST]], [[YALMIP]], [[MatConvNet]]

#### Comments:
The repository calls it a "Matlab Toolbox for Neural Network Verification". It requires the user to install Matlab and use it from within Matlab.

#### URIs (github, websites, etc.):
Repository: https://github.com/verivital/nnv

#### Last commit date:
20 July 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_2
https://doi.org/10.1007/978-3-030-53288-8_1

#### Related tools (tools mentioned or compared to in the paper):
Other tools for neural network verification: [Reluplex](Solvers/SMT/Reluplex.md), [Marabou](Marabou.md) and [ReluVal](ReluVal).