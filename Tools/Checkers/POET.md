Explicit-state model checker

#### Name:
POET: Partial Order Exploration Tool

#### Application domain/field:
Partial order reduction
Net unfoldings
Model checking
State space exploration

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
Multi-threaded C program

#### Expected input format:
(Restricted fragment of the) C
- Can use `__poet_fail()` to indicate an assert false
- Supports POSIX threads

#### Expected output:
It can:
* "print the result of the front-end" (???)
* execute the system with a non-deterministic schedule
* perform explicit-state model checking

#### Internals (tools used, frameworks, techniques, paradigms, ...):
?

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/marcelosousa/poet
Web page for CONCUR '15 paper: https://www.cs.ox.ac.uk/people/marcelo.sousa/poet/

#### Last commit date:
19 Oct 2018 (default branch)
19 Oct 2018 (last activity)

#### Last publication date:
26 August 2015

#### List of related papers:
[Unfolding-based Partial Order Reduction](https://doi.org/10.4230/LIPIcs.CONCUR.2015.456) (CONCUR '15)

#### Related tools (tools mentioned or compared to in the paper):
Second version of POET is called [APOET](../APOET.md).
Compared to: [Nidhugg](../Nidhugg.md)

#### Meta
:: C
:: Concurrency
:: PV1 :: analyses a multi-threaded program to see if it conforms to expectations of the tool
:: Model checking
:: Source :: compared to [[Nidhugg]] :: https://doi.org/10.1145/3550355.3552426
