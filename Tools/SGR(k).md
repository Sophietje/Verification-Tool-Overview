#### Name:
SGR(k): Separated GR(k)

#### Application domain/field:
Design pattern
Program synthesis
Reactive synthesis
Adapters

#### Type of tool (e.g. model checker, test generator):
Synthesizer

#### Expected input thing:
- Equivalence relation and the specification of the adaptee and the target
- Set of temporal properties (special form of LTL)

#### Expected input format:
?

#### Expected output:
Adapter, in the form of a transducer

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This work focuses on the Adapter design pattern where a program implements a Target interface by constructing an Adapter that accesses an existing Adaptee code.
It aims to, given an Adaptee and a Target (two finite-state transducers), to synthesize an Adapter transducer. This Adapter transducer will, combined with the Adaptee, generate equivalent behavior to the Target's behavior.

The implementation uses the [CUDD](Libraries/CUDD.md) package for BDD manipulation.

#### Comments:
The tool is called a 'prototype tool' in the CAV '21 paper.

#### URIs (github, websites, etc.):
Artifact for CAV '21 paper: https://zenodo.org/record/4726692

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_41 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in the CAV '21 paper: [Strix](Synthesiser/Strix.md)