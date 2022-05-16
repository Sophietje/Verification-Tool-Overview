#### Name:
Java Pathfinder (aka jpf-core, aka JPF)

#### Application domain/field:
Model checking
Software model checking
Bytecode

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Java program (possibly with annotations)
- *Optionally*: configuration files

#### Expected input format:
- `.class` or `.java` (Java program)
- `.jpf` file, `jpf.properties` file, `.jpf/site.properties` file (for application properties, project properties and site properties respectively)

#### Expected output:
The system can report on 3 different things:
1. System under test (SUT) output: what is the SUT doing?
2. JPF logging: what is JPF doing?
3. JPF reporting system: result of the JPF run

The last option is probably the most interesting for users. This will report any property violations.
Per property violation it can show the type of error, a trace leading to the violation, give a snapshot of all threads when the violation occurs, show the program output for the trace and some statistics.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Software model checker for Java bytecode programs

#### Comments:
It is possible to run Java Pathfinder from within NetBeans or Eclipse (with and without a plugin) as well as from a Java program or the command line.

#### URIs (github, websites, etc.):
Repository: https://github.com/javapathfinder/jpf-core
Wiki: https://github.com/javapathfinder/jpf-core/wiki

#### Last commit date:
11 May 2021

#### Last publication date:
4 April 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-17502-3_18

#### Related tools (tools mentioned or compared to in the paper):
The wiki contains a list of tools that use JPF: https://github.com/javapathfinder/jpf-core/wiki/Projects

#### Meta
:: Java
:: PV3           :: checks properties of annotated Java code
:: Model checking