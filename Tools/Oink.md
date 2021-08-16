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
10 July 2021

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_14
https://doi.org/10.1007/978-3-319-89960-2_16

#### Related tools (tools mentioned or compared to in the paper):