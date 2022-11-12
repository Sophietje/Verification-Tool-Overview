#### Name:
DEEPSEC: Deciding Equivalence Properties in Security Protocols

#### Application domain/field:
Security protocol analysis
Cryptographic protocols

#### Type of tool (e.g. model checker, test generator):
Security protocol verifier

#### Expected input thing:
Cryptographic primitives, the protocol and the security properties that should be verified.

#### Expected input format:
Its own `.dps` format

#### Expected output:
Whether two specified processes are trace equivalent or not.
If the query is not satisfied, the interface shows "how to mount the attack" (i.e. a counterexample).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
DEEPSEC decides trace equivalence for cryptographic protocols specified in a dialect of the applied pi calculus.

#### Comments:
The analysis is restricted to a finite number of protocol sessions.

#### URIs (github, websites, etc.):
Project page: https://deepsec-prover.github.io/
Manual: https://deepsec-prover.github.io/manual/
Repository: https://github.com/DeepSec-prover/deepsec
Repository for the UI: https://github.com/DeepSec-prover/deepsec_ui

#### Last commit date:
23 July 2020

#### Last publication date:
4 February 2020

#### List of related papers:
[DEEPSEC: Deciding Equivalence Properties in Security Protocols Theory and Practice](https://doi.org/10.1109/SP.2018.00033)
[Exploiting Symmetries When Proving Equivalence Properties for Security Protocols](https://doi.org/10.1145/3319535.3354260)
[The DEEPSEC Prover](https://doi.org/10.1007/978-3-319-96142-2_4)
[On the semantics of communications when verifying equivalence properties](https://doi.org/10.3233/JCS-191366)

#### Related tools (tools mentioned or compared to in the paper):
Other security verifiers: [[SPEC]], [[APTE]], [[Akiss]], [[Sat-Eq]], 

#### Meta
:: Security
:: Protocol
:: PV1 :: checks whether two cryptographic protocols are trace equivalent
:: Source :: https://doi.org/10.1145/3550355.3552426