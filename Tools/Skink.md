Skink is a static analysis tool that analyses the LLVM intermediate representation (LLVM-IR) of a program source code

#### Name:
Skink

#### Application domain/field:
LLVM intermediate representation (LLVM-IR)
Static analysis
Reachability analysis
Multi-threaded programs
Concurrent programs

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
Program with assertions (`assert(condition)`)

#### Expected input format:
C file

#### Expected output:
Verification output and witness file.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md), [SMTInterpol](Solvers/SMT/SMTInterpol.md) and [CVC4](Solvers/SMT/CVC4.md).

Skink may assume unbounded integers resulting in false negatives.
Skink's analysis tries to determine whether an assertion can be violated.

#### Comments:
-

#### URIs (github, websites, etc.):
Download link for Skink: https://science.mq.edu.au/~fcassez/sw/
Project page: https://science.mq.edu.au/%7efcassez/software-verif.html#sec-tool

#### Last commit date:
24 December 2015

#### Last publication date:
31 March 2017

#### List of related papers:
https://doi.org/10.1007/978-3-662-54580-5_27 (TACAS '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: LLVM
:: Compiler
:: C
:: PV3 :: verifies assertions given in source code