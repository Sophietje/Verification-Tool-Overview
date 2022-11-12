#### Name:
Nagini

#### Application domain/field:
Program verification
Dynamic languages
Deductive verification
Concurrent programs

#### Type of tool (e.g. model checker, test generator):
Static verifier/deductive verifier

#### Expected input thing:
Source code (statically-typed) with specifications (pre-/postconditions/loop invariants/etc.)

#### Expected input format:
Python file

#### Expected output:
Verified (i.e. specification holds) or an error

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Automated verifier for statically-typed, concurrent Python 3 programs. The Python program is encoded into a Viper program. The program can then be verified using either symbolic execution or verification condition generation.

"Nagini can verify memory safety, functional properties, termination, deadlock freedom, and input/output behavior."

Uses [Viper](Frameworks/Viper.md), [[mypy]], [Boogie](Frameworks/Boogie.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/marcoeilers/nagini
Information about the specification language: https://github.com/marcoeilers/nagini/wiki
Artifact of CAV 2021 paper: https://zenodo.org/record/4724854

#### Last commit date:
18 May 2021

#### Last publication date:
18 July 2018

#### List of related papers:
[Nagini: A Static Verifier for Python](https://doi.org/10.1007/978-3-319-96145-3_33) (CAV 2018)
[Product Programs in the Wild: Retrofitting Program Verifiers to Check Information Flow Security](https://doi.org/10.1007/978-3-030-81685-8_34) (CAV 2021)

#### Related tools (tools mentioned or compared to in the paper):
Tools that also use Viper as a back end for verification: [Gobra](Gobra.md), [[Prusti]] and [[VerCors]].

#### Meta
:: Python
:: Concurrency
:: PV4 :: verifies general properties like termination and deadlock freedom of Python programs
:: Source :: https://doi.org/10.1145/3550355.3552426