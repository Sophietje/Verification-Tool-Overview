#### Name:
SeaHorn

#### Application domain/field:
Safety properties
Software model checking
Abstract interpretation
Software verification

#### Type of tool (e.g. model checker, test generator):
Model checker?

#### Expected input thing:
Program with assertions

#### Expected input format:
C program, assertions written in the SV-COMP style (e.g., `__VERIFIER_error()`)

#### Expected output:
`Result TRUE` when the program is safe, `Result FALSE` when a counterexample was found, or `Result UNKNOWN` otherwise.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Seahorn is a verification platform that uses Constrained Horn Clauses (CHC) as an intermediate verification language. It focuses on proving safety properties for C programs.
It uses software model checking and abstract interpretation techniques.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://seahorn.github.io/
Repository: https://github.com/seahorn/seahorn

#### Last commit date:
29 Mar 2023 (last activity)

#### Last publication date:
24 November 2018

#### List of related papers:
[Executable Counterexamples in Software Model Checking](https://doi.org/10.1007/978-3-030-03592-1_2) (VSTTE 2018)
[Synthesizing Ranking Functions from Bits and Pieces](https://doi.org/10.1007/978-3-662-49674-9_4) (TACAS 2016)
[The SeaHorn Verification Framework](https://doi.org/10.1007/978-3-319-21690-4_20) (CAV 2015)
[SeaHorn: A Framework for Verifying C Programs (Competition Contribution)](https://doi.org/10.1007/978-3-662-46681-0_41) (TACAS 2015)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: C
:: PV3 :: checks assertions in a C program
:: CHC
:: Model checking
:: Source :: https://doi.org/10.1007/978-3-662-49674-9 :: https://doi.org/10.1145/3550355.3552426
