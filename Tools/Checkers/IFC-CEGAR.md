#### Name:
IFC-CEGAR

#### Application domain/field:
Security verification
Information flow

#### Type of tool (e.g. model checker, test generator):
Model checker?

#### Expected input thing:
- Program
- Set of high-security variables

#### Expected input format:
C-program with annotations indicating the secret variables and the locations at which leaks should be checked.

#### Expected output:
`SAFE`, `UNSAFE` or `UNKNOWN`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Procedure for unbounded verification of secure information flow. It uses taint analysis and self-composition.
- Implemented on top of [SeaHorn](SeaHorn.md), uses [Spacer](../Solvers/Spacer.md) ([Z3](../Solvers/SMT/Z3.md)'s CHC solver).
- Note that the paper calls this a 'prototype implementation'.

#### Comments:

#### URIs (github, websites, etc.):
Benchmark files: http://www.cs.princeton.edu/~aartig/benchmarks/ifc_bench.zip

#### Last commit date:
-

#### Last publication date:
18 July 2018

#### List of related papers:
[Lazy Self-composition for Security Verification](https://doi.org/10.1007/978-3-319-96142-2_11) (CAV 2018)

#### Related tools (tools mentioned or compared to in the paper):
[IFC-BMC](IFC-BMC.md)

#### Meta
:: C
:: Security
:: PV4 :: checks if a program is safe with respect to variables marked secret