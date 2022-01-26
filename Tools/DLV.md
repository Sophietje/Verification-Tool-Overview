Framework for automated verification of safety of classification decisions made by feed-forward deep neural networks.

#### Name:
DLV: Deep Learning Verification

#### Application domain/field:
Deep neural networks
Safety verification
Image classification
Adversarial perturbations
Classifiers

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Dataset
- Neural network
- ?

#### Expected input format:
Everything seems to be defined within a python file.

#### Expected output:
The network is verified (i.e. no misclassifications were found for all layers) or it is falsified (i.e. the tool found an adversarial example )

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md), [[Keras]] (neural network library), [[Theano]] (deep learning package).

#### Comments:
License: GNU General Public License v3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/verideep/dlv 

#### Last commit date:
5 February 2018

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63387-9_1 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Neural network
:: DNN