#### Name:
SyReNN: Symbolic Representation for Neural Networks

#### Application domain/field:
Deep neural networks (DNNs)
Adversarial attacks
Symbolic representation

#### Type of tool (e.g. model checker, test generator): 
Library for analyzing DNNs

#### Expected input thing:
- Piecewise-linear DNN (Deep Neural Network)
- X: union of one- or two-dimensional polytopes

#### Expected input format:
- *DNN*: [ERAN](Formats/ERAN.md) or [ONNX](ONNX.md)
- *X*: list of its vertices in counter-clockwise order

#### Expected output:
Symbolic representation $\widehat{f_{\upharpoonright X}}$

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Computes a symbolic representation that decomposes the behavior of a DNN into finitely-many linear functions.

A DNN is piecewise-linear if its input domain can be precisely partitioned into finitely-many linear functions.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/95616ARG/SyReNN

#### Last commit date:
10 Sep 2021 (default branch)
22 Nov 2022 (last activity)

#### Last publication date:
2021

#### List of related papers:
[SyReNN: A Tool for Analyzing Deep Neural Networks](https://doi.org/10.1007/978-3-030-72013-1_15) (TACAS '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: DNN
:: Library
:: PV1 :: computes a symbolic representation of a neural network as linear functions
:: Source :: https://doi.org/10.1007/978-3-030-72013-1 :: https://doi.org/10.1145/3550355.3552426
