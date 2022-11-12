Automated verification tool for concurrent programs.

#### Name:
Starling

#### Application domain/field:
Concurrency
Concurrent algorithms

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Program
- Annotations, expressed as Concurrent Views Framework-style assertions
- Constraints binding assertions to concrete facts

#### Expected input format:
- *Program*: C-like language
- *Annotations*: ?
- *Constraints*: ?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md), [GRASShopper](GRASShopper.md).

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/septract/starling-tool

#### Last commit date:
21 Jul 2017

#### Last publication date:
13 July 2017

#### List of related papers:
[Starling: Lightweight Concurrency Verification with Views](https://doi.org/10.1007/978-3-319-63387-9_27) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Concurrency
:: PV3 :: checks user-specified specifications for concurrent algorithms in a C-like language