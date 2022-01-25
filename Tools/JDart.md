JDart performs dynamic symbolic execution of Java programs: it executes programs with concrete inputs while recording symbolic constraints on executed program paths. A constraint solver is then used for generating new concrete values from recorded constraints that drive execution along previously unexplored paths. 

#### Name:
JDart

#### Application domain/field:
Dynamic symbolic execution
Java programs
Constraint solver
Concolic execution

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
- Program annotated with assertions
- Analysis configuration

#### Expected input format:
- *Program*: `.java`
- *Analysis configuration*: jpf application properties file (`.jpf` file)

#### Expected output:
Reports assertion violations

#### Internals (tools used, frameworks, techniques, paradigms, ...):
JDart is built on top of the [JPF](Checkers/JPF.md) software model checker and uses the [JConstraints](Libraries/JConstraints.md) library for the integration of constraint solvers.

#### Comments:
License: Apache-2.0

#### URIs (github, websites, etc.):
Original repository: https://github.com/psycopaths/jdart
Documentation (from original repository): https://github.com/psycopaths/jdart/wiki
Repository: https://github.com/tudo-aqua/jdart

#### Last commit date:
26 November 2019

#### Last publication date:
17 April 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-45237-7_28 (TACAS '20)
https://doi.org/10.1007/978-3-662-49674-9_26 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
Other tools that participated in the JavaOverall category of SV-COMP in 2020: [[Java-Ranger]], [JBMC](Checkers/JBMC.md), [COASTAL](COASTAL.md), [JayHorn](Checkers/JayHorn.md)[SPF](SPF.md)

#### Meta
:: Java
:: PV2           :: checks properties of annotated Java code with dynamic symbolic execution