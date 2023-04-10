An analyzer based on abstract interpretation for verification of MNIST, CIFAR10, and ACAS Xu based networks.

#### Name:
ERAN: ETH Robustness Analyzer for Neural Networks

#### Application domain/field:
Neural networks
Abstract interpretation
Safety properties

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Neural network
- Dataset
- Lots of parameters, depending on what analysis you want to run.

#### Expected input format:
- *Neural network*: [ONNX](../Formats/ONNX.md)
- *Dataset*: Argument passed to ERAN. It has `mnist`, `acasxu`, `cifar10`

#### Expected output:
Depends on the analysis that is run.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Has its own [ERAN language](../Formats/ERAN%20language.md)

#### Comments:
License: Apache-2.0

#### URIs (github, websites, etc.):
Repository: https://github.com/eth-sri/eran

#### Last commit date:
27 Jan 2023 (last activity)

#### Last publication date:
2021

#### List of related papers:
[PRIMA: general and precise neural network certification via scalable convex hull approximations](https://doi.org/10.1145/3498704) (POPL 2022)
https://files.sri.inf.ethz.ch/website/papers/mueller2021precise.pdf (open version of POPL 2022)
https://proceedings.mlsys.org/paper/2021/file/ca46c1b9512a7a8315fa3c5a946e8265-Paper.pdf (MLSys '21)
https://arxiv.org/abs/2009.09318 (AAAI '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Neural network
:: PV3 :: verifies safety properties of neural networks against input perturbations
:: Source :: https://doi.org/10.1145/3550355.3552426
