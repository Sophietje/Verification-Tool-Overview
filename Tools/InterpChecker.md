InterpChecker is a tool for verifying safety properties of C programs

#### Name:
InterpChecker

#### Application domain/field:
Safety verification
Model checking
Counterexample-guided abstraction refinement (CEGAR)
Reachability checking

#### Type of tool (e.g. model checker, test generator):
Model checker?

#### Expected input thing:
C program instrumented with error labels

#### Expected input format:
`.c` file

#### Expected output:
`UNSAFE` or `SAFE` indicating whether the program can reach unsafe states (i.e. error labels)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Implementation builds on [CPAchecker](Checkers/CPAchecker.md).

Given a C program, it will use reachability checking to see whether it can reach any of the instrumented error labels.

#### Comments:
False negatives may occur for programs with recursive functions since recursive functions are treated as pure functions.

#### URIs (github, websites, etc.):
Repository: https://github.com/duanzhao-dz/interpchecker

#### Last commit date:
22 November 2017

#### Last publication date:
14 April 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-89963-3_27 (TACAS '18)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C