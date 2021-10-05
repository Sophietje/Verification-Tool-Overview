#### Name:
dReal

#### Application domain/field:
SMT solving

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SMT formula

#### Expected input format:
[[SMT-LIB]] v2

#### Expected output:
"unsat" or "$\delta$-sat"

#### Internals (tools used, frameworks, techniques, paradigms, ...):
dReal focuses on formulas over *real* numbers. "Its special strength is in handling problems that involve a wide range of nonlinear real functions." ([Source](https://dreal.github.io/))
It can handle $\exists\forall$-formulas with most standard elementary, trigonometric and hyberbolic functions (e.g. power, exp, log, root, sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh), etc. 

It uses [[IBEX-lib]], [[CLP]], [[NLopt]], [[PicoSAT]] and [[capd]]

#### Comments:

#### URIs (github, websites, etc.):
Project page: https://dreal.github.io/
Repository: https://github.com/dreal/dreal4/
Collection of related repositories: https://github.com/dreal/

#### Last commit date:
4 June 2021

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_15

#### Related tools (tools mentioned or compared to in the paper):