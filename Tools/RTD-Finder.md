#### Name:
RTD-Finder

#### Application domain/field:
Safety verification
Real-time systems
Component-based systems
Compositional verification
Invariant generation

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Real-time BIP program
- *Optional*: Safety property

#### Expected input format:
- *Program*: RT-BIP source file
- *Safety property*: Yices syntax. If this property is not provided then the tool will default to check deadlock-freedom.

#### Expected output:
It will report whether the safety property is satisfied or not. If it is not satisfied, then it will also provide a counterexample.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It takes as input a RT-BIP model and a safety property to check for. Then it computes a global invariant. The idea is that this global invariant encodes the components of the system and the interactions relating them. This invariant is sometimes called the interaction invariant because of this.
The invariant together with the safety property are then given to the [Yices](Solvers/SMT/Yices.md) solver to check whether $GI \wedge \neg \Psi$ is satisfiable. It will then report that (1) the property is satisfied, or (2) that it is not satisfied and a counterexample.

Uses [Yices](Solvers/SMT/Yices.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: www-verimag.imag.fr/RTD-Finder

#### Last commit date:
-

#### Last publication date:
9 April 2016

#### List of related papers:
https://doi.org/10.1007/978-3-662-49674-9_23 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
[[D-Finder]]: similar system for untimed systems.

#### Meta
:: PV4 :: can check deadlock-freedom and user-specified safety properties of RT-BIP models