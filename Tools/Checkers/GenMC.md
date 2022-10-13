LLVM-based stateless model checker (SMC) for concurrent C/C++ programs

#### Name:
GenMC

#### Application domain/field:
Model checking
Stateless model checker (SMC)
Concurrent programs
Concurrency
Memory models

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- C/C++ program that 
	- **uses stdatomic.h and/or pthread.h** APIs for concurrency
	- needs to be **finite** (i.e. all tests need to have finite traces, so no infinite loops)
	- needs to be **data-deterministic** (i.e. all non-determinism should originate from the scheduler or the employed memory model, can't use actions like `rand()` or perform actions based on user input or the clock)
- *Optional*: specifications in the form of assertions in the code
- *Optional*: assumptions to reduce the state space (in the `__VERIFIER_assume()` syntax)
- *Optional*: memory model, the default is the RC11 memory model

#### Expected input format:
`.c` file

#### Expected output:
Any safety error that are detected will be reported. 
These errors can include data races on non-atomic variables, memory errors (e.g. double-free error) and assertion violations.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Given a C/C++ program as inputs (that uses C/C++11 atomics and/or concurrency primitives from the pthread library), it reports any data races, assertion violations, or other errors encountered.
The verification can be performed with respect to the RC11 memory model (default), or other models such as IMM and LKMM.

#### Comments:
- License: GPL-3.0 License
- GenMC has PV3 features (checks assertions), PV4 features (infers provable properties from goals like data race), and PV5 features (when used with a non-RC11 memory model).

#### URIs (github, websites, etc.):
Project page: https://plv.mpi-sws.org/genmc/
Repository: https://github.com/mpi-sws/genmc/

#### Last commit date:
22 Feb 2022

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_20 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: LLVM
:: C
:: C++
:: PV5 :: given a C program with assertions and a memory model spec, reports safety errors
:: Model checking