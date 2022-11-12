#### Name:
SPIN

#### Application domain/field:
Multi-threaded software
Model checking
Simulation
Concurrency

#### Type of tool (e.g. model checker, test generator):
Model checker + simulator

#### Expected input thing:
- System description
- Properties: can be expressed as system or process invariants (using assertions), as linear temporal logic (LTL) requirements, as Büchi automata, or as omega-regular properties.

#### Expected input format:
[PROMELA](../Formats/PROMELA.md)

#### Expected output:
It reports on deadlocks, race conditions, different types of incompleteness, unwarranted assumptions about the relative speed of processes, and property violations.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Spin is a open-source software verification tool for formal verification of multi-threaded software applications. It can be used in four main modes:

- as a **simulator**, allowing for rapid prototyping with a random, guided, or interactive simulations
- as an **exhaustive verifier**, capable of rigorously proving the validity of user specified correctness requirements (using partial order reduction theory to optimize the search)
- as **proof approximation system** that can validate even very large system models with maximal coverage of the state space.
- as a driver for **swarm verification** (a new form of swarm computing that can exploit cloud networks of arbitrary size), which can make optimal use of large numbers of available compute cores to leverage parallelism and search diversification techniques, which increases the chance of locating defects in very large verification models.

(source: https://spinroot.com/spin/what.html)

#### Comments:
License: BSD 3-clause open source license

#### URIs (github, websites, etc.):
Repository: https://github.com/nimble-code/Spin
Project page: https://spinroot.com/

#### Last commit date:
15 January 2022

#### Last publication date:
2012

#### List of related papers:
[Parallelizing the Spin Model Checker](https://doi.org/10.1007/978-3-642-31759-0_12) (SPIN '12)
[Model checking with bounded context switching](https://doi.org/10.1007/s00165-010-0160-5) (Formal Aspects of Computing, 2011)
Principles of the Spin Model Checker (ISBN: 978-1846287695, 2008)
The Spin Model Checker: Primer and Reference Manual (ISBN: 978-0321228628, 2003)
[The model checker SPIN](https://doi.org/10.1109/32.588521) (IEEE Trans. on Software Engineering, 1997)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Concurrency
:: LTL
:: PV5 :: analyses models of multi-threaded applications with different message passing paradigms or shared memory communication
:: Simulation
:: Model checking
:: Source :: https://doi.org/10.1145/3550355.3552426