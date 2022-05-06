Game solver for two-player reachability games

#### Name:
CabPy

#### Application domain/field:
Two-player reachability games
Reachability games
Game solver

#### Type of tool (e.g. model checker, test generator):
Game solver

#### Expected input thing:
Two-player linear reachability game

#### Expected input format:
`.rg` file with the following structure:
```
bool: 'a list of the Boolean variables of the game'
(int or real): 'a list of the variables of the game'
init: 'a formula describing the initial states of the game'
safe: 'a formula describing the moves of the safety player'
reach: 'a formula describing the moves of the reachability player'
goal: 'a formula describing the goal states of the game'
```
The connectives -> (Implies), <-> (Iff), | (or), & (and), ! (not), < (less than), <= (less or equal), = (equal), >= (greater or equal), > (greater), + (plus) and - (minus) are allowed.

#### Expected output:
Which player ('REACH' or 'SAFE') wins the game.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [PySMT](Libraries/PySMT.md), [MathSAT](Solvers/SMT/MathSAT.md) 5 and [Z3](Solvers/SMT/Z3.md).

#### Comments:
License: MIT License

#### URIs (github, websites, etc.):
Repository: https://github.com/reactive-systems/cabpy

#### Last commit date:
28 May 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_42 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: solves a two-player reachability game