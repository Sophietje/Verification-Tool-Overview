#### Name:
nnenum: The Neural Network Enumeration Tool

#### Application domain/field:
Neural networks
Neural network verification

#### Type of tool (e.g. model checker, test generator):
Neural network verifier

#### Expected input thing:
- Neural network
- Input set
- Unsafe set
?

#### Expected input format:
?

#### Expected output:
`safe` or `unsafe`. 
For neural networks this means that they check whether the output of the neural network (for a given input set) overlaps with the provided unsafe set. If they do not overlap, then the network is considered `safe`.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
nnenum focuses on the verification of fully-connected, feedforward neural networks with ReLU activation functions.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/stanleybak/nnenum

#### Last commit date:
15 June 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_4 (CAV 2020)

#### Related tools (tools mentioned or compared to in the paper):
Other tools for the verification of neural networks: [Marabou](Marabou.md), [[Neurify]], [NNV](NNV.md).

#### Meta
:: Neural network
:: PV1 :: given an unsafe set an a neural network, checks whether the set overlaps with the output of the network