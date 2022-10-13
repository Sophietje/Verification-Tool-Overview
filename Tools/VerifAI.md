Toolkit for formal design and analysis for systems that include artificial intelligence and machine learning components.

#### Name:
VerifAI

#### Application domain/field:
Artificial intelligence
Machine learning
Simulation
Synthesis

#### Type of tool (e.g. model checker, test generator):
Framework?

#### Expected input thing:
- Simulatable model of the system, including code for one or more controllers and perception components, and a dynamical model of the system being controlled
- Probabilistic model of the environment, specifying constraints on the workspace, locations of agents and objects, and the dynamical behavior of agents
- Property over the composition of the system and its environment

#### Expected input format:
- *System model*: Any executable code, invoked by the simulator
- *Environment model*: Typically a definition in the simulator of the different types of agents, plus a description of their initial conditions and other parameters using the **Scenic** probabilistic programming language.
- *Property*: Metric Temporal Logic (MTL), objective functions or arbitrary code monitoring the property

#### Expected output:
Depends on what analysis is used.
- *Falsification* will return one or more counterexamples for simulation traces that violate the property
- *Fuzz testing*: Traces samples from the distribution of behaviors induced by the environment model
- *Data augmentation*: Generates additional data for training and testing an ML component
- *Error table analysis*: Identifies features that are correlated with property failures
- *Hyper-parameter or model parameter synthesis*: Generates a parameter evaluation that satisfies the specified property.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
VerifAI offers the following analyses:
1. temporal-logic falsification, 
2. model-based fuzz testing, 
3. counterexample-guided data augmentation, 
4. counterexample (error table) analysis, 
5. hyper-parameter synthesis, and 
6. model parameter synthesis

Uses [py-metric-temporal-logic](Libraries/py-metric-temporal-logic.md).

#### Comments:
License: BSD-3-Clause

#### URIs (github, websites, etc.):
Repository: https://github.com/BerkeleyLearnVerify/VerifAI
Documentation: https://verifai.readthedocs.io/en/latest/

#### Last commit date:
30 Sep 2022

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25540-4_25 (CAV '19)
https://doi.org/10.1007/978-3-030-53288-8_6 (CAV '20, case study)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Synthesis
:: Framework
:: PV3 :: checks built-in and user-defined properties of system models