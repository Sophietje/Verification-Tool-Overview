SAT-based minimizer for Mealy machines

#### Name:
MeMin

#### Application domain/field:
Mealy machines
Minimization

#### Type of tool (e.g. model checker, test generator):
Minimizer for Mealy machines

#### Expected input thing:
Mealy machine

#### Expected input format:
[[KISS2]] format

#### Expected output:
`result.kiss` file describing the minimized Mealy machine.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This tool focuses on minimizing *incompletely specified* Mealy machines (where one or mote outputs or next states might not be specified). 
When it minimized a Mealy machine M, it looks for a machine M' with the minimal number of states with the same input/output behavior on all input sequences for which the behavior of M is defined. M' might be defined on additional input on which M is not defined.

Uses [MiniSat](Solvers/SAT/MiniSat.md).

#### Comments:
**Not published at CAV or TACAS but mentioned in a "Uses" clause of another tool.**

#### URIs (github, websites, etc.):
Project page: http://embedded.cs.uni-saarland.de/MeMin.php
Repository: https://github.com/andreas-abel/MeMin

#### Last commit date:
08 May 2018 (default branch)
08 May 2018 (last activity)

#### Last publication date:
2015

#### List of related papers:
[MEMIN: SAT-based exact minimization of incompletely specified Mealy machines](https://doi.org/10.1109/ICCAD.2015.7372555) (ICCAD)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Automaton
:: PV1 :: minimizes Mealy machines
:: Source :: https://doi.org/10.1145/3550355.3552426
