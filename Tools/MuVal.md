Termination analyzer?

#### Name:
MuVal

#### Application domain/field:
Program termination
Counterexample guided inductive synthesis (CEGIS)
Ranking functions

#### Type of tool (e.g. model checker, test generator):
(Non-)termination analyzer

#### Expected input thing:
C program

#### Expected input format:
`.t2` file
They provide a command that can be used to convert a `.c` file into a z`.t2` file using [llvm2kittel](https://github.com/gyggg/llvm2kittel/tree/kou).

#### Expected output:
Indicates whether the tool can prove that the program terminates (`YES`), the tool verifies non-termination(`NO`), timed out (`TO`), or could not find an answer (`U`).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
They focus on synthesizing ranking functions. Ranking functions assign a natural number to each program state, in such a way that the values strictly decrease along transitions. If there is such a ranking function, it can be used to prove the termination of a program.

Uses [Z3](Solvers/SMT/Z3.md)

#### Comments:
License: Apache-2.0

#### URIs (github, websites, etc.):
Repository?: https://github.com/hiroshi-unno/coar (should include [MuVal](MuVal.md) and [PCSat](Solvers/PCSat.md))

#### Last commit date:
11 May 2021 (default branch)
11 May 2021 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[Decision Tree Learning in CEGIS-Based Termination Analysis](https://doi.org/10.1007/978-3-030-81688-9_4) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
[AProVE](AProVE.md), [iRankFinder](iRankFinder.md), [Ultimate Automizer](Ultimate%20Automizer.md)

#### Meta
:: Termination
:: C
:: PV1 :: checks whether a C program will (non-)terminate
:: Source :: https://doi.org/10.1007/978-3-030-81688-9 :: https://doi.org/10.1145/3550355.3552426
