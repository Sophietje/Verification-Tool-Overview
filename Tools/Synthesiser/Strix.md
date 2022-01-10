Tool for reactive LTL synthesis

#### Name:
Strix

#### Application domain/field:
Synthesis
LTL synthesis
Reactive synthesis
Deterministic parity automata (DPA)
Controller synthesis

#### Type of tool (e.g. model checker, test generator):
LTL synthesis tool

#### Expected input thing:
LTL formula(s)

#### Expected input format:
[Owl](../Libraries/Owl.md) format (https://gitlab.lrz.de/i7/owl/blob/master/doc/FORMATS.md)

#### Expected output:
`REALIZABLE` or `UNREALIZABLE`.

If realizable, then it also outputs a controller in one of the following formats: 
- Mealy/Moore machine ([HOA](../../Formats/HOA.md) format)
- [AIGER](../../Formats/AIGER.md) circuit
- BDD (dot format with [CUDD](../Libraries/CUDD.md) interpretation)
- Parity game ([[PGSolver]] format)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Speculoos](../Speculoos.md), [MeMin](../MeMin.md), [ABC](../Frameworks/ABC.md).

Given an LTL formula, it synthesizes a controller. I.e. it tries to find a matching implementation, e.g. a Mealy machine, for an LTL formula.
To achieve this, it takes the following steps:
1. Decompose the given formula into simpler formulas
2. Translate these formulas on-the-fly into DPAs based on the queries of the parity game solver
3. Compose the DPAs into a parity game, and at the same time solve the intermediate games using strategy iteration
4. Translate the winning strategy, if it exists, into a Mealy machine or an AIGER circuit

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://strix.model.in.tum.de/
Repository: https://github.com/meyerphi/strix
Online demo: https://meyerphi.github.io/strix-demo/

#### Last commit date:
4 September 2021

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_31 (CAV '18)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in the CAV '18 paper: [PARTY](PARTY.md), [BoSy](BoSy.md), [[LTLSYNT]]