#### Name:
AllRepair

#### Application domain/field:
Fault localization
Automated program repair

#### Type of tool (e.g. model checker, test generator):
Program repair

#### Expected input:
Program with assertions

#### Expected input format:
C program, assertions written as `__CPROVER_assert(..)`

#### Expected output:
List of all minimal repairs such that all assertions are true.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
SMT solver

#### Comments
Mutation-based repair tool for C programs equipped with assertions

The proposed repairs are minimal in the number of changes applied to the program code.

#### URIs (github, websites, etc.):
https://github.com/batchenRothenberg/AllRepair

#### Last commit date:
8 March 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53291-8_33 (CAV 2020)
https://doi.org/10.1007/978-3-319-48989-6_36 (FM 2016)

#### Related tools (tools mentioned or compared to in the paper):
Automated repair tools: [[Angelix]], [[GenProg]], [[FoRenSiC]], [[Maple]]

#### Meta
:: C
:: SMT
:: Program repair
:: PV2 :: proposes minimal repairs to the source code to satisfy properties