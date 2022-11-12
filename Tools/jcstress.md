Java Concurrency Stress executes tests concurrently and tries to identify reorderings or contract violations for concurrent code.

#### Name:
Java Concurrency Stress (jcstress)

#### Application domain/field:
Concurrency
Testing

#### Type of tool (e.g. model checker, test generator):
Testing framework

#### Expected input thing:
*Optional:* name of the specific test that should be run. Otherwise it runs all tests.

#### Expected input format:
Text argument when executing the JAR file of jcstress.

#### Expected output:
An HTML report with the test results. This includes how many tests failed (either because a strong assertion was violated, or some other reason), and 'interesting' tests.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Testing tool to ensure correctness of concurrency support in the JVM. It has a suite of tests that can be used for research in the correctness of concurrency support in the JVM, class libraries, and hardware. It can be used as a library as well.
Note that jcstress can require significant time to catch all errors.

#### Comments:
Part of the Code Tools project, this is a project that provides tools for developers who work on the OpenJDK code base.

#### URIs (github, websites, etc.):
Repository: https://github.com/openjdk/jcstress
Project page: https://openjdk.java.net/projects/code-tools/jcstress/

#### Last commit date:
12 July 2021

#### Last publication date:
-

#### List of related papers:
-

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Java
:: Concurrency
:: PV1 :: executes test cases in an order that may lead to faults
:: Source :: https://doi.org/10.1145/3550355.3552426