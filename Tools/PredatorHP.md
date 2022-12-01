Shape analyzer

#### Name:
PredatorHP: Predator Hunting Party

#### Application domain/field:
Memory-related errors
Memory leaks
Abstract interpretation

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- C program to be verified, possibly with assertions
- Property file that contains the property that should be verified
- Path where witness file will be stored
- *Optional*: Compiler options

#### Expected input format:
- *C program*: `.bc` bitcode file. They provide instructions on how to generate the bitcode file from a C file.
- *Property file*: `.prp` file, same format as SV-COMP
- *Path to witness file*: Passed as argument when calling PredatorHP
- *Optional compiler options*: Passed as argument when calling PredatorHP

#### Expected output:
`TRUE` indicating that the specification is satisfied.
`FALSE` indicating that the specification is violated.
`UNKNOWN` if the tool could not determine whether the specification is satisfied or not.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
PredatorHP is built on the [[Predator]] shape analyzer.
PredatorHP looks for memory-related errors such as invalid pointer dereferences, double free operations and memory leaks. It also checks the validity of assertions in the code.

PredatorHP runs multiple tools in parallel. The first tool is the Predator verifier, which can claim that a program is correct. The other tools are called hunters, which typically report errors. These hunters are used to decrease the chances of producing false alarms.

TACAS'20: improved handling of interval-sized memory regions or new support of memory reallocation

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Project page: https://www.fit.vutbr.cz/research/groups/verifit/tools/predator-hp/
Repository: https://github.com/versokova/predatorhp

#### Last commit date:
20 November 2019

#### Last publication date:
17 April 2020

#### List of related papers:
[PredatorHP Revamped (Not Only) for Interval-Sized Memory Regions and Memory Reallocation (Competition Contribution)](https://doi.org/10.1007/978-3-030-45237-7_30) (TACAS '20)
[Optimized PredatorHP and the SV-COMP Heap and Memory Safety Benchmark](https://doi.org/10.1007/978-3-662-49674-9_66) (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C
:: PV4 :: checks memory-related errors and user-specified properties in C programs
:: Source :: https://doi.org/10.1145/3550355.3552426
