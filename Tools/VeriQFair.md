
#### Name:
VeriQFair

#### Application domain/field:
Machine learning
Quantum machine learning
Fairness

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Quantum decision model
- Qubits (all qubits used in the model)
- Measurement (single qubit measurement)

#### Expected input format:
The 'tool' can be imported in Python. One should then pass the inputs as parameters to a library call.
- Quantum decision model: defined using Cirq (library for representing quantum circuits)
- Qubits: defined using Cirq
- Measurement: numpy array

#### Expected output:
Lipschitz constant

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This tool can be used to compute the Lipschitz constant of a quantum decision model. This constant can be used to determine fairness for a quantum decision model. Specifically, they focus on individual fairness, i.e. "treating similar individuals similarly".

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/Veri-Q/Fairness

#### Last commit date:
4 June 2022

#### Last publication date:
6 August 2022

#### List of related papers:
[Verifying Fairness in Quantum Machine Learning](https://doi.org/10.1007/978-3-031-13188-2_20) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV1 :: computes the Lipschitz constant of a quantum decision model
:: Source :: https://doi.org/10.1007/978-3-031-13188-2
