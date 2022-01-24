Modeling language and formal analysis tool for virtually synchronous cyber-physical systems with complex control programs, continuous behaviors, bounded clock skews, network delays, and execution times.

#### Name:
HybridSynchAADL

#### Application domain/field:
Cyber-physical systems (CPSs)
Synchronous systems
Continuous systems
Reachability analysis
Symbolic reachability analysis
Simulation

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
- Model of a synchronous cyber-physical system
- Specification/requirement to check

#### Expected input format:
HybridSynchAADL model

#### Expected output:
Depends on the analysis that is chosen.
It can check whether the model is well-formed.
The formal analyses might give a counterexample if the specification is not satisfied.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
HybridSynchAADL (the language) is a subset of the avionics modeling standard AADL and its behavioral annex to model control programs, and captures a synchronous subset of AADL with continuous behaviors.

The formal analysis is done using a combination of [Maude](../Formats/Maude.md) and [Yices](Solvers/SMT/Yices.md). It can do symbolic reachability analysis and randomized simulation. Symbolic reachability analysis can verify that all possible behaviors satisfy a given requirement, if not then a counterexample is generated. Randomized simulation repeatedly executes the model until a counterexample is found.
The user can specify time-bounded invariant and reachability properties that should be checked.

The tool can be used to do the following things:
- Constraints checking: validate that the model satisfies all the syntactic constraints of the modelling language
- Code generation: Synthesize Maude code from the model
- Formal analysis: 
	1. *Symbolic reachability* to verify that all possible behaviors satisfy a given requirement, if not then a counterexample is generated. This can guarantee the absence of a counterexample.
	2. *Randomized simulation*, which repeatedly executes the model until a counterexample of a requirement is found.
	3. *Portfolio analysis* which runs both previous methods in parallel and gives the results of the analysis that terminates first.

Extends [[SynchAADL]]

#### Comments:
Note: HybridSynchAADL is an OSATE2 plugin

#### URIs (github, websites, etc.):
Project page: https://hybridsynchaadl.github.io/
Repository: https://github.com/hybridsynchaadl/HybridSynchAADL

#### Last commit date:
5 May 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_23 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
