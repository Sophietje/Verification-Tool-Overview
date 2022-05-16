Constraint-based technique to repair neural network classifiers

#### Name:
NNRepair

#### Application domain/field:
Neural networks
Neural network classifiers
Program repair
Fault localization
Faulty parameters
Constraint solving

#### Type of tool (e.g. model checker, test generator):
Program (neural network) repair

#### Expected input thing:
- Neural network used for classification
- Positive and negative examples, i.e. dataset for classification

#### Expected input format:
- *Neural network*: Keras model
- *Dataset*: ?

#### Expected output:
Repaired neural network.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
NNRepair targets neural networks used for classification.
First NNrepair uses fault localization to find potentially faulty parameters (weights on edges connecting neurons) in a neural network. Then it performs repair using constraint solving to apply small modifications to the parameters to remedy the defects.

The tool is based on [NeuroSPF](NeuroSPF.md). It uses [Symbolic PathFinder](SPF.md) and [Z3](Solvers/SMT/Z3.md).

#### Comments:
A combination of finding a problem (PV1) and suggesting how it can be solved (PV2)

#### URIs (github, websites, etc.):
Repository (only contains dataset for experiments of the CAV '21 paper, not the tool itself): https://github.com/muhammadusman93/nnrepair

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_1 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Other neural network repair tool: [[MODE]]
Tool to generate adversarial examples: [[DeepFault]]

#### Meta
:: Neural network
:: Program repair
:: PV3 :: repairs neural network classifiers based on examples