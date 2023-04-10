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

License: GPL-3.0

#### URIs (github, websites, etc.):
Project page: https://gears.win.tue.nl/software/gpu4bmc
ParaFROST Repository: https://github.com/muhos/ParaFROST
CBMC Interface Repository: https://github.com/muhos/gpu4bmc

#### Last commit date:
muhos/gpu4bmc: 14 Mar 2022 (last activity)
muhos/ParaFROST: 29 Mar 2023 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[SAT Solving with GPU Accelerated Inprocessing](https://doi.org/10.1007/978-3-030-72016-2_8) (TACAS '21)
[GPU Acceleration of Bounded Model Checking with ParaFROST](https://doi.org/10.1007/978-3-030-81688-9_21) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to (in CAV '21 paper): [MiniSat](MiniSat.md), [Glucose](Glucose.md), [[CaDiCaL]]

#### Meta
:: SAT
:: PV4 :: produces a satisfiability result for a formula
:: Source :: https://github.com/Sophietje/Verification-Tool-Overview/pull/3 :: https://doi.org/10.1145/3550355.3552426
