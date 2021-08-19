#### Name:
Origami

#### Application domain/field:
Networking
Network verification
Counterexample-guided abstraction refinement (CEGAR)

#### Type of tool (e.g. model checker, test generator):
Network verification tool

#### Expected input thing:
? (a network configuration, possibly a source and destination node)

#### Expected input format:
?

#### Expected output:
Network is verified successfully or a property violation is reported?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Origami can be used to verify reachability in networks in the presence of faults.

Origami first computes a small abstract network that satisfies certain SPPF (Stable Path Problems with Faults) effective approximation conditions. If this abstraction satisfies the desired property then the verification terminates successfully. If it could not be verified, then it checks whether the returned counterexample is an actual counterexample. If not, then a new abstraction is computed.

Uses [[Batfish]], [Z3](Z3.md)

#### Comments:
The goal of Origami is **scalability**, they want to be able to analyze large networks (e.g. 1000s of routers).

#### URIs (github, websites, etc.):
Repository (? linked on author's webpage): https://github.com/NetworkVerification/nv

#### Last commit date:

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25543-5_18

#### Related tools (tools mentioned or compared to in the paper):