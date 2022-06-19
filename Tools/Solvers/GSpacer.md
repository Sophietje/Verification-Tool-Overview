#### Name:
GSpacer

#### Application domain/field:
SMT solving
CHC solving

#### Type of tool (e.g. model checker, test generator):
CHC solver

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
`safe` (and an inductive invariant so that the system can be proven to be safe) or `unsafe`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Extension of [Spacer](Spacer.md), a CHC (Constrained Horn Clause) solver in [Z3](SMT/Z3.md), with global guidance (to tackle limitations of locality).

#### Comments:

#### URIs (github, websites, etc.):
Repository: https://github.com/hgvk94/z3/tree/gspacer-cav-ae

#### Last commit date:
19 December 2019

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53291-8_7

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: CHC
:: SMT
:: PV4 :: produces a satisfiability result for a given CHC
