#### Name:
AdamMC

#### Application domain/field:
Software-defined networks
Petri nets (with transits)

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
One of the following three options:

1. Software-defined network (up to 82 switches) and a Flow-LTL formula
2. Petri net with transits and a Flow-LTL formula
3. Petri net and a LTL formula

#### Expected input format:
- Petri nets should be given in PNML (Petri Net Markup Language) or APT format
- It seems to have its own input format to describe the topology of a software-defined network
- (Flow-)LTL formula which should be checked can be passed as a string when calling the model checker

#### Expected output:
SAT or UNSAT
If it is UNSAT, then a counterexample is visualized with DOT/Graphviz

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Model checker for Petri nets with transits against Flow-LTL
- Transit relations are used to follow the flow induced by tokens.
- Flow-LTL is a temporal logic to specify local flow of data and global behavior or markings.
- Note that it can be used to visualize Petri nets with transits (in DOT or pdf file), or a software-defined network (converted to a Petri net with transits, also in DOT or pdf file).
- Uses [ABC](../Frameworks/ABC.md), [MCHyper](MCHyper.md), [[Aigertools]]
- Based on [Adam](../Frameworks/Adam.md)

#### Comments:

#### URIs (github, websites, etc.):
https://uol.de/en/csd/adammc (outdated)
https://github.com/adamtool/adammc

https://figshare.com/articles/code/AdamMC_A_Model_Checker_for_Petri_Nets_with_Transits_against_Flow-LTL_Artifact_/11676171

#### Last commit date:
15 May 2020

#### Last publication date:
14 July 2020

#### List of related papers:
[AdamMC: A Model Checker for Petri Nets with Transits against Flow-LTL](https://doi.org/10.1007/978-3-030-53291-8_5)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Flow-LTL
:: Petri nets :: also software-defined networks
:: PV3 :: verifies user-specified properties of Petri nets
:: Source :: https://doi.org/10.1145/3550355.3552426
