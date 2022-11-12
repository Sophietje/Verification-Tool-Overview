2LS is a C program analyser built upon the [CProver](Frameworks/CProver.md) infrastructure

#### Name:
2LS

#### Application domain/field:
Assertion checking
Invariant generation
Bounded model checking
Incremental k-induction
Abstract interpretation
Static analysis

#### Type of tool (e.g. model checker, test generator):
Model checker?? / Program analyser

#### Expected input thing:
- C program
- *Optionally*: Assertions in the program

#### Expected input format:
`.c` file

#### Expected output:
`PASS`, `FAIL` or `UNKNOWN`?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- The name seems to be derived from the fact that it takes program analysis problems expressed in second order logic. So, it reduces (an existential fragment of) 2nd order logic to quantifier elimination in first order logic.
- 2LS can verify array bounds (buffer overflows), pointer safety, exceptions, user-specified assertions, and (non-)termination properties.
- There are many different options to specify the kind of analyses that you want to do. Some analyses that it supports include: bounded model checking, k-induction, non-termination analysis and function-modular termination analysis.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/diffblue/2LS

#### Last commit date:
27 Sep 2022

#### Last publication date:
14 April 2018

#### List of related papers:
[2LS for Program Analysis](https://doi.org/10.1007/978-3-662-49674-9_56) (TACAS '16)
[2LS: Memory Safety and Non-termination](https://doi.org/10.1007/978-3-319-89963-3_24) (TACAS '18)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C
:: PV4           :: can generate properties within certain conditions
:: Model checking