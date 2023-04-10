#### Name:
NIS (Numerical Invariant Synthesizer)

#### Application domain/field:
Synthesis
Invariant synthesis
Numerical programs
Data-driven synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
Transition system and a property?

#### Expected input format:
[SyGuS language](../../Formats/SyGuS%20language.md)

#### Expected output:
An inductive invariant I such that the program can be proven correct, otherwise an error.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](../../Tools/Solvers/SMT/Z3.md) for solving SMT queries and [APRON](../../Tools/Libraries/APRON.md) for abstract domains.
Uses ICE-DT, a learning approach tailed for invariant synthesis that uses decision trees.

#### Comments:
-

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
7 August 2022

#### List of related papers:
[Data-driven Numerical Invariant Synthesis with Automatic Generation of Attributes](https://doi.org/10.1007/978-3-031-13185-1_14) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '22 paper: [[ICE-DT]], [LoopInvGen](../../Tools/LoopInvGen.md), [CVC4](../../Tools/Solvers/SMT/CVC4.md), [Spacer](../../Tools/Solvers/Spacer.md)

#### Meta
:: Invariant synthesis
:: PV2 :: synthesises inductive invariants for a SyGuS problem
:: Source :: https://doi.org/10.1007/978-3-031-13185-1

