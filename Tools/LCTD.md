Verifier for C programs

#### Name:
LCTD

#### Application domain/field:
Symbolic execution
Dynamic symbolic execution (DSE)
Counterexample guided abstraction refinement (CEGAR)
Reachability properties
Assertion violations

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
They have implemented the DASH algorithm as a modification to the [[Lime Concolic Tester]] (LCT). 
The DASH algorithm tries to generate tests based on counterexamples found with CEGAR. 

Uses [Z3](Solvers/SMT/Z3.md).

In 2016, it participated in only one category of SV-COMP because it only supported reachability properties and had limited language support.

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
http://users.cse.aalto.fi/osaariki/lctd-svcomp/
https://github.com/OlliSaarikivi/benchexec/blob/master/benchexec/tools/lctd.py

#### Last commit date:
-

#### Last publication date:
9 April 2016

#### List of related papers:
[LCTD: Tests-Guided Proofs for C Programs on LLVM](https://doi.org/10.1007/978-3-662-49674-9_62) (TACAS '16)
[LCTD: Test-guided proofs for C programs on LLVM](https://doi.org/10.1016/j.jlamp.2015.10.010) (Journal of Logical and Algebraic Methods in Programming '16, Volume 85 Issue 6)

#### Related tools (tools mentioned or compared to in the paper):
Other tools that participated in the BitVectorsReach category of SV-COMP 2016: [2LS](2LS.md), [CBMC](Checkers/CBMC.md), [[Ceagle]], [CPAchecker](Checkers/CPAchecker.md), [ESBMC](ESBMC.md), [[Forest]], [[Impara]], [[PAC-MAN]], [SeaHorn](Checkers/SeaHorn.md), [[SMACK+Coral]], [[Symbiotic]], [Ultimate Automizer](Ultimate%20Automizer.md), [[UKojak]]

#### Meta
:: C
:: LLVM
:: PV4 :: generates increasingly precise tests to pinpoint an error or prove program correct
:: Source :: https://doi.org/10.1145/3550355.3552426