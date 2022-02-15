#### Name:
VVT: Vienna Verification Tool

#### Application domain/field:
Infinite-state systems
Counterexample-guided abstraction refinement (CEGAR)
Predicate abstraction
Model checking
Bounded model checking

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
Program

#### Expected input format:
C/C++ file

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
VVT primarily targets the verification of infinite parallel programs.

VVT consists of several tools
- `vvt-enc` to translate instrumented bitcode into an SMTLIB-based format
- `vvt-opt` to deploy several optimization techniques
- `vvt-verify` to verify the program
- `vvt-bmc` to rapidly find counterexamples

Uses [Z3](Solvers/SMT/Z3.md) and [MathSAT](Solvers/SMT/MathSAT.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://vvt.forsyte.at/
Repository: https://github.com/hgoes/vvt

#### Last commit date:
9 February 2018

#### Last publication date:
9 April 2016

#### List of related papers:
https://doi.org/10.1007/978-3-662-49674-9_6 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
