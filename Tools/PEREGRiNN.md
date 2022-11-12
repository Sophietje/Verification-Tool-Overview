A tool to formally verifying the input/output behavior or ReLU neural networks.

#### Name:
PEREGRiNN: Penalized-Relaxation Greedy Neural Network Verifier
Sometimes stylized as PeregriNN.

#### Application domain/field:
Neural networks
Model checking
Safety verification
Input-output behavior
Adversarial inputs

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Rectified Linear Unit (ReLU) neural network
- Image file
- Max-norm perturbation $\epsilon$

#### Expected input format:
- *Neural network*: `nnet` format
- Comma-separated file that describes each pixel as a float between 0 and 1
- *Max-norm perturbation*: passed when calling the script, e.g. `0.02`.

#### Expected output:
Proves whether a particular input image always results in the same classification when it is subjected to a max-norm perturbation of at most some fixed size $\epsilon$.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Gurobi](Solvers/Gurobi.md) 9.1 convex optimizer for solving linear programs, [[Volesti]] to sample from the input polytope for the sampling inference block

#### Comments:
License: MIT, however it relies on [[Gurobi]] which is a commercial tool. It is possible to get an academic license for Gurobi.

#### URIs (github, websites, etc.):
Repository: https://github.com/rcpsl/PeregriNN

#### Last commit date:
09 Jul 2022

#### Last publication date:
15 July 2021

#### List of related papers:
[PEREGRiNN: Penalized-Relaxation Greedy Neural Network Verifier](https://doi.org/10.1007/978-3-030-81685-8_13) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '21 paper: [[Neurify]], [[Venus]], [nnenum](nnenum.md), [Marabou](Marabou.md)

#### Meta
:: Neural network
:: PV1 :: checks whether an image is always classified the same when it's perturbed