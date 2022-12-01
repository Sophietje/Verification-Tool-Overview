#### Name:
Yices

#### Application domain/field:
SMT solving
SMT (Satisfiability Modulo Theories)

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SMT formula

#### Expected input format:
[SMT-LIB](../../../Formats/SMT-LIB.md)(version 1.2 and 2.0), or its own specification language.

It also has a C API and bindings for Java, Python, Go and OCaml.

#### Expected output:
`sat` if the problem is satisfiable, `unsat` if it is not satisfiable or `unknown` if the solver does not terminate within a fixed number of iterations.

If the formula can be satisfied, then you can ask Yices for a satisfying model.

#### Internals (tools used, frameworks, techniques, paradigms, ...):

#### Comments:
License: GPLv3

#### URIs (github, websites, etc.):
Project page: https://yices.csl.sri.com/
Repository: https://github.com/SRI-CSL/yices2

#### Last commit date:
25 Nov 2022 (default branch)
25 Nov 2022 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[Interpolation and Model Checking for Nonlinear Arithmetic](https://doi.org/10.1007/978-3-030-81688-9_13) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: SMT
:: PV4 :: produces a satisfiability result for a formula
