#### Name:
ATHOS: Asynchronous to HO Synchronizer

#### Application domain/field:
Verification
Asynchronous fault-tolerant distributed systems

#### Type of tool (e.g. model checker, test generator):
Rewriter/translator

#### Expected input thing:
- Asynchronous fault-tolerant protocol, e.g. a leader election protocol, in a C embedding of the language specified in the paper
- Configuration file

#### Expected input format:
*Protocol*: C embedding of their language. Be aware:
- can only contain C99-like syntactic constructions
- all code has to be in a `main()` function
- directives and headers are not supported
- `if` and `else` tokens are followed by curly braces

*Configuration file:* .py file

#### Expected output:
Round-based synchronous protocol (C file) that is the counterpart of the input (the asynchronous version)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Verifast](Verifast.md)

#### Comments
Reduces the verification of asynchronous fault-tolerant protocols to the verification of round-based synchronous protocols.

The Github repository contains examples of configuration files and protocols.

#### URIs (github, websites, etc.):
https://github.com/alexandrumc/async-to-sync-translation

#### Last commit date:
28 Apr 2020 (last activity)

#### Last publication date:
12 July 2019

#### List of related papers:
[Communication-Closed Asynchronous Protocols](https://doi.org/10.1007/978-3-030-25543-5_20)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: C
:: Protocol
:: PV2 :: computes the synchronous counterpart of an asynchronous protocol
:: Source :: https://doi.org/10.1007/978-3-030-25543-5 :: https://doi.org/10.1145/3550355.3552426
