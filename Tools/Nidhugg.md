Stateless model checker (SMC) for C/C++ programs

#### Name:
Nidhugg

#### Application domain/field:
Model checking
Stateless model checking
Concurrency
Concurrent programs
Relaxed memory models

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Multithreaded C/C++ program
	- Each thread should be deterministic when run in isolation.
	- The concurrency should be implemented with pthreads.
- Memory model

#### Expected input format:
- *Program*: `.ll` file (LLVM assembly code)
- *Memory model*: This is passed as an argument when calling Nidhugg. It can be one of the following: `--sc`, `--tso`, `--pso`, `--power`, `--arm`.

#### Expected output:
It will indicate an error or state that no errors were found.
The errors can be either assertion violations or robustness violations (e.g. segmentation faults).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It supports the following memory models: SC, TSO, PSO, POWER and ARM.

Nidhugg explores the possible executions to find bugs. It does this such that it will not explore executions that are equivalent to each other. 

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/nidhugg/nidhugg

#### Last commit date:
13 December 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_16 (CAV '21)
https://doi.org/10.1145/3360576 (OOPSLA '19)
https://doi.org/10.1007/s00236-016-0275-0 (Extended version of TACAS '15 paper, Acta Informatica '17)
https://doi.org/10.1007/978-3-662-46681-0_28 (TACAS '15)

#### Related tools (tools mentioned or compared to in the paper):
Other stateless model checkers: [GenMC](Checkers/GenMC.md), [[RCMC]], [[CDSChecker]]

#### Meta
:: C
:: C++
:: Model checking
:: Concurrency