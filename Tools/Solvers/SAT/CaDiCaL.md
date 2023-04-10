SAT solver uses Conflict Driven Clause Learning (CDCL) and inprocessing, built with the main aim being clean, understandable and modifiable.

#### Name:
CaDiCaL

#### Application domain/field:
SAT solving

#### Type of tool (e.g. model checker, test generator):
SAT solver

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Local search, target phases (generalisation of phase saving), rephasing, lucky phase detection, bounded variable elimination, failed literal probing, clause subsumption/vivification, chronological backtracking, incremental solving, model based testing.

License: MIT

#### URIs (github, websites, etc.):
Project page: http://fmv.jku.at/cadical/
Repository: https://github.com/arminbiere/cadical

#### Last commit date:
17 Aug 2022
11 Mar 2023 (last activity)

#### Last publication date:
2019

#### List of related papers:
[CaDiCaL at the SAT Race 2019](http://fmv.jku.at/papers/Biere-SAT-Race-2019-solvers.pdf)
[Backing Backtracking](https://doi.org/10.1007/978-3-030-24258-9_18)

#### Related tools (tools mentioned or compared to in the paper):
[[ParaFROST]] (extension), [[Mobical]] (integrated model based tester), [[YalSAT]] (earlier experiment with local search), [[Lingeling]] (earlier experiment with lucky phases)

#### Meta
:: SAT
:: PV4 :: produces a satisfiability result for a formula
:: Source :: extended by [[ParaFROST]]
