Tool for systematic testing of multithreaded programs.
It can handle programs with input (data) and concurrency.

#### Name:
POR-SE

#### Application domain/field:
Symbolic execution
Partial-order reduction
Multithreaded programs
Concurrency
Systematic testing

#### Type of tool (e.g. model checker, test generator):
Testing tool?

#### Expected input thing:
?

#### Expected input format:
C program?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- POR-SE combines quasi-optimal partial order reduction (POR) with symbolic execution (SE). 
- It has been implemented as an extension of [KLEE](KLEE.md) (it is basically a multi-threaded extension of it).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/por-se/por-se
Extended version of CAV '20 paper: https://arxiv.org/pdf/2005.06688.pdf

#### Last commit date:
16 Dec 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_18

#### Related tools (tools mentioned or compared to in the paper):
[Yogar-CBMC](Yogar-CBMC.md)

#### Meta
:: Concurrency
:: PV3 :: checks properties of multi-threaded programs by symbolic execution