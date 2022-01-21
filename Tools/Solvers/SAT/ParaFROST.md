SAT solver that uses Conflict Driven Clause Learning (CDCL) with GPU acceleration of pre- and inprocessing, tuned for bounded model checking.

#### Name:
ParaFROST

#### Application domain/field:
SAT solving
Boolean satisfiability

#### Type of tool (e.g. model checker, test generator):
SAT solver

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
`SATISFIABLE`, `UNSATISFIABLE` or an error indicating e.g. out of memory or a timeout.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Based on [[CaDiCaL]], interfaces with [CBMC](../../Checkers/CBMC.md)

#### Comments:
**NOTE**: Although ParaFROST is presented as a parallel SAT solver, it only seems to be available combined with [CBMC](../../Checkers/CBMC.md) and thus it is unclear whether it can be used individually without [CBMC](../../Checkers/CBMC.md)!

License: GPL-3.0

#### URIs (github, websites, etc.):
Project page: https://gears.win.tue.nl/software/gpu4bmc
Repository: https://github.com/muhos/gpu4bmc

#### Last commit date:
3 June 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_21 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to (in CAV '21 paper): [MiniSat](MiniSat.md), [Glucose](Glucose.md), [[CaDiCaL]]

#### Meta
:: SAT
:: PV4 :: produces a satisfiability result for a formula