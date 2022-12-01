Model checking tool for consensus algorithms formulated in the ConsL language

#### Name:
Consensus Verifier

#### Application domain/field:
Consensus algorithms
Fault-tolerant distributed systems

#### Type of tool (e.g. model checker, test generator):
Specification/model translator?

#### Expected input thing:
Consensus algorithm

#### Expected input format:
ConsL (own) language

#### Expected output:
PROMELA/Spin model

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The tool automatically translates a ConsL algorithm into appropriate [PROMELA](../Formats/PROMELA.md) models and LTL properties for the [SPIN](SPIN.md) model checker.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://www.infsec.ethz.ch/research/software/consl-verifier

#### Last commit date:
-

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63390-9_12 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV4 :: translates a consensus algorithm into a PROMELA model and LTL properties
:: Model checking
:: Source :: https://doi.org/10.1145/3550355.3552426
