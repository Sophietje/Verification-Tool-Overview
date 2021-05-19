#### Name:
ATHOS

#### Application domain/field:
Verification
Asynchronous fault-tolerant distributed systems

#### Type of tool (e.g. model checker, test generator):
Rewriter/translator

#### URIs (github, websites, etc.):
https://github.com/alexandrumc/async-to-sync-translation

#### Expected input:
- Asynchronous fault-tolerant protocol, e.g. a leader election protocol, in a C embedding of the language specified in the paper
- Configuration file

#### Expected output:
- Round-based synchronous protocol that is the counterpart of the input (the asynchronous version)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Reduces the verification of asynchronous fault-tolerant protocols to the verification of round-based synchronous protocols.

Uses [[Verifast]]

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25543-5_20
