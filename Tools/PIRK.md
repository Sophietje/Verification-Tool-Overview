Tool to efficiently compute reachable sets for general nonlinear systems of extremely high dimensions

#### Name:
PIRK: Parallel Interval Reachability Kernel

#### Application domain/field:
Reachability analysis
Nonlinear systems
Dynamical systems
Parallelism

#### Type of tool (e.g. model checker, test generator):
Reachability analysis tool

#### Expected input thing:
- Configuration file
- Dynamic system
- Initial hyper-interval for states and inputs

#### Expected input format:
- *Configuration file*: `.cfg` file
- *Dynamical system*: `.cl` file
- *Initial hyper-interval*: `.cl` file
The README of the repository describes the expected syntax for each of these files.

#### Expected output:
`.raw` file which contains the reach pipe of the system

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses the acceleration system [pFaces](pFaces).

#### Comments:
There is a **Matlab-interface** so that users can load/use files generated from PIRK.

From the CAV 2020 paper (emphasis our own): "To the best of our knowledge, PIRK is the first and the only tool that can compute reachable sets of general non-linear systems with **dimensions beyond the billion**."

#### URIs (github, websites, etc.):
https://github.com/mkhaled87/pFaces-PIRK

#### Last commit date:
3 June 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_27

#### Related tools (tools mentioned or compared to in the paper):
Other reachability analysis tools: [C2E2](C2E2), [CORA](CORA), [Flow*](Flow*), [Isabelle](Isabelle), [SpaceEx](SpaceEx), [SymReach](SymReach)