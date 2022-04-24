SMT solver for  theory of linear real arithmetic with ReLU constraints.
ReLU (Rectified Linear Unit), are a specific kind of activation function used in deep neural networks (DNNs).

#### Name:
Reluplex

#### Application domain/field:
Neural networks
Deep neural networks (DNNs)
Activation functions
SMT solving

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
`SAT`, `UNSAT` or `TIMEOUT`
`UNSAT` indicates that a property holds, `SAT` indicates that the property does not hold. 

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Verifying DNNs is difficult because it is beyond the reach of general-purpose tools such as linear programming and SMT solvers. Therefore they focus on making an SMT solver that can deal with DNNs. Specifically, they focus on DNNs with a specific kind of activation function called Rectified Linear Unit (ReLU).

#### Comments:
**Note**: The repository of Reluplex is no longer maintained, nowadays the algorithm is implemented in [Marabou](../../Marabou.md)

#### URIs (github, websites, etc.):
Artifact of CAV '17 paper: https://github.com/guykatzz/ReluplexCav2017

#### Last commit date:
8 July 2020

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63387-9_5 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
Other solvers: [CVC4](CVC4.md), [Z3](Z3.md), [Yices](Yices.md), [MathSAT](MathSAT.md), [Gurobi](../Gurobi.md).

Other tools that focus on the verification of neural networks: [NNV](../../NNV.md), [Marabou](../../Marabou.md), [[ReluVal]]

#### Meta
:: SMT
:: DNN
:: Neural network
:: PV5 :: produces a satisfiability result for a formula