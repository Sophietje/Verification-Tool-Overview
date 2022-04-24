SMT solver that can compute Craig interpolants for various theories

#### Name:
SMTInterpol

#### Application domain/field:
SMT solving

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SMT formula

#### Expected input format:
[SMT-LIB](../../../Formats/SMT-LIB.md) v2.6
It supports Craig interpolation via an extension of the SMT-LIB format.

#### Expected output:
`sat`, `unsat` or `unknown`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It supports the combination of the theories of uninterpreted functions, linear real arithmetic, linear integer arithmetic, arrays including constant arrays, and datatypes. It supports quantifiers for all supported theories except for datatypes. It supports interpolation for the quantifier-free fragments of all supported theories except datatypes.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://ultimate.informatik.uni-freiburg.de/smtinterpol/
Try online: https://ultimate.informatik.uni-freiburg.de/smtinterpol/online/
Repository: https://github.com/ultimate-pa/smtinterpol

#### Last commit date:
22 September 2021

#### Last publication date:
12 January 2021

#### List of related papers:
https://doi.org/10.1007/978-3-642-36742-7_9 (TACAS '13)
https://doi.org/10.1007/978-3-319-21668-3_3 (CAV '15)
https://doi.org/10.1007/978-3-030-67067-2_24 (VMCAI '21)
See also: https://ultimate.informatik.uni-freiburg.de/smtinterpol/publications.html

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: SMT
:: PV5 :: produces a satisfiability result for a formula