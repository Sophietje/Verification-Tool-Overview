Tool that supports modelling, simulation and verification (model checking) for extended timed-arc Petri nets

#### Name:
TAPAAL

#### Application domain/field:
Timed-Arc Petri Nets (TAPNs)
Simulation
Model checking

#### Type of tool (e.g. model checker, test generator):
Framework/model checking for timed-arc petri nets

#### Expected input thing:
- Model
- Query (it supports the operators EF, EG, AF and AG)

#### Expected input format:
- *Model*: to be constructed in the TAPAAL GUI
- *Query*: input in the TAPAAL GUI

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [verifydtapn](../verifydtapn.md)

#### Comments:
TAPAAL models can be automatically translated into [UPPAAL](../Frameworks/UPPAAL.md) models.  So the user can choose to translate a TAPAAL model and use UPPAAL as a verification engine instead of TAPAAL.

#### URIs (github, websites, etc.):
Project page: www.tapaal.net
Download page: https://www.tapaal.net/download/

#### Last commit date:
6 April 2021 (last release date)

#### Last publication date:
16 August 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-85037-1_3 (FORMATS '21)
https://doi.org/10.1007/978-3-030-76983-3_7 (PETRI NETS '21)
https://doi.org/10.4230/LIPIcs.CONCUR.2019.23 (CONCUR '19)
https://doi.org/10.1007/978-3-319-91268-4_8 (PETRI NETS '18)
https://doi.org/10.1007/978-3-319-96145-3_28 (CAV '18)
https://doi.org/10.1007/978-3-642-28756-5_36 (TACAS '12)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Petri nets
:: PV2 :: performs queries on Petri nets