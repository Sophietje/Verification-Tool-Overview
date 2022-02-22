#### Name:
xSAP: eXtended Safety Assessment Platform

#### Application domain/field:
Synchronous transition systems
Model-based safety assessment (MBSA)
Fault tree analysis
Model checking

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Nominal model
- Fault Extension Instructions (FEI)

#### Expected input format:
- *Nominal model*: SMV language
- *Fault Extension Instructions*: dedicated FEI language

#### Expected output:
Depends on the analysis that was chosen.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [nuXmv](Checkers/nuXmv.md) model checker.
Some parts of xSAP are used as a back-end for [COMPASS](Frameworks/COMPASS.md).

It implements several types of model analyses, including:
- Fault Tree Analysis (FTA)
- Failure Mode and Effects Analysis (FMEA)
- Failure propagation analysis using Timed Failure Propagation Graphs (TFPGs)
- Common Cause Analysis (CCA)

#### Comments:
xSAP is a re-implementation of FSAP.

#### URIs (github, websites, etc.):
Project page: https://xsap.fbk.eu/

#### Last commit date:
28 June 2021 (last release date)

#### Last publication date:
March 2021

#### List of related papers:
https://doi.org/10.1007/s00165-021-00532-9 ('21, Formal Aspects of Computing, Vol. 33 Iss. 2, case study)
https://doi.org/10.1007/978-3-030-54549-9_7 (SAFECOMP '20)
https://doi.org/10.1007/978-3-662-49674-9_31 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
Other platforms for model-based safety assessment: [[Altarica/OCAS]], [[Scade]], [[Statemate]]

#### Meta
