#### Name:
LEVEL-UP

#### Application domain/field:
Markov decision processes (MDPs)
Probabilistic behavior
Probabilistic programs
Subroutines
Probabilistic model checking
Model checking

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
Two Markov decision processes:
1. MDP that encodes the (uncertain) macro-MDP
2. MDP that describes the parametric template for the subMDPs

#### Expected input format:
Probabilistic program description in [PRISM language](../../Formats/PRISM%20language.md)

#### Expected output:
Computed bounds (for what?)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The idea is to analyse an MDP by splitting it into two (hierarchical) levels. The first is a toplevel macro-MDP where they consider the subprocesses as some kind of uncertainty. They then use an analysis techniques for uncertain MDPs to approximate things. In this loop it removes uncertainty by analysing more and more of the previously unanalysed subprocesses.

It is a technique that can be used for probabilistic model checking of MDPs.

LEVEL-UP is a prototype built on top of [Storm](../../Tools/Checkers/Storm.md).

#### Comments:

#### URIs (github, websites, etc.):
- The source code and executables, the benchmarks, logﬁles and utilities are all available in an archived Docker container: https://doi.org/10.5281/zenodo.6524787.
- Repository: https://github.com/sjunges/level-up

#### Last commit date:
15 Aug 2022 (default branch)
15 Aug 2022 (last activity)

#### Last publication date:
2022

#### List of related papers:
[Abstraction-Refinement for Hierarchical Probabilistic Models](https://doi.org/10.1007/978-3-031-13185-1_6) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: MDP
:: Probabilistic programs
:: Source :: https://doi.org/10.1007/978-3-031-13185-1
