an extension of [Symbolic PathFinder](SPF.md) for veritesting and summarising dynamically dispatched methods and exceptional control-flow.

#### Name:
Java Ranger

#### Application domain/field:
Symbolic execution

#### Type of tool (e.g. model checker, test generator):
Symbolic execution tool

#### Expected input thing:
- Java code
- Configurations for the analysis

#### Expected input format:
- *Classpath*: classpath of target code, given as an argument when calling Java Ranger
- *Configurations*, all arguments when calling Java Ranger:
	- `veritestingMode = \<1-5\>` indicating which path-merging features should be enabled
	- `performanceMode = \<true or false\>`
	- `jitAnalysis = \<true or false\>`
	- `recursiveDepth = \<integer value\>`

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
License: Apache License v2.0

#### URIs (github, websites, etc.):
Repository: https://github.com/vaibhavbsharma/java-ranger
Project page: https://vaibhavbsharma.github.io/java-ranger/

#### Last commit date:
7 December 2021

#### Last publication date:
-

#### List of related papers:
https://doi.org/10.1007/978-3-030-45237-7_27 (TACAS '20)

#### Related tools (tools mentioned or compared to in the paper):
[Symbolic PathFinder](Symbolic%20PathFinder)

#### Meta
:: Java
:: PV3 :: checks properties of annotated Java code with static symbolic execution