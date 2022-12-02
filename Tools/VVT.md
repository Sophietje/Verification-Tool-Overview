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
C/C++ and SMTLib2

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
08 Feb 2018 (default branch)
09 Feb 2018 (last activity)

#### Last publication date:
9 April 2016

#### List of related papers:
[Vienna Verification Tool: IC3 for Parallel Software](https://doi.org/10.1007/978-3-662-49674-9_69) (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C
:: C++
:: PV3 :: encodes an LLVM program into a transition relation and checks properties on it
:: Source :: https://doi.org/10.1145/3550355.3552426
