#### Name:
cvc4sy

#### Application domain/field:
Syntax-guided synthesis (SyGuS) solver
SMT solving

#### Type of tool (e.g. model checker, test generator):
SyGuS solver

#### Expected input thing:
SyGuS problem

#### Expected input format:
[SyGuS](../../Formats/SyGuS.md) input format

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
cvc4sy is integrated in [CVC4](SMT/CVC4.md).
cvc4sy is based on counterexample-guided inductive synthesis (CEGIS).

#### Comments:
This solver specifically aims to prove unsatisfiability of formulae like: $\forall f \exists \bar{x}. \neg P[f,\bar{x}]$

#### URIs (github, websites, etc.):
CVC4 repository: https://github.com/CVC4/CVC4-archived/

#### Last commit date:
06 May 2021

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25543-5_5

#### Related tools (tools mentioned or compared to in the paper):
Other SyGuS solver: [[EUSolver]]

#### Meta
:: SyGuS
:: SAT
:: PV4 :: proves unsatisfiability of a narrow class of formulae with counterexample-guided inductive synthesis