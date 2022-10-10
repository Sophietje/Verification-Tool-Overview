DIVINE is an explicit-state LLVM-based model checker focusing on the analysis of real-world C and C++ programs

#### Name:
DIVINE

#### Application domain/field:
Model checker
Explicit-state model checker
Multithreaded programs
LLVM

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
C program with assertions

#### Expected input format:
Single C/C++ file or a compiled program that is linked to DIVINE's runtime libraries.

#### Expected output:
Whether it could verify the assertions in the program. If not then it will produce an error trace (output of the program until the point of the error).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md).

Aside from verifying the program, DIVINE also has some an option to visualize the state space and to simulate a program run interactively.

Note: before verifying with DIVINE, you first need to compile the program (if it's not a single file) into LLVM bitcode and link it against DIVINE's runtime librraries. This can be done with `divine cc program.c`

#### Comments:
License; ISC license (2-clause BSD)
#### URIs (github, websites, etc.):
Project page: https://divine.fi.muni.cz/index.html
Mirror of code on github: https://github.com/paradise-fi/divine

#### Last commit date:
21 March 2021

#### Last publication date:
04 April 2019

#### List of related papers:
[Extending DIVINE with Symbolic Verification Using SMT](https://doi.org/10.1007/978-3-030-17502-3_14) (TACAS '19)
[Model Checking of C and C++ with DIVINE 4](https://doi.org/10.1007/978-3-319-68167-2_14) (ATVA '17)
[
      DIVINE: Explicit-State LTL Model Checker](https://doi.org/10.1007/978-3-662-49674-9_60) (TACAS  '16)

#### Related tools (tools mentioned or compared to in the paper):
Tool that is now integrated in DIVINE: [SymDIVINE](Checkers/SymDIVINE.md)

#### Meta
:: C
:: C++
:: PV3 :: checks user-specified assertions in a C/C++ program
:: Simulation