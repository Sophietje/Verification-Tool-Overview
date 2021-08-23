Tool for the analysis and parameterized verification of population protocols

#### Name:
Peregrine

#### Application domain/field:
Population protocols
Distributed computing
Parameterized verification

#### Type of tool (e.g. model checker, test generator):
Analysis tool

#### Expected input thing:
Population protocol

#### Expected input format:
Graphical editor or Python script

#### Expected output:
Depends on the option chosen to analyse a protocol.
For verification it will show whether correctness could be proven or not. If not, then it can give a counterexample.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Peregrine has several options for analysing a protocol, including:
- Manual step-by-step simulation
- Automatic sampling
- Statistics generation of average convergence speed
- Detection of incorrect executions through simulation
- Formal verification (only for silent protocols): This proves correctness for all of the infinitely many initial configurations. It verifies that a population protocol computes a given predicate. This predicate needs to be specified by the user in quantifier-free Presburger arithmetic

Uses [[Z3]] to check satisfiability of Presburger arithmetic formulas.

#### Comments:
On scalability of Peregrine (from the CAV 2018 paper): "Currently, Peregrine can verify protocols with up to a hundred states and a few thousands transitions. The bottleneck is the size of the constraint system."

#### URIs (github, websites, etc.):
Project page: https://peregrine.model.in.tum.de/
Repository: https://gitlab.lrz.de/ga97cer/peregrine

#### Last commit date:
21 December 2020

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_34

#### Related tools (tools mentioned or compared to in the paper):