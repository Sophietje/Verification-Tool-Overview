#### Name:
nuXmv

#### Application domain/field:
Symbolic model checking
Synchronous transition systems
Finite-state systems
Infinite-state systems

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Transition system (finite transition system (FSM) or timed transition system (TTS))
- *Optional*: Specification/property to check

#### Expected input format:
Own input language (described in the user manual)

#### Expected output:
Depends on what is asked of nuXmv.
A typical use case would be model checking (i.e. checking whether a property holds). In this case, nuXmv reports per property whether it is true. If a property is not true then it will print a counterexample.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Symbolic model checker for finite- and infinite-state transition systems and temporal logics.

nuXmv has commands for model checking, model simulation, computing reachable states, predicate abstraction, model transformation, and model exploration.
Moreover, it also supports the conversion of the nuXmv format into [AIGER](../../Formats/AIGER.md) 1.9.4 and [[VMT]] (extension of [SMT-LIB](../../Formats/SMT-LIB.md) for symbolic transition systems).

Uses [MathSAT](../Solvers/SMT/MathSAT.md) 5, [CUDD](../Libraries/CUDD.md), [MiniSat](../Solvers/SAT/MiniSat.md), [MSATIC3](../Solvers/MSATIC3.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://nuxmv.fbk.eu/
User manual: https://nuxmv.fbk.eu/pmwiki.php?n=Documentation.Home

#### Last commit date:
14 October 2019 (date of last publicly available binary)

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25540-4_21
https://doi.org/10.1007/978-3-319-08867-9_22

#### Related tools (tools mentioned or compared to in the paper):
Successor of [[NuSMV]].
[[NuRV]]: nuXmv extension for runtime verification.

#### Meta
:: PV2 :: checks user-specified properties of a transition system