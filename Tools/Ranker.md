
#### Name:
Ranker

#### Application domain/field:
Büchi automata
Automata theory
Complementation

#### Type of tool (e.g. model checker, test generator):
-

#### Expected input thing:
Büchi automata

#### Expected input format:
[HOA](../../Formats/HOA.md) or [[../../Formats/ba]] format

#### Expected output:
Complement of the Büchi automaton

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Ranker supports several types of $\omega$-automata:
- Büchi automata with mixed transition-based/state-based acceptance condition
- Generalized co-Büchi automata

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/vhavlena/ranker

#### Last commit date:
30 December 2022

#### Last publication date:
6 August 2022

#### List of related papers:
[Complementing Büchi Automata with Ranker](https://doi.org/10.1007/978-3-031-13188-2_10) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '22 paper: [ROLL](Libraries/ROLL.md), [[GOAL]], [Spot](Frameworks/Spot.md), [Seminator](Seminator.md) 2, [[LTL2DSTAR]]

#### Meta
:: Automaton
:: PV1 :: constructs the complement of a Büchi automaton
:: Source :: https://doi.org/10.1007/978-3-031-13188-2