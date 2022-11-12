#### Name:
Boogie

#### Application domain/field:
Static program verification

#### Type of tool (e.g. model checker, test generator):
Verification framework

#### Expected input thing:
Program

#### Expected input format:
Boogie language (.bpl file)

#### Expected output:
Error message for any assertions, preconditions, postconditions, or loop invariants that could not be proven correct.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The verifier, given a Boogie program, generates verification conditions (VCs) that are passed to an SMT solver.

Uses [Z3](../Solvers/SMT/Z3.md), [CVC4](../Solvers/SMT/CVC4.md), [Yices](../Solvers/SMT/Yices.md)

#### Comments:
Intermediate verification **language & verifier**
It is intended as a layer to build program verifiers on top of.

License: MIT

#### URIs (github, websites, etc.):
https://github.com/boogie-org/boogie
https://boogie-docs.readthedocs.io/en/latest/ (Documentation)

#### Last commit date:
30 Sep 2022

#### Last publication date:
15 July 2021

#### List of related papers:
[Formally Validating a Practical Verification Condition Generator](https://doi.org/10.1007/978-3-030-81688-9_33) (CAV '21)
[Layered Concurrent Programs](https://doi.org/10.1007/978-3-319-96145-3_5) (CAV '18)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Framework
:: PV4           :: infers invariants and generates verification conditions to pass to Z3