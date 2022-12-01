Verification technique to prove properties of a class of array programs with a symbolic parameter N denoting the size of the arrays.

#### Name:
Diffy

#### Application domain/field:
Array programs
Program verification
Invariants

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
C program with assertions, arrays need to be stack allocated instead of malloc'd.

#### Expected input format:
C program: similar format to what is used for SV-COMP. 
Assertions are expressed as `__VERIFIER_assert(...)`

#### Expected output:
`DIFFY_VERIFICATION_SUCCESSFUL` when the given post-condition is verified.
`DIFFY_VERIFICATION_FAILED` when the given post-condition is violated.
`DIFFY_VERIFICATION_UNKNOWN` when the result cannot be determined.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md).

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Artifact for CAV '21: https://figshare.com/articles/software/Diffy_Inductive_Reasoning_of_Array_Programs_using_Difference_Invariants/14509467
Artifact for CAV '21, repository: https://github.com/divyeshunadkat/diffy-artifact

#### Last commit date:
29 Apr 2021 (default branch)
05 Nov 2021 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[Diffy: Inductive Reasoning of Array Programs Using Difference Invariants](https://doi.org/10.1007/978-3-030-81688-9_42) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [[Vajra]] (part of [VeriAbs](VeriAbs.md))

#### Meta
:: PV3 :: checks user-specified assertions in a C program
:: C
:: Source :: https://doi.org/10.1145/3550355.3552426
