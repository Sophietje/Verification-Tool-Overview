Separation logic-based multi-language verification architecture/framework.

It can be used to verify C and JavaScript code ([[Gillian-C]] and [[Gillian-JS]] respectively).

#### Name:
Gillian

#### Application domain/field:
Symbolic execution
Separation logic
Symbolic testing
Memory models

#### Type of tool (e.g. model checker, test generator):
Framework

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Gillian uses compositional memory models of JS and C.
Gillian does not seem to support reasoning about concurrent programs.

#### Comments:
License: BSD-3-Clause

#### URIs (github, websites, etc.):
Artifact for CAV '21: https://zenodo.org/record/4838116
Project page: https://gillianplatform.github.io/
Repository: https://github.com/GillianPlatform/Gillian

#### Last commit date:
23 April 2022

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_38 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Other multi-language verification frameworks: [[coreStar]], [Viper](Frameworks/Viper.md).
Verification tools for JS based on separation logic: [[JaVerT]]
Verification tools for C based on separation logic: [Verifast](Verifast.md)
The artefact description states that it "works in a close way to [[Klee]]'s"

#### Meta
:: C
:: JavaScript
:: PV5 :: verifies properties of a user-specified memory model