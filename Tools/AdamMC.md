#### Name:
AdamMC

#### Application domain/field:
Software-defined networks
Petri nets

#### Type of tool (e.g. model checker, test generator):
Model checker

#### URIs (github, websites, etc.):
https://uol.de/en/csd/adammc

#### Expected input:
One of the following three options:
1. Software-defined network and a Flow-LTL formula
2. Petri net with transits and a Flow-LTL formula
3. Petri net and a LTL formula

#### Expected output:
Verified or a counterexample

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Model checker for Petri nets with transits against Flow-LTL
Transit relations are used to follow the flow induced by tokens.
Flow-LTL is a temporal logic to specify local flow of data and global behavior or markings.

Uses [[ABC]], [[MCHyper]]
Based on [[Adam]]

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53291-8_5
