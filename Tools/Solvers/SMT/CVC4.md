#### Name:
CVC4

#### Application domain/field:
SMT solving

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SMT formula

#### Expected input format:
One of the following:
- CVC4 native input language
- [SMT-LIB](../../../Formats/SMT-LIB.md) (v2)
- SyGuS-IF
- TPTP

#### Expected output:
`sat` or `unsat` which indicates whether the SMT formula was satisfiable or not.

#### Internals (tools used, frameworks, techniques, paradigms, ...):

#### Comments:
CVC4 is now **succeeded by** [cvc5](cvc5.md).

#### URIs (github, websites, etc.):
Repository: https://github.com/CVC4/CVC4-archived
Project page: https://cvc4.github.io/

#### Last commit date:
6 May 2021

#### Last publication date:
12 July 2019

#### List of related papers:
[High-Level Abstractions for Simplifying Extended String Constraints in SMT](https://doi.org/10.1007/978-3-030-25543-5_2) (CAV '19)
[Solving Quantified Bit-Vectors Using Invertibility Conditions](https://doi.org/10.1007/978-3-319-96142-2_16) (CAV '18)
[Scaling Up DPLL(T) String Solvers Using Context-Dependent Simplification](https://doi.org/10.1007/978-3-319-63390-9_24) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
Predecessors: [[CVC]], [[CVC Lite]], [[CVC3]].
Successor: [cvc5](cvc5.md)

#### Meta
:: SMT
:: PV4 :: produces a satisfiability result for a formula