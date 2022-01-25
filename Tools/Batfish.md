#### Name:
Batfish

#### Application domain/field:
Networks
Network configuration

#### Type of tool (e.g. model checker, test generator):
Configuration testing tool

#### Expected input thing:
- Network configuration
- Network topology
- User-defined properties that should be checked

#### Expected input format:
- *Network configuration*: in the configuration language of Cisco IOS, Cisco NXOS, Juniper JunOS, Arist or Quanta.
- *Network topology:* ?
- *User-defined properties*: first-order logic formula

#### Expected output:
- User can query the system about control and data planes
- It can provide a counterexample in case of a property violation

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses Network Optimized Datalog ([[NoD]])

#### Comments:
Tool to detect network configuration errors

The tool checks for some default properties such as:

- Absence of black holes and loops
- Multipath consistency: all packets with the same header should be treated identically in terms of being accepted or dropped, regardless of the path taken through the network
- Failure consistency: Consider a network E. If a package is accepted by network E, then it should also be accepted in an identical network E' where some nodes/links are considered failed. (This is for testing the fault tolerance of a network)
- Destination consistency: A customer AS can only send route announcements for its own address, ensuring that it only receives packets destined to itself.

#### URIs (github, websites, etc.):
https://www.batfish.org/
https://github.com/batfish/batfish

#### Last commit date:
28 May 2021

#### Last publication date:
2015

#### List of related papers:
https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-fogel.pdf

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Datalog
:: Computer network
:: PV2           :: checks properties of networks