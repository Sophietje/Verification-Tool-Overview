Tool to analyse CRNs (Chemical Reaction Networks)

#### Name:
SeQuaiA

#### Application domain/field:
Chemical reaction networks (CRNs)
Biochemical systems
Continuous-time stochastic systems
Semi-qualitative analysis

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Chemical reaction network (CRN): consists of a set of chemical reactions of given species, each running at a certain rate.
- *Optional*: if doing a semi-quantitative analysis of the system, the user needs to provide the following
	- For each species, a list of increasing population thresholds and a population bound

#### Expected input format:
Input via the GUI

#### Expected output:
Depends on what the tool is used for (see "Internals").

#### Internals (tools used, frameworks, techniques, paradigms, ...):
SeQuaiA supports several different analyses:
- It can be used to edit a CRN
- It can be used to analyze the system using a semi-quantitative analysis on an abstraction of the Markov chain of the CRN
- It can be used to generate concrete runs using simulation. These display average-case behaviour, also called mean simulations.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://sequaia.model.in.tum.de/

#### Last commit date:
-

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_32 (CAV '20)
https://doi.org/10.1007/978-3-030-25540-4_28 (CAV '19)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: handles and analyses chemical reaction networks
:: Simulation
