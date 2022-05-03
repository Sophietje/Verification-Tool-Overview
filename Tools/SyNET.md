Synthesises network wide configurations given forwarding requirements.

#### Name:
SyNET

#### Application domain/field:
Computer networks
Network configuration

#### Type of tool (e.g. model checker, test generator):
Synthesis tool for network configurations

#### Expected input thing:
- Topology of the network
- Requirements
- Routing protocol

#### Expected input format:
- *Network topology*: set of Datalog predicates, `.logic` file
- *Requirements*: `.logic` file
- *Routing protocol*: passed as an argument, the user can choose between `static`, `ospf` or `bgp`. 

#### Expected output:
Datalog input that results in a forwarding state satisfying the requirements. From this Datalog input one can derive the configurations for routers.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md) to check whether the generated SMT constraints are satisfiable and to obtain a model.

#### Comments:
License: Apache v2.0

#### URIs (github, websites, etc.):
Project page: https://synet.ethz.ch/
Repository: https://github.com/nsg-ethz/synet

#### Last commit date:
7 December 2017

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63390-9_14 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
Tools that produce network-wide configurations from routing requirements: [[Propane]], [[Genesis]], [[ConfigAssure]]

#### Meta
:: Computer network
:: PV2 :: generates configurations for routers such that given requirements are satisfied