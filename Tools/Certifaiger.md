Tool suite for certification of model checking results, independent of any model checker

#### Name:
Certifaiger

#### Application domain/field:
Model checking
Proof certificates
Proof checker

#### Type of tool (e.g. model checker, test generator):
Proof certifier/checker

#### Expected input thing:
- Circuit
- Value $k$ provided by a k-induction-based model checker which outputs a positive model checking result.

#### Expected input format:
[AIGER](AIGER.md)
Note: they extended the reset logic definition of the existing AIGER format to enable reset functions.

#### Expected output:
`SUCCESS` if the original circuit is safe

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Certifaiger reduces the certification problem to pure SAT checks and checking a simple quantified Boolean formula (QBF) with one quantifier alternation.
Uses the SAT solver [[Kissat]] for checking validity of the formulas. Uses the QBF solver [[QuAbS]]

#### Comments:
-

#### URIs (github, websites, etc.):
Source code and data for CAV '21 paper: http://fmv.jku.at/certifaiger/

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_17

#### Related tools (tools mentioned or compared to in the paper):
