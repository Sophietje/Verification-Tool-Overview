#### Name:
Murxla

#### Application domain/field:
SMT solving
Fuzzing
API fuzzing

#### Type of tool (e.g. model checker, test generator):
Fuzzer for SMT solvers

#### Expected input thing:
- SMT solver
- *Optional*: solver profile which defines what theories/operators are supported

#### Expected input format:
- *SMT solver*: If it is natively integrated, one simply needs to pass an argument when calling Murxla. Otherwise, one needs to pass an argument that links to an executable script that calls the SMT solver.
- *Solver profile*: `.json`file, see also: https://murxla.github.io/docs/solver_integration/solver_profile.html

#### Expected output:
API trace file if an issue is encountered. 
This trace file can be replayed (and minimized) to trigger the issue.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Murxla is a model-based API fuzzer for SMT solvers, i.e. it tries to find bugs in SMT solvers via fuzzing. It generates valid sequences of solver API calls. It provides support to record, minimize and replay such traces.

Murxla currently supports the following SMT solvers: [Bitwuzla](../../Tools/Solvers/SMT/Bitwuzla.md), [Boolector](../../Tools/Solvers/SMT/Boolector.md), [cvc5](../../Tools/Solvers/SMT/cvc5.md), [Yices](../../Tools/Solvers/SMT/Yices.md)

Murxla supports two modes: continuous and one-shot. Continuous can be used to continuously fuzz an SMT solver until (1) it is interrupted or (2) the specified maximum number of test runs were performed. This is typically used to find solver errors.
In one-shot mode, Murxla performs a single test run. This can be done using either a specific seed or an API trace. This is typically used to inspect a specific test run in detail, i.e. debugging purposes.
Murxla also provides options to replay and minimize traces.

#### Comments:
-

#### URIs (github, websites, etc.):
- CAV '22 Artifact: https://zenodo.org/record/6494381.
- Project page: https://murxla.github.io/
- Documentation: https://murxla.github.io/docs/index.html
- Repository: https://github.com/murxla/murxla

#### Last commit date:
24 February 2023
06 Apr 2023 (last activity)

#### Last publication date:
6 August 2022

#### List of related papers:
[Murxla: A Modular and Highly Extensible API Fuzzer for SMT Solvers](https://doi.org/10.1007/978-3-031-13188-2_5) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Other fuzzers for the [SMT-LIB](../../Formats/SMT-LIB.md) language: [[FuzzSMT]], [[Storm]], [[TypeFuzz]]

#### Meta
:: SMT
:: PV1 :: fuzzer for SMT solvers
