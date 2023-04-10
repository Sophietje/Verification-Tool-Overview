#### Name:
RINO

#### Application domain/field:
Neural network
Reachability
Neural network verification

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Open-loop or closed loop system, can be discrete or continuous-time
- *Optional*: Neural network which can be used as some inputs of the closed-loop system
- *Optional*: Configuration file to set initial values, input, and disturbances ranges, and parameters of the analysis

#### Expected input format:
- *System*: C++
- *Neural network*: format inspired by the format used by [[Sherlock]]
- *Configuration file*: ?

#### Expected output:
Computes inner and outer approximations of reachable sets.

Inner and outer-approximations of the projection on each component of ranges, and joint 2D and 3D inner-approximations.
It also computes approximations of output ranges that are reachable robustly or adversarially w.r.t. disturbances, specified as a subset of inputs.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [[FILIB++]] library for interval computations, [[aaflib]] library for affine arithmetic and [[FADBAD++]] library for automatic differentiation.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/cosynus-lix/RINO

#### Last commit date:
22 September 2022
22 Sep 2022 (last activity)

#### Last publication date:
7 August 2022

#### List of related papers:
[RINO: Robust INner and Outer Approximated Reachability of Neural Networks Controlled Systems](https://doi.org/10.1007/978-3-031-13185-1_25) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Other tools that focus on reachability analysis of neural network controlled systems with smooth activation functions: [[Sherlock]], [Flow*](../../Tools/Flow*.md), [NNV](../../Tools/NNV.md), [[ReachNN]], [[ReachNN*]], [Verisig](../../Tools/Verisig.md), [[JuliaReach]], [[POLAR]].

#### Meta
:: Neural network
:: PV1 :: Computes reachable sets for dynamical systems
:: Source :: https://doi.org/10.1007/978-3-031-13185-1
