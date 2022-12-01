#### Name:
Oink

#### Application domain/field:
Parity games
Model checking

#### Type of tool (e.g. model checker, test generator):
Parity game solver

#### Expected input thing:
Parity game

#### Expected input format:
PGSolver format
The file may be zipped using gzip (.gz) or bzip2 (.bz2).

#### Expected output:
Solution to the parity game (i.e. who is the winner of the game starting from the initial vertex)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This tool implements several algorithms for solving parity games.
The tool also provides a few options to transform parity games (e.g. removing self-loops) and it can generate a .dot graph of a parity game.

Uses the [[Lace]] work-stealing framework.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://www.github.com/trolando/oink

#### Last commit date:
04 Sep 2022 (default branch)
04 Sep 2022 (last activity)

#### Last publication date:
18 July 2018

#### List of related papers:
[Attracting Tangles to Solve Parity Games](https://doi.org/10.1007/978-3-319-96142-2_14)
[Oink: An Implementation and Evaluation of Modern Parity Game Solvers](https://doi.org/10.1007/978-3-319-89960-2_16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: solves a parity game
:: Source :: https://doi.org/10.1145/3550355.3552426
