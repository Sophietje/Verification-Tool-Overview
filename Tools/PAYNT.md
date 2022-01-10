Given a sketch of a program, it will synthesize (if possible) the missing parts such that a user-defined specification is satisfied.

#### Name:
PAYNT: Probabilistic progrAm sYNThesizer

#### Application domain/field:
Program synthesis
Probabilistic programs
Oracle-guided synthesis

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
- Program sketch, concisely describing a finite family of finite Markov chains (MCs)
- Specification, as a temporal logic constraint

#### Expected input format:
- *Program sketch*: extension of the [PRISM](Checkers/PRISM.md) language or [JANI](../Formats/JANI.md) language
- *Specification*: [PRISM](Checkers/PRISM.md) syntax

#### Expected output:
A satisfying realization, i.e. an assignment to the holes in the program sketch such that the program satisfies the specification.
Otherwise, it will report that such a design does not exist.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
PAYNT has been implemented on top of the probabilistic model checker [Storm](Checkers/Storm.md). It uses [Z3](Solvers/SMT/Z3.md).

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/gargantophob/synthesis
CAV '21 artifact: https://doi.org/10.5281/zenodo.4726056

#### Last commit date:
3 June 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_40 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Topology synthesis: [[ProFeat]], [[QFLan]]
Parameter synthesis: [Storm](Checkers/Storm.md), [PRISM](Checkers/PRISM.md)

Probabilistic model checkers: [Storm](Checkers/Storm.md), [PRISM](Checkers/PRISM.md), [Modest](Frameworks/Modest.md)