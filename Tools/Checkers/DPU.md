#### Name:
DPU: Dynamic Program Unfolder

#### Application domain/field:
Model checking
Partial-order reduction

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
A POSIX multi-threaded program

#### Expected input format:
C program that is data-deterministic

#### Expected output:
Whether it has detected any assertion violations, abort calls, exit calls with a non-zero exit code, data races or deadlocks.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Stateless model checker for C programs with POSIX threading

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/cesaro/dpu

#### Last commit date:
18 March 2018

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_22

#### Related tools (tools mentioned or compared to in the paper):
Mentioned in the README of the repository: [POET](POET.md), [Nidhugg](../Nidhugg.md), [[CHESS]], and [[Maple]]

#### Meta
:: C
:: Concurrency
:: PV1           :: borderline PV2 (relies on user-driven assertions) but mostly works with assumed properties