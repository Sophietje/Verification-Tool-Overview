Tool for the generation of random transition systems in a symbolic representation

#### Name:
AIGEN

#### Application domain/field:
Transition systems
Reactive synthesis
Program synthesis
Benchmark generation

#### Type of tool (e.g. model checker, test generator):
Benchmark generator/test generator

#### Expected input thing:
- Number of latches $l$
- Number of uncontrollable inputs $u$
- Number of controllable inputs $c$
- Bound $o$
- *Optionally*: list of seeds (i.e. natural numbers for initialization of pseudorandom number generator)

#### Expected input format:
Arguments are all numbers passed as parameters to a Python script.

#### Expected output:
Transition system in [AIGER](../Formats/AIGER.md) format.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [ABC](Frameworks/ABC.md), [AIGER](../Formats/AIGER.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/mhdsakr/AIGEN-Tool

#### Last commit date:
2 June 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_20 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
