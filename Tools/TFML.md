Tool to generate models of quantified first-order formula over built-in theories

#### Name:
TFML: Taint engine for ForMuLa

#### Application domain/field:
SMT solving
Quantified formula
Model generation
Quantifier elimination

#### Type of tool (e.g. model checker, test generator):
Meta-tool?

#### Expected input thing:
Quantified SMT formula

#### Expected input format:
[SMT-LIB](../Formats/SMT-LIB.md) (ABV, arrays and bitvectors, theory)

#### Expected output:
SMT-LIB formula

#### Internals (tools used, frameworks, techniques, paradigms, ...):
They focus on the problem to generate models (i.e. find solutions) of an SMT formula.
Given a quantified formula, they transform it into a quantifier-free formula with the guarantee that any model of the latter contains a model of the former.

#### Comments:
License: GNU LGPL v2.1

#### URIs (github, websites, etc.):
Project page: https://benjamin.farinier.org/cav2018/
Repository: https://github.com/binsec/tfml

#### Last commit date:
27 August 2018

#### Last publication date:
18 July 2018

#### List of related papers:
[Model Generation for Quantified Formulas: A Taint-Based Approach](https://doi.org/10.1007/978-3-319-96142-2_19) (CAV 2018)

#### Related tools (tools mentioned or compared to in the paper):
[BINSEC](BINSEC.md)

#### Meta
:: PV2 :: generates a quantifier-free formula overapproximating a given quantified formula
:: SMT