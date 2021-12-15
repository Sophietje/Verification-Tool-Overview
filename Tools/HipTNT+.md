HipTNT+ is a modular termination and non-termination analyzer for imperative programs

#### Name:
HipTNT+

#### Application domain/field:
Termination analysis
Non-termination
Imperative programs

#### Type of tool (e.g. model checker, test generator):
Termination prover?

#### Expected input thing:
- C program
- *Optional*: Specification

#### Expected input format:
?

#### Expected output:
`TRUE`, `FALSE` and a witness, or `UNKNOWN`. 
The witness (+`FALSE`) represents a counterexample to termination. `TRUE` indicates that the program will terminate.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
HipTNT+ is built upon the [[HIP/SLEEK]] toolset. 
Uses [[Omega Calculator]] and [Z3](Solvers/SMT/Z3.md).

#### Comments:
-

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
31 March 2017

#### List of related papers:
https://doi.org/10.1007/978-3-662-54580-5_25 (TACAS '17)

#### Related tools (tools mentioned or compared to in the paper):
Other tools that participated in the termination division of SV-COMP 2015: [AProVE](AProVE.md), [[FuncTion]], [Ultimate Automizer](Ultimate%20Automizer.md), [SeaHorn](Checkers/SeaHorn.md)