#### Name:
Code2Inv

#### Application domain/field:
Loop invariant generation
Constrained Horn Clause (CHC) solving

#### Type of tool (e.g. model checker, test generator):
Invariant generator

#### Expected input thing:
- Verification instance
- Proof checker *check*

#### Expected input format:
- *Verification instance*: C program (only supports one loop and no external funciton calls) or a CHC program
- *Proof checker*: ? (a function that takes a verification instance T and a candidate invariant inv, it then either returns success or a counterexample. For example an SMT or CHC solver)

#### Expected output:
Invariant *inv* such that T can be verified with *check*

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Deep learning
- Reinforcement learning

#### Comments:
Framework for program verification based on deep learning.
Given a verification task and proof checker as input, it automatically learns a valid proof for the verification task by interacting with the given checker.

#### URIs (github, websites, etc.):
Repository: https://github.com/PL-ML/code2inv

#### Last commit date:
26 January 2021

#### Last publication date:
14 July 2020

#### List of related papers:
[Code2Inv: A Deep Learning Framework for Program Verification](https://doi.org/10.1007/978-3-030-53291-8_9)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: CHC
:: C
:: PV2 :: generates invariants from a C or CHC program, requires an external solver