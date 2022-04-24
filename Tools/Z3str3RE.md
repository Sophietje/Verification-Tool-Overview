#### Name:
Z3str3RE: 

#### Application domain/field:
SMT solving
String solvers
Regular expressions

#### Type of tool (e.g. model checker, test generator):
Algorithm for SMT solving

#### Expected input thing:
-

#### Expected input format:
-

#### Expected output:
-

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Implemented as part of [Z3](Solvers/SMT/Z3.md) for solving regex constraints and linear integer arithmetic over length of string terms.

#### Comments:
-

#### URIs (github, websites, etc.):
Artifact/reproduction package for CAV '21 paper: https://figshare.com/s/5ae73a6f3c55f5c5e4c1

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_14 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Other string solvers: [CVC4](Solvers/SMT/CVC4.md), [[OSTRICH]], [[Z3seq]], [[Z3str3]], [[Z3-Trau]]
SMT solvers that support theories over regular expression membership predicate and linear arithmetic over length of strings: [CVC4](Solvers/SMT/CVC4.md), [[Z3str3]], [[Norn]], [[S3P]], [[HAMPI]]

#### Meta
:: SMT
:: PV4 :: part of Z3, produces a satisfiability result for a set of constrains