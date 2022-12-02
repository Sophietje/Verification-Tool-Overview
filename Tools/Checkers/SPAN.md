"... [A] formal verification engine for model checking indistinguishability (trace equivalence) and state-based safety properties of randomized security protocols in the symbolic model."

#### Name:
SPAN: Stochastic Protocol Analyzer

#### Application domain/field:
Randomized security protocols
Model checking
Security protocols

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Protocol P
- Protocol P'

#### Expected input format:
?

#### Expected output:
`true` or `false` indicating whether two randomized security protocols are indistinguishable.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [[KISS]], [[AKISS]], [Maude](../../Formats/Maude.md), [Apfloat](../Libraries/Apfloat.md)

#### Comments:

#### URIs (github, websites, etc.):
Repository: https://github.com/bauer-matthews/SPAN

#### Last commit date:
20 Apr 2018 (default branch)
22 May 2019 (last activity)

#### Last publication date:
18 July 2018

#### List of related papers:
[Model Checking Indistinguishability of Randomized Security Protocols](https://doi.org/10.1007/978-3-319-96142-2_10)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Security
:: PV1           :: computes whether two protocols are indistinguishable
:: Protocol
:: Source :: https://doi.org/10.1145/3550355.3552426
