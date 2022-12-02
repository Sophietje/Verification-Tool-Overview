Framework for quantitative analysis of BNNs (binarized neural networks).

#### Name:
BDD4BNN

#### Application domain/field:
Binarized Neural Networks (BNNs)
Binary Decision Diagrams (BDDs)
Quantitative analysis

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Binarized Neural Network (BNN)
- Region R

#### Expected input format:
?

#### Expected output:
BDD that encodes the input-output relation of the binarized neural network in the region R.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It encodes a BNN and the associated input region into BDDs.
Uses [CUDD](CUDD.md)

#### Comments:
The tool is called a "prototype tool" in the CAV '21 paper.

#### URIs (github, websites, etc.):
*Cannot find a repository or download link*

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
[BDD4BNN: A BDD-Based Quantitative Analysis Framework for Binarized Neural Networks](https://doi.org/10.1007/978-3-030-81685-8_8) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Library
:: BDD
:: PV1 :: encodes a binarized neural network and input region into a BDD
:: Source :: https://doi.org/10.1007/978-3-030-81685-8 :: https://doi.org/10.1145/3550355.3552426
