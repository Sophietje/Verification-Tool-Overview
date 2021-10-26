#### Name:
IFC-BMC

#### Application domain/field:
Security verification
Information flow

#### Type of tool (e.g. model checker, test generator):
Model checker?

#### Expected input thing:
- Program
- Set of high-security variables
- Maximum unrolling bound

#### Expected input format:
C-program with annotations that indicate which variables are secret and the locations at which leaks should be checked.

#### Expected output:
`SAFE`, `UNSAFE` or `UNKNOWN`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Procedure for bounded verification of secure information flow.

Implemented on top of [[SeaHorn]], uses [[Z3]].
 Note that the paper calls this a 'prototype implementation'.

#### Comments:

#### URIs (github, websites, etc.):
Benchmark files: http://www.cs.princeton.edu/~aartig/benchmarks/ifc_bench.zip

#### Last commit date:
-

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_11

#### Related tools (tools mentioned or compared to in the paper):
[[IFC-CEGAR]]