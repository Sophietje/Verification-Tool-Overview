Map2Check is a bug hunting tool that automatically checks safety properties in C programs

#### Name:
Map2Check

#### Application domain/field:
Fuzzing
Symbolic execution
Inductive invariants
Safety properties
Unit tests
Assertions
Memory safety

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- C program
- Property file

#### Expected input format:
- *C program*: `.c` file
- *Property file*: `.prp` file (SV-COMP format)

#### Expected output:
`TRUE` + witness, `FALSE` or `FALSE(p)` + witness or `UNKNOWN`.
`FALSE(p)` means that the property `p` is violated.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Map2Check checks for the following (SV-COMP) properties:
- Invalid free
- Invalid dereference
- Memory leak
- Assertion violations
- Overflows
- Pointer safety

Uses [KLEE](KLEE.md), [[LibFuzzer]], [[Crab-LLVM]]

#### Comments:
License: GPL v2.0

#### URIs (github, websites, etc.):
Project page: https://map2check.github.io/
Repository: https://github.com/hbgit/Map2Check

#### Last commit date:
13 February 2020

#### Last publication date:
17 April 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-45237-7_29 (TACAS '20)
https://doi.org/10.1007/978-3-319-89963-3_28 (TACAS '18)
https://doi.org/10.1007/978-3-662-49674-9_64 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
Other tools that participated in similar categories of SV-COMP: [CPAchecker](Checkers/CPAchecker.md), [DIVINE](DIVINE.md), [ESBMC](ESBMC.md), [PeSCo](Metatools/PeSCo.md), [Pinaka](Pinaka.md), [Symbiotic](Symbiotic.md), [Ultimate Automizer](Ultimate%20Automizer.md), [[UKojak]], [VeriAbs](VeriAbs.md), [VeriFuzz](VeriFuzz.md)