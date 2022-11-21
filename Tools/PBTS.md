Tool to compute Piecewise Barrier Tubes (PBTs) automatically

#### Name:
PBTS: Piecewise Barrier Tube Solver

#### Application domain/field:
Nonlinear continuous systems
Hybrid systems
Nonlinear ordinary differential equations

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Dynamics of the system $M$
- Initial set $X_0$
- Length of piecewise barrier tube $N$
- ?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
PBTs (Piecewise barrier tubers) are used to over-approximate the flowpipe of nonlinear systems. These are used for safety verification of hybrid systems.

Uses [Gurobi](Solvers/Gurobi.md) (linear programming solver).

#### Comments:
-

#### URIs (github, websites, etc.):
?

#### Last commit date:
?

#### Last publication date:
18 July 2018

#### List of related papers:
[Reachable Set Over-Approximation for Nonlinear Systems Using Piecewise Barrier Tubes](https://doi.org/10.1007/978-3-319-96145-3_24) (CAV 2018)

#### Related tools (tools mentioned or compared to in the paper):
[[CORA]], [[Flow\*]]

#### Meta
:: Hybrid system
:: PV2 :: compute piecewise barrier tubes configuration from a system spec
:: Source :: https://doi.org/10.1145/3550355.3552426