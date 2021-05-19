#### Name:
AMUSIC: Approximate Minimal Unsatisfiable Subsets Implicit Counter

#### Application domain/field:
Minimal unsatisfiable sets (MUSes)

#### Type of tool (e.g. model checker, test generator):
Counting tool?

#### URIs (github, websites, etc.):
https://github.com/jar-ben/amusic

#### Expected input:
- Boolean formula in CNF
- Tolerance parameter ε
- Confidence parameter δ

#### Expected output:
Estimate of the amount of MUSes guaranteed to be within (1+ε)-multiplicative factor of the exact count with confidence at least 1-δ

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Tool for approximate counting of minimal unsatisfiable subets of a given Boolean formula in CNF

Uses [[CAQE]], [[CADET]], [[QRATPre+]], [[muser2]], [[UWrMaxSat]], [[pysat]]

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_21