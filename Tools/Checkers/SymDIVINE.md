SymDIVINE, a model-checker for concurrent C/C++ programs

#### Name:
SymDIVINE

#### Application domain/field:
Model checking
Concurrent programs
Software model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Program
- *Optional*: Assertions in program
- *Optional*: LTL property

#### Expected input format:
`.ll` file (for assert reachability verification of LLVM bitcode) or C/C++ program.

#### Expected output:
`TIMEOUT`, `true` or `false` indicating whether it could prove the assertion/LTL property.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](../Solvers/SMT/Z3.md)

#### Comments:
The repo is archived and no longer maintained. It is now integrated into [DIVINE](../DIVINE.md).

#### URIs (github, websites, etc.):
Repository: https://github.com/paradise-fi/SymDIVINE

#### Last commit date:
19 March 2019

#### Last publication date:
31 March 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-32582-8_14 (SPIN '16)
https://doi.org/10.1007/978-3-662-54580-5_29 (TACAS '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Concurrency