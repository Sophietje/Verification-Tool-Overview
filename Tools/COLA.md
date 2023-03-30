#### Name:
COLA

#### Application domain/field:
Büchi automata
Determinization
Complementation
Nondeterministic Büchi automata (NBAs)

#### Type of tool (e.g. model checker, test generator):
Library for determinization of Büchi automata

#### Expected input thing:
Büchi automaton

#### Expected input format:
[HOA](../../Formats/HOA.md)

#### Expected output:
By default, it converts a given Büchi automaton into a deterministic automaton

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Built on top of [Spot](../../Tools/Frameworks/Spot.md

COLA supports the following operations on Büchi automata:
- Determinization (output can be a deterministic automaton, deterministic Parity automaton or deterministic Rabin automaton)
- Complementation (outputs complement Büchi automaton of the given automaton after determinization)

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/liyong31/COLA
- CAV '22 Artifact: https://doi.org/10.5281/zenodo.6558928

#### Last commit date:
21 June 2022
15 Jul 2022 (last activity)

#### Last publication date:
6 August 2022

#### List of related papers:
[Divide-and-Conquer Determinization of Büchi Automata Based on SCC Decomposition](https://doi.org/10.1007/978-3-031-13188-2) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Compared to (in CAV '22 paper): [Spot](../../Tools/Frameworks/Spot.md), [Owl](../../Tools/Libraries/Owl.md)

#### Meta
:: Automaton
:: PV1 :: computes complementation, determinization and containment for Büchi automaton
