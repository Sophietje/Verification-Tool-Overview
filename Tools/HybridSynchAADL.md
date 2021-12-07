Modeling language & formal analysis tool for virtually synchronous cyber-physical systems with complex control programs, continuous behaviors, bounded clock skews, network delays, and execution times.

HybridSynchAADL (the language) is a subset of the avionics modeling standard AADL and its behavioral annex to model control programs, and captures a synchronous subset of AADL with continuous behaviors.

The formal analysis is done using a combination of [Maude](Maude.md) and [Yices](Solvers/SMT/Yices.md). It can do symbolic reachability analysis and randomized simulation. Symbolic reachability analysis can verify that all possible behaviors satisfy a given requirement, if not then a counterexample is generated. Randomized simulation repeatedly executes the model until a counterexample is found.
The user can specify time-bounded invariant and reachability properties that should be checked.

Extends [[SynchAADL]]

Project page: https://hybridsynchaadl.github.io/
Repository: https://github.com/hybridsynchaadl/HybridSynchAADL

Note: HybridSynchAADL is an OSATE2 plugin