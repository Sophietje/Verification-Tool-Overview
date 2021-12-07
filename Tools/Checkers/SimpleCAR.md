Safety hardware model checker
Tool specifically for evaluating and extending the CAR (Complementary Approximate Reachability) framework. It can be used for unsafety checking, or bug-finding.

#### Name:
SimpleCAR

#### Application domain/field:
Model checking
Hardware model checking
Safety verification

#### Type of tool (e.g. model checker, test generator):
Hardware model checker

#### Expected input thing:
Hardware circuit model expressed as And-Inverter Graphs containing a single safety property

#### Expected input format:
[AIGER](../../Formats/AIGER.md) 1.9

#### Expected output:
0 (`SAFE`), 1(`UNSAFE`)
SimpleCar can also generate a counterexample if run with the option `-e`.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Glucose](../Solvers/SAT/Glucose.md) as underlying SAT solver, [AIGER](../../Formats/AIGER.md) for parsing and error checking.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/lijwen2748/simplecar/
Project page: http://temporallogic.org/research/CAV18/

#### Last commit date:
21 December 2020

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_5 (CAV '18)
https://doi.org/10.1007/978-3-030-41600-3_12 (VSTTE '19)

#### Related tools (tools mentioned or compared to in the paper):
SimpleCAR is a rewrite of [[CARChecker]].
