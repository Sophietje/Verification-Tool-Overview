Reachability analysis for AWS-based networks

#### Name:
TIROS

#### Application domain/field:
Reachability analysis
Cloud networks

#### Type of tool (e.g. model checker, test generator):
Reachability checker

#### Expected input thing:
- Model of the network, consisting of:
	- *Formal specification*: formalizes the semantics of the AWS networking components, e.g. in which order a firewall applies rules, and how load balancers route traffic
	- *Snapshot*: describes the topology and details of the network
- Query

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Soufflé](Not-verifiers/Soufflé.md), [MonoSAT](Solvers/SMT/MonoSAT.md) and [Vampire](Provers/Vampire.md).

Should be able to answer queries such as "list all open paths from the Internet to any instance in the VPC (Virtual Private Cloud)"

#### Comments:
Used by Amazon Web Services (AWS). It encodes the semantics of the entire AWS cloud network service stack. It has been made to scale well to networks of hundreds of thousands of instances, routers and firewall rules.

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25543-5_14 (CAV '19)

#### Related tools (tools mentioned or compared to in the paper):
Tools that analyse software-defined-network (SDN) programs: [[VeriCon]], [[NICE]], [[VeriFlow]], [[SecGuru]]
Tools based on model checking: [[Anteater]], [[ConfigChecker]]
Tools that analyse networks with a similar Datalog approach: [Batfish](Batfish.md), [SyNET](SyNET.md)

#### Meta
:: Computer network
:: PV3 :: checks user-specified queries for AWS-based networks