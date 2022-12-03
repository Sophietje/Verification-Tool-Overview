Tool to generate tests that witness violations to atomicity or weaker consistency properties in concurrent objects.

#### Name:
Violat

#### Application domain/field:
Concurrency
Thread interleavings
Test generation
Atomicity

#### Type of tool (e.g. model checker, test generator):
Test generator

#### Expected input thing:
Program

#### Expected input format:
Name of a single Java class that is available on the classpath or in a user-provided JAR

#### Expected output:
Reports test results, signalling any discovered consistency violations.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
In principle Violat outputs a sequence of Java classes which can be tested with off-the-shelf back-end analysis engines.
It integrates with [JPF](Checkers/JPF.md) and [Java Concurrency Stress](jcstress.md), thus it is able to provide results directly.

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/michael-emmi/violat

#### Last commit date:
10 Apr 2022 (default branch)
10 Apr 2022 (last activity)

#### Last publication date:
12 July 2019

#### List of related papers:
[Violat: Generating Tests of Observational Refinement for Concurrent Objects](https://doi.org/10.1007/978-3-030-25543-5_30) (CAV '19)
[Weak-consistency specification via visibility relaxation](https://doi.org/10.1145/3290373) (POPL '19)
[Monitoring Weak Consistency](https://doi.org/10.1007/978-3-319-96145-3_26) (CAV '18)

#### Related tools (tools mentioned or compared to in the paper):
Test generation for concurrent objects: [[Ballerina]], [[ConTeGe]], [[ConSuite]], [[AutoConTest]], [[CovCon]], [[Omen]], [[Narada]], [[Intruder]], [[Minion]]
Test generation for memory consistency: [[TSOtool]], [[LCHECK]], [[CppMem]], [[Herd]], [[McVerSi]],

#### Meta
:: Concurrency
:: PV2 :: generates classes attempting to violate properties
:: Source :: https://doi.org/10.1007/978-3-319-96145-3 :: https://doi.org/10.1145/3550355.3552426
