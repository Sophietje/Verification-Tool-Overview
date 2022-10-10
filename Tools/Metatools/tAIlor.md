automatically tailors an abstract interpreter to the code under analysis and any given resource constraints

#### Name:
tAIlor (tailor)

#### Application domain/field:
Configuration
Abstract interpretation

#### Type of tool (e.g. model checker, test generator):
Metatool

#### Expected input thing:
Program

#### Expected input format:
?

#### Expected output:
Configuration for [Crab](Libraries/Crab.md) abstract interpreter

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Tailor will automatically tune the [Crab](Libraries/Crab.md) abstract interpreter to the code under analysis and any given resource constraints.
It specifically focuses on *time* as the constrained resource.

#### Comments:
License: Apache v2.0

#### URIs (github, websites, etc.):
Repository: https://github.com/Practical-Formal-Methods/tailor
Artifact for CAV '21: https://zenodo.org/record/4719604

#### Last commit date:
24 November 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[Automatically Tailoring Abstract Interpretation to Custom Usage Scenarios](https://doi.org/10.1007/978-3-030-81688-9_36) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV2 :: generates a configuration for an abstract interpreter from constraints