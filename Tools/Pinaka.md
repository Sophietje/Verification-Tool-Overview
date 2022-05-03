Pinaka extends symbolic execution with incremental solving coupled with eager infeasibility checks

#### Name:
Pinaka

#### Application domain/field:
Symbolic execution
Incremental SAT solving
Infeasibility checks

#### Type of tool (e.g. model checker, test generator):
Meant to be used in combination with [[CProver/Symex]] framework or maybe as a library?

#### Expected input thing:
GOTO program or C program (which is translated into a GOTO program with the [[CProver/Symex]] framework)

#### Expected input format:
?

#### Expected output:
Successful/failed outcome (indicating an assertion violation) and a witness.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Pinaka is built on top of [CProver](Frameworks/CProver.md)+[[Symex]] framework.
It uses incremental SAT solving, e.g. [MiniSat](Solvers/SAT/MiniSat.md), [Glucose](Solvers/SAT/Glucose.md) and [[MapleSAT]].

#### Comments:
The TACAS '19 paper mentions that Pinaka is the result of the rewriting and refactoring of [[VerifOx]].

#### URIs (github, websites, etc.):
Repository: https://github.com/sbjoshi/Pinaka

#### Last commit date:
19 October 2020

#### Last publication date:
4 April 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-17502-3_20 (TACAS '19)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV3 :: checks user-specified assertions in GOTO  and C programs
:: C