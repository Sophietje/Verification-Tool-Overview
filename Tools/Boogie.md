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

Uses [[Z3]], [[CVC4]], [[Yices]]

#### Comments:
Intermediate verification language & verifier
It is intended as a layer to build program verifiers on top of.

#### URIs (github, websites, etc.):
https://github.com/boogie-org/boogie
https://boogie-docs.readthedocs.io/en/latest/ (Documentation)

#### Last commit date:
6 May 2021

#### Last publication date:

#### List of related papers:

#### Related tools (tools mentioned or compared to in the paper):


