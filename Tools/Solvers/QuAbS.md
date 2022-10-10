Solver for quantified Booelan formulas (QBF) based on a CEGAR-based abstraction algorithm

#### Name:
QuAbS: Quantified Abstraction Solver

#### Application domain/field:
Quantified Boolean formula (QBF)
Counterexample guided abstraction refinement (CEGAR)
QBF satisfiability
Satisfiability solving

#### Type of tool (e.g. model checker, test generator):
Satisfiability solver

#### Expected input thing:
Quantified boolean formula

#### Expected input format:
[[QCIR]] (quantified circuit) format.

#### Expected output:
`r SAT` or `r UNSAT`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
There is also a prototype that has been parallelized, which is referred to as PQUABS in the SAT '16 paper.

They provide a conversion from QCIR to [QAIGER](../../Formats/QAIGER.md)

#### URIs (github, websites, etc.):
Project page: https://www.react.uni-saarland.de/tools/quabs/
Repository: https://github.com/ltentrup/quabs

#### Last commit date:
24 October 2020

#### Last publication date:
2018

#### List of related papers:
[Solving QBF by Abstraction](https://doi.org/10.4204/EPTCS.277.7) (GandALF '18)
[Non-prenex QBF Solving Using Abstraction](https://doi.org/10.1007/978-3-319-40970-2_24) (SAT '16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: QBF
:: PV4 :: produces a satisfiability result for a quantified boolean formula