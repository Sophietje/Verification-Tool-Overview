Reversible circuit compiler that has been formally verified in [F\*](https://www.fstar-lang.org/). It compiles circuits that operate correctly with respect to the input program.

#### Name:
ReVerC, pronounced as "reverse"

#### Application domain/field:
Reversible circuits
Compilation
Quantum computing

#### Type of tool (e.g. model checker, test generator):
Compiler

#### Expected input thing:
Program

#### Expected input format:
Revs language

#### Expected output:
Combinational reversible circuits with as few ancillary bits as possible which provably cleans temporary values.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This work focuses on helping a programmer translate classical irreversible programs into a form which a quantum computer can execute. These are called reversible circuits. 

ReVerC is fully verified, meaning that the circuit compiled by ReVerC will produce the same output for every input as the original source program.

ReVerC also provides an assertion checker to verify the source program. 

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/msr-quarc/ReVerC

#### Last commit date:
5 March 2019

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63390-9_1 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
[[Quipper]]

#### Meta
:: PV2 :: transforms irreversible programs into reversible circuits
:: Reversible computation