#### Name:
Concord

#### Application domain/field:
Program synthesis

#### Type of tool (e.g. model checker, test generator):
Program synthesis

#### Expected input thing:
- Domain-specific language
- Specification

#### Expected input format:
?

#### Expected output:
A program that satisfies the specification

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Synthesis algorithm based on reinforcement learning tightly coupled with statistical and deductive reasoning.
It focuses on syntax-guided synthesis: given a domain-specific language (DSL) and a specification, they try to find a program that satisfies the specification.
Uses [Z3](../Solvers/SMT/Z3.md).

#### Comments:

#### URIs (github, websites, etc.):

#### Last commit date:
-

#### Last publication date:
14 July 2020

#### List of related papers:
[Program Synthesis Using Deduction-Guided Reinforcement Learning](https://doi.org/10.1007/978-3-030-53291-8_30)

#### Related tools (tools mentioned or compared to in the paper):
Compared to [[Neo]] and [[DeepCoder]].

#### Meta
:: Synthesis
:: PV2 :: given a domain-specific language and specification, it synthesises a program that satisfies the specification