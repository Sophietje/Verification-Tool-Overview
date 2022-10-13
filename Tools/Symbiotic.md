Symbiotic implements an approach of combining instrumentation, slicing, and symbolic execution to detect errors in (sequential) C programs

#### Name:
Symbiotic

#### Application domain/field:
Symbolic execution
Bug detection
Program slicing
Safety verification
Memory safety

#### Type of tool (e.g. model checker, test generator):
Bug detector

#### Expected input thing:
- Instrumented C program. It needs to be instrumented with e.g. assertions or `__VERIFIER_error()`.
- *Optional*: This can be used to indicate that Symbiotic should look for certain errors aside from assertion violations, e.g. errors in memory manipulations.

#### Expected input format:
- *Program*: `.c` file(s)
- *Optional property*: passed as an argument while calling symbiotic

#### Expected output:
Symbiotic will report any assertion or property violations that it finds.
It can also generate a violation witness if a property/assertion is violated.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Symbiotic can be used to check safety properties such as assertion violations, invalid pointer dereference, double free, memory leaks, etc.

Uses [KLEE](KLEE.md) for symbolic execution. Uses [Z3](Solvers/SMT/Z3.md) for SMT solving.

#### Comments:
Symbiotic has participated in SV-COMP (verification competition) in 2016-2021.

#### URIs (github, websites, etc.):
Repository: https://github.com/staticafi/symbiotic
Project page: http://staticafi.github.io/symbiotic/

#### Last commit date:
24 Sep 2022

#### Last publication date:
18 May 2020

#### List of related papers:
https://doi.org/10.1007/s10009-020-00573-0 (Journal on Software Tools for Technology Transfer 23, '20)
https://doi.org/10.1007/978-3-030-45237-7_31 (TACAS '20)
https://doi.org/10.1007/978-3-319-89963-3_29 (TACAS '18)
https://doi.org/10.1007/978-3-662-54580-5_28 (TACAS '17)
https://doi.org/10.1007/978-3-662-49674-9_67 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
[PredatorHP](PredatorHP.md) also participated in SV-COMP in the MemSafety category.
Other tools that participated in SV-COMP: [CPAchecker](Checkers/CPAchecker.md), [PeSCo](Metatools/PeSCo.md), [Ultimate Automizer](Ultimate%20Automizer.md), [[SMACK]].

#### Meta
:: PV4 :: can detect assertion violations and memory-related bugs in C programs