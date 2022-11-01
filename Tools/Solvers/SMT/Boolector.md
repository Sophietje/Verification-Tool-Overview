#### Name:
Boolector

#### Application domain/field:
SMT solving

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SMT formula

#### Expected input format:
One of the following:
- [BTOR](../../../Formats/BTOR.md)/[BTOR2](../../../Formats/BTOR2.md) (its own formats)
- [SMT-LIB](../../../Formats/SMT-LIB.md) (version 1.2 or 2.0)

#### Expected output:
- If `satisfiable` then it can print a model (if model generation is enabled) or query assignments of bit vector and array variables or uninterpreted functions.
- Else `unsatisfiable` 

#### Internals (tools used, frameworks, techniques, paradigms, ...):

#### Comments:
This is an SMT solver for the theories of fixed-size bit-vectors, arrays and uninterpreted functions.

It has a C and Python API.

#### URIs (github, websites, etc.):
Repository: https://github.com/Boolector/boolector
Project page: https://boolector.github.io/
Documentation: https://boolector.github.io/docs/index.html

#### Last commit date:
27 May 2021

#### Last publication date:
July 2019

#### List of related papers:
[Btor2 , BtorMC and Boolector 3.0](https://doi.org/10.1007/978-3-319-96145-3_32)
[null](https://doi.org/10.35011/fmvtr.2016-1)
[Boolector 2.0](https://doi.org/10.3233/SAT190101)

#### Related tools (tools mentioned or compared to in the paper):
[[Bitwuzla]] is a successor

#### Meta
:: SMT
:: PV4 :: produces a satisfiability result for a formula