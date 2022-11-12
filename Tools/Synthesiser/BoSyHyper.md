#### Name:
BoSyHyper

#### Application domain/field:
Reactive synthesis
LTL synthesis
Bounded synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
HyperLTL formula

#### Expected input format:
JSON based format

#### Expected output:
Whether a specification is realizable. If realizable, then a solution can be given.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Implementation based on [BoSy](BoSy.md) LTL synthesis tool.
- Uses [Z3](../Solvers/SMT/Z3.md)

#### Comments:
- Synthesis tool for universal HyperLTL based on a bounded synthesis algorithm (i.e.: Given a specification in HyperLTL, it synthesizes a reactive system).
- HyperLTL is an extension of LTL with trace variables and explicit trace quantification. Hyperlogics (like HyperLTL) can be used to express things that relate multiple traces, e.g. absence of information leaks.

#### URIs (github, websites, etc.):
https://www.react.uni-saarland.de/tools/bosy/
https://github.com/reactive-systems/bosy

#### Last commit date:
17 May 2021

#### Last publication date:
18 July 2018

#### List of related papers:
[Synthesizing Reactive Systems from Hyperproperties](https://doi.org/10.1007/978-3-319-96145-3_16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: HyperLTL
:: PV4 :: proves realizability of a given hyperproperty
:: Synthesis
:: Source :: https://doi.org/10.1145/3550355.3552426
