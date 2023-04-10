Framework for verifying deep neural networks based on SMT solving.

#### Name:
Marabou

#### Application domain/field:
Deep neural networks
Neural network verification

#### Type of tool (e.g. model checker, test generator): 
Neural network verifier

#### Expected input thing:
- Neural network
- Property that should be checked

#### Expected input format:
- *Neural network*: Tensorflow format (.pb file), .nnet format, .onnx file, 
- *Property*: inequality over input and output variables or via the Python interface

#### Expected output:
`SAT` or `UNSAT` indicating whether the network satisfies the property. If it does not satisfy the property then it will provide a counter-example (concrete input) for which the property is violated.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Marabou converts queries about a network into a constraint satisfaction problem.

Marabou supports fully connected feed-forward and convolutional neural networks with piece-wise linear activation functions.

The property/query that should be checked can be one of two types:
- *Reachability queries*: if the input is in a given range, the output will be guaranteed to be in some, typically safe, range.
- *Robustness queries*: test whether there exist adversarial points around a given input point that change the output of the network.

Uses [GLPK](Libraries/GLPK.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/guykatzz/Marabou/
Repository (unsure what the difference is): https://github.com/NeuralNetworkVerification/Marabou
Project page: https://neuralnetworkverification.github.io/

#### Last commit date:
NeuralNetworkVerification/Marabou: 10 Apr 2023 (last activity)
guykatzz/Marabou: 09 Oct 2021 (last activity)

#### Last publication date:
23 March 2021

#### List of related papers:
[The Marabou Framework for Verification and Analysis of Deep Neural Networks](https://doi.org/10.1007/978-3-030-25540-4_26)
[An SMT-Based Approach for Verifying Binarized Neural Networks](https://doi.org/10.1007/978-3-030-72013-1_11)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Neural network
:: DNN
:: PV3 :: checks user-specified properties of deep neural networks
:: Source :: https://doi.org/10.1145/3550355.3552426
