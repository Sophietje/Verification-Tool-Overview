#### Name:
FORKLIFT

#### Application domain/field:
Inclusion
Automata
Büchi automata

#### Type of tool (e.g. model checker, test generator):
Inclusion checker for Büchi automata

#### Expected input thing:
Two Büchi automata A & B

#### Expected input format:
Two `.ba` files ([ba](../Formats/ba.md))

#### Expected output:
0 if the language of automata A is a subset of the language of automata B.
1 if the language of automata A is not a subset of the language of automata B.
127 if the inclusion was not computed.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
FORKLIFT is an inclusion checker for Büchi automata.

#### Comments:
-

#### URIs (github, websites, etc.):
- Artifact: https://doi.org/10.5281/zenodo.6552870
- Repository: https://github.com/Mazzocchi/FORKLIFT

#### Last commit date:
7 June 2022
07 Jun 2022 (last activity)

#### Last publication date:
6 August 2022

#### List of related papers:
[FORQ-Based Language Inclusion Formal Testing](https://doi.org/10.1007/978-3-031-13188-2_6) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Other tools that can solve inclusion problems: [Spot](../../Tools/Frameworks/Spot.md), [[GOAL]], [RABIT](../../Tools/RABIT.md), [ROLL](../../Tools/Libraries/ROLL.md), [[BAIT]]

#### Meta
:: Automaton
:: PV1 :: checks language-inclusion for Büchi automata
:: Source :: https://doi.org/10.1007/978-3-031-13188-2
