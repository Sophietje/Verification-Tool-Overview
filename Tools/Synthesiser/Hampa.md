#### Name:
Hampa

#### Application domain/field:
Replicated objects
Synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Replicas are often used for fault-tolerance, availability, responsiveness and scalability. We need some kind of coordination between replicated objects, e.g. using consensus protocols, to keep all objects up-to-date/synchronised. This tool provides a correct-by-construction replicated object that guarantees (1) integrity, (2) convergence, and (3) recency. This replicated object is automatically synthesized based on a given sequential object with the declaration of its integrity and recency requirements.

Uses [CVC4](../Solvers/SMT/CVC4.md).

#### Comments:

#### URIs (github, websites, etc.):
Artifact: https://github.com/XiaoLi0614/HampaAE

#### Last commit date:
22 Apr 2020 (last activity)

#### Last publication date:
14 July 2020

#### List of related papers:
[Hampa: Solver-Aided Recency-Aware Replication](https://doi.org/10.1007/978-3-030-53288-8_16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Synthesis
:: PV2 :: synthesises a replicated object that guarantees integrity, convergence and recency
:: Source :: https://doi.org/10.1145/3550355.3552426
