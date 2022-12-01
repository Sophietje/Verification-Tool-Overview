#### Name:
IVy

#### Application domain/field:
Protocol verification
Distributed programs

#### Type of tool (e.g. model checker, test generator):
Protocol verifier

#### Expected input thing:
Program

#### Expected input format:
.ivy file (program specified in the IVy language)

#### Expected output:
Depends on the mode of operation:
1. `ivy_check` checks the proof of an IVy program, will return `PASS` or `FAIL`
2. `ivy` will allow the user to interactively construct inductive invariants
3. `ivy_to_cpp` will result in a C++ program extracted from the IVy program

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Used for specifying, modeling, implementing and verifying protocols.
"Tool for correct design and implementation of distributed protocols and algorithms, supporting modular specification, implementation and proof"

Some things it can do:
- Checking safety/liveness via (1) deductive verification, (2) abstraction and model checking (3) manual proofs using natural deduction
- Compositional specification-based testing and bounded model checking
- Extract executable distributed programs by translation to efficient C++ code

Uses [ABC](Frameworks/ABC.md), [Z3](Solvers/SMT/Z3.md).

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Project page: https://microsoft.github.io/ivy/
Repository (linked on project page): https://github.com/kenmcmil/ivy
Old repository (the original, now archived repository, links to the repository above as the new one): https://github.com/microsoft/ivy

#### Last commit date:
ivy: 13 Oct 2022 (default branch)
ivy: 04 Sep 2020 (default branch)
13 Oct 2022 (last activity)

#### Last publication date:
14 July 2020

#### List of related papers:
[Ivy: A Multi-modal Verification Tool for Distributed Algorithms](https://doi.org/10.1007/978-3-030-53291-8_12) (CAV 2020)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Model checking
:: Framework
:: Protocol
:: PV6 :: deductively or inductively proves or helps prove program properties
:: Source :: https://doi.org/10.1145/3550355.3552426
