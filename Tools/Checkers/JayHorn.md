JayHorn is a model checker for verifying the absence of assertion violations in sequential Java programs by automatically inferring program annotations that are sufficient to witness program safety

#### Name:
JayHorn

#### Application domain/field:
Model checking
Sequential programs
Safety verification
Software model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
Program with assertions

#### Expected input format:
Java bytecode (it supports Java class files, Jar archives, or Android apk)

#### Expected output:
`SAFE`, `UNSAFE` or `UNKNOWN`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [[Eldarica]], [Spacer](Spacer.md) as back-end solvers and [[Soot]] to translate Java bytecode to simplified Jimple three-address format.

JayHorn can also infer some program annotations automatically for NullPointerExceptions, ArrayIndexOutOfBoundsExceptions and ClassCastExceptions.

#### Comments:
JayHorn does not support strings, enums, bounded integer data-types, floating-point data-types, reflection, dynamic loading, and concurrency

License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/jayhorn/jayhorn
Project page: https://jayhorn.github.io/jayhorn/

#### Last commit date:
27 May 2021

#### Last publication date:
23 March 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-72013-1_29 (TACAS '21)
https://doi.org/10.1145/3340672.3341113 (FTfJP '19)
https://doi.org/10.1007/978-3-030-17502-3_16 (TACAS '19)
https://doi.org/10.1007/978-3-319-41528-4_19 (CAV '16)

#### Related tools (tools mentioned or compared to in the paper):
-