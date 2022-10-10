Verification infrastructure for permission-based reasoning

#### Name:
Viper

#### Application domain/field:
Verification architecture
Symbolic execution
Separation logic
Verification condition generation
Deductive verification

#### Type of tool (e.g. model checker, test generator):
Deductive verifier/verification architecture

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Given a program and its specification in Viper's intermediate language, it can either generate verification conditions, which are then passed to [Boogie](Boogie.md), or it can use symbolic execution to try and detect inconsistencies between the code and the specifications.

Uses [Z3](../Solvers/SMT/Z3.md).

#### Comments
- If it would only generate verification conditions for Boogie, it would have ended up on PV2.
- There is a VS Code extension for Viper.

#### URIs (github, websites, etc.):
Project page: https://www.pm.inf.ethz.ch/research/viper.html
Repositories: https://github.com/viperproject/
VS Code extension: https://github.com/viperproject/viper-ide

#### Last publication date:
2018

#### List of related papers:
[Automating Deductive Verification for Weak-Memory Programs](https://doi.org/10.1007/978-3-319-89960-2_11) (TACAS '18)
[Viper: A Verification Infrastructure for Permission-Based Reasoning](https://doi.org/10.1007/978-3-662-49122-5_2) (VMCAI '16)
[Automatic Verification of Iterated Separating Conjunctions Using Symbolic Execution](https://doi.org/10.1007/978-3-319-41528-4_22) (CAV '16)

#### Related tools (tools mentioned or compared to in the paper):
Verifiers built on top of Viper: [Gobra](../Gobra.md), [Nagini](../Nagini.md), [[Prusti]], [[Chalice]], [[VerCors]]
Tool to infer permission annotations for Viper programs: [Sample](../Sample.md)

#### Meta
:: Framework
:: PV3 :: detects inconsistencies between the code and spec with symbolic execution