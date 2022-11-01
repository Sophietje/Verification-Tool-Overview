Checks reachability for timed automata with diagonal constraints (and only resets as updates).

#### Name:
TChecker

#### Application domain/field:
Reachability
Timed automata
Pushdown timed automata (PDTA)
Model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
Timed automaton,
Optional flags available to e.g. choose a reachability algorithm, specify which state to compute reachability for, whether to use syntax check or to flatten the model, etc.

#### Expected input format:
Own language

#### Expected output:
Depends on the tool and flags that are used.
`tck-reach` will compute the reachable states.
`tck-syntax` will either (1) report syntax errors, or (2) computes a flattened model

#### Internals (tools used, frameworks, techniques, paradigms, ...):
TChecker consists of two tools:
- `tck-reach` for reachability analysis
- `tck-syntax` for analyses such as model transformation and syntax checks

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/ticktac-project/tchecker

#### Last commit date:
21 December 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[Certifying Emptiness of Timed Büchi Automata](https://doi.org/10.1007/978-3-030-57628-8_4) (FORMATS '20)
[Why Liveness for Timed Automata Is Hard, and What We Can Do About It](https://doi.org/10.1145/3372310) (ACM Trans. on Computational Logic, Vol. 21, Iss. 3, '20)

https://doi.org/10.1007/978-3-030-81685-8_30 (CAV '21, extends TChecker)
https://doi.org/10.1007/978-3-030-25540-4_3 (CAV '19, extends TChecker)

#### Related tools (tools mentioned or compared to in the paper):
[UPPAAL](Frameworks/UPPAAL.md)

#### Meta
:: Automaton
:: PV1 :: can compute reachable states and detect syntax errors of timed automata