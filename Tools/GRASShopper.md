Automated deductive program verifier

#### Name:
GRASShopper

#### Application domain/field:
Dynamic allocation
Data structures
Separation logic
Functional correctness
Heap manipulating programs
Deductive verification

#### Type of tool (e.g. model checker, test generator):
Deductive verifier

#### Expected input thing:
Program

#### Expected input format:
Own simple procedural imperative language that supports user-defined struct types and arrays. (`.spl` file)

#### Expected output:
It will indicate errors in the program or specification.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Given an input program, GRASShopper will check the following:
- All procedures mutually satisfy their specified contracts
- All loops satisfy their loop invariants
- All heap accesses and memory deallocations are safe
- There are no memory leaks

GRASShopper focuses on a decidable specification logic so that the proof obligations can be reduced to a decidable fragment of first-order logic.

Uses [Z3](Solvers/SMT/Z3.md), [CVC4](Solvers/SMT/CVC4.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/wies/grasshopper
Project page: https://cs.nyu.edu/~wies/software/grasshopper/

#### Last commit date:
20 May 2021
(Last release: 8 February 2019)

#### Last publication date:
2014

#### List of related papers:
https://doi.org/10.1007/978-3-319-08867-9_47 (CAV '14)
https://doi.org/10.1007/978-3-642-54862-8_9 (TACAS '14)
https://doi.org/10.1007/978-3-642-39799-8_54 (CAV '13)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV4 :: checks user-specified contracts and memory safety of programs in its own language