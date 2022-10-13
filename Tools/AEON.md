Tool to analyse bifurcations (significant change in structure and quality of attractors) in asynchronous parametrised Boolean networks

#### Name:
AEON

#### Application domain/field:
Boolean networks (BNs)
Parametrised Boolean networks
Computational systems biology

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
Parametrised Boolean network including a graphical description of the regulations.

#### Expected input format:
Parametrised Boolean network can either be edited using their interface/editor. However they also provide an import/export function for Boolean networks in their own text-based format (.aeon) or XML-based SBML level 3 qual standard (.sbml)

#### Expected output:
- Partitioning represented as a list of behaviour classes with the cardinality of the respective parameter space partitions.
	![[Screenshot 2021-05-27 at 15.25.43.png]] *Source: "AEON - Attractor Bifurcation Analysis of Parametrised Boolean Networks." by N. Benes et al. (CAV 2020)*
- Witness BN (if user selects a behaviour class form the list above)
- Bifurcation function encoded as BDDs

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- BDDs (Binary Decision Diagrams)
- TSCC (temporal strongly connected components) detection algorithm

#### Comments:

#### URIs (github, websites, etc.):
Online client: https://biodivine.fi.muni.cz/aeon/
Client: https://github.com/sybila/biodivine-aeon-client
Compute engine/server: https://github.com/sybila/biodivine-aeon-server

#### Last commit date:
14 Sep 2022

#### Last publication date:
24 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_28

#### Related tools (tools mentioned or compared to in the paper):
Tools for non-parametrised BNs: ATLANTIS, Bio Model Analyzer (BMA), BoolNet, PyBoolNet, Inet, The Cell Collective, CellNetAnalyzer, ASSA-PBN.
Tools for parameter synthesis for parametrised BNs: GRNMC, GINsim, TREMPPI.
Tool to control cell behaviour through BNs: ViSiBooL.

#### Meta
:: BDD
:: PV1           :: analyses bifurcations of a parametrised Boolean network