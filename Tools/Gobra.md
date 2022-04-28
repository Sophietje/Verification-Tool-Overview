Deductive program verifier for Go that proves memory safety, crash safety, data-race freedom, and user-provided specifications.

#### Name:
Gobra

#### Application domain/field:
Deductive verification
Memory safety
Data-race freedom
Functional correctness
Separation logic

#### Type of tool (e.g. model checker, test generator):
Deductive program verifier

#### Expected input thing:
Go program with specifications

#### Expected input format:
`.gobra` file
Specifications should be written in the form of assertions (preconditions, postconditions, loop invariants, predicates) in the program code.

#### Expected output:
If verification fails, then it will report on the level of the Go program, what assertions could not be proven.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Gobra takes an annotated Go program as input. It will then encode this annotated program into the intermediate verification language [Viper](Frameworks/Viper.md) and apply an existing SMT-based verifier.
If verification fails, then it will report on the level of the Go program, what assertions could not be proven.

#### Comments:
License: Mozilla Public License version 2.0 with exceptions for some files.

#### URIs (github, websites, etc.):
Artifact CAV '21: https://zenodo.org/record/4716664
VSCode plugin: https://github.com/viperproject/gobra-ide
Project page: https://www.pm.inf.ethz.ch/research/gobra.html
Repository: https://github.com/viperproject/gobra
Zulip organization for discussions: https://gobra.zulipchat.com/login/
Tutorial: https://github.com/viperproject/gobra/blob/master/docs/tutorial.md

#### Last commit date:
13 December 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_17 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Other verification approaches for Go: [[Perennial]]
Other [Viper](Frameworks/Viper.md)-based verifiers: [Nagini](Nagini.md), [[Prusti]], [[VerCors]].

#### Meta
:: Go
:: PV4 :: checks memory safety, crash safety, data-race freedom, and user-provided specifications for Go programs