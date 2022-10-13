Separation logic-based modular verifier for C and Java programs.

#### Name:
Verifast

#### Application domain/field:
Separation logic
Termination
Concurrency
Symbolic execution
Deductive verification

#### Type of tool (e.g. model checker, test generator):
Deductive verifier

#### Expected input thing:
Program annotated with preconditions, postconditions, etc. that express the expected behavior of the program

#### Expected input format:
C or Java program. 
Specifications are written as comments in Verifast's own specification language.

#### Expected output:
"0 errors found" or indicates the location of a potential error.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Verifast checks that the program does not perform illegal memory accesses, does not include data races and complies with the specified pre- and postconditions.

Uses [Z3](Solvers/SMT/Z3.md).

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/verifast/verifast/
Tutorial: https://doi.org/10.5281/zenodo.1068185

#### Last commit date:
29 Sep 2022

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_2 (CAV '21)
https://doi.org/10.1007/978-3-642-20398-5_4 (NFM '11)
https://doi.org/10.1007/978-3-642-17164-2_21 (APLAS '10)

#### Related tools (tools mentioned or compared to in the paper):
Tools using separation logic: [[Smallfoot]], [[jStar]], [[SpaceInvader]], [[Abductor]]
Tools for Java Card programs: [[ESC/Java]], [[KeY]]
Tools for C programs: [[BLAST]], [[SLAM/SDV]], [[VCC]]
Other deductive verifiers: [[VerCors]], [[OpenJML]]

#### Meta
:: PV4 :: checks for illegal memory accesses, data races and user-written specifications in C/Java code