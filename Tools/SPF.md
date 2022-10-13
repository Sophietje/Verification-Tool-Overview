Symbolic Pathfinder (SPF) is a program analysis tool for Java bytecode; the tool is based on symbolic execution

#### Name:
SPF: Symbolic PathFinder

#### Application domain/field:
Symbolic execution
Model checking
Automated test case generation

#### Type of tool (e.g. model checker, test generator):
Symbolic executor

#### Expected input thing:
- Java bytecode program
- Configuration file specifying, e.g. which methods should be executed symbolically

#### Expected input format:
- *Java bytecode program*: `.class`
- *Configuration file*: `.jpf`

#### Expected output:
Test suite (test inputs or test sequences) and/or counterexamples for the failed properties

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
License: Apache License v2.0

#### URIs (github, websites, etc.):
Repository: https://github.com/SymbolicPathFinder/jpf-symbc

#### Last commit date:
10 Sep 2022

#### Last publication date:
4 April 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-17502-3_21 (TACAS '19)
https://doi.org/10.1007/s10515-013-0122-2 (ASE '13)
https://doi.org/10.1145/1858996.1859035 (ASE '10)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Java
:: Binary level
:: PV3           :: checks properties of annotated Java code with static symbolic execution