#### Name:
BtorMC

#### Application domain/field:
Model checking
Bounded model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
?

#### Expected input format:
[Btor2](../../Formats/Btor2.md) model

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
BtorMC is a bounded model checker.
It can check safety properties for models with registers and memories.
It also produces witnesses for satisfiable properties.

Uses [Boolector](../Solvers/SMT/Boolector.md) 3.0

#### Comments:
It is called a 'reference' bounded model checker in the paper.

#### URIs (github, websites, etc.):
Seems to be included in the [Boolector](../Solvers/SMT/Boolector.md) repository: https://github.com/Boolector/boolector/tree/ad16fd1b47fdce57cc55ca5f1b2f4f7c95b2f631

#### Last commit date:
11 Oct 2022 (last activity)

#### Last publication date:
18 July 2018

#### List of related papers:
[Btor2 , BtorMC and Boolector 3.0](https://doi.org/10.1007/978-3-319-96145-3_32)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [Boolector](../Solvers/SMT/Boolector.md), [Yices](../Solvers/SMT/Yices.md)

#### Meta
:: PV4 :: checks safety properties of models with registers and memories
:: Model checking
:: Source :: https://doi.org/10.1145/3550355.3552426
