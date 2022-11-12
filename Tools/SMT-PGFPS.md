SMT-PGFPS
#### Name:

#### Application domain/field:
Preliminary Safety Assessment (PSA)
Failure propagations
Minimal cut sets
Safety-critical systems

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [MathSAT](Solvers/SMT/MathSAT.md)

They proposed a framework called: PGFDS (Propagation Graphs over Finite Degradation Structures). This framework allows to model non-deterministic and cyclic propagation graphs.

#### Comments:
-

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
[Efficient SMT-Based Analysis of Failure Propagation](https://doi.org/10.1007/978-3-030-81688-9_10) (CAV 2021)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in the CAV '21 paper: [xSAP](xSAP.md), [[Emmy]]

#### Meta:
:: PV2 :: computes a minimal cut set of a hypergraph
:: Source :: https://doi.org/10.1145/3550355.3552426