SMT solver, decides satisfiability of *quantified* bit-vector formulas.

#### Name:
Q3B

#### Application domain/field:
SMT solving
Quantified bit-vector formulas
Binary Decision Diagrams (BDDs)

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
Quantified bit-vector formula

#### Expected input format:
[SMT-LIB](SMT-LIB) 2.5

#### Expected output:
`sat` or `unsat` indicating whether the quantified bit-vector formula was satisfiable or not.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [CUDD](../../Libraries/CUDD.md), [ANTLR](../../Not-verifiers/ANTLR.md), [SMT-LIB](../../../Formats/SMT-LIB.md), [Z3](Z3.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/martinjonas/Q3B

#### Last commit date:
6 March 2019

#### Last publication date:
12 July 2019

#### List of related papers:
[Q3B: An Efficient BDD-based SMT Solver for Quantified Bit-Vectors](https://doi.org/10.1007/978-3-030-25543-5_4)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: SMT
:: BDD
:: PV4 :: produces a satisfiability result for a formula
:: Source :: https://doi.org/10.1007/978-3-030-25543-5 :: https://doi.org/10.1145/3550355.3552426
