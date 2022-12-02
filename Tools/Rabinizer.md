A tool set for translating formulae of LTL to different types of deterministic ω-automata.

#### Name:
Rabinizer

#### Application domain/field:
Linear temporal logic (LTL)
Deterministic 𝜔-automata
Rabin automata
Büchi automata
Automata translation

#### Type of tool (e.g. model checker, test generator):
Automata translator

#### Expected input thing:
LTL formula

#### Expected input format:
Same format as [Owl](Libraries/Owl.md), described in detail here: https://gitlab.lrz.de/i7/owl/blob/master/doc/FORMATS.md

#### Expected output:
Automata that corresponds to the LTL formula.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
As of Rabinizer 4, it can translate an LTL formula into one of the following type of automata:
- DGRA: deterministic generalized Rabin automata
- DRA: deterministic Rabin automata
- DPA: deterministic parity automata
- LDGBA: limit-deterministic generalized Büchi automata
- LDBA: limit-deterministic Büchi automata
- Or it can translate the frequency extension of LTL to a deterministic generalized mean-payoff Rabin automata (DGRMA)

It is also linked to [PRISM](Checkers/PRISM.md) to allow for probabilistic verification of some automata.

#### Comments:
Bundled with [Owl](Libraries/Owl.md), a tool collection and library for Omega-words, 𝜔-automata and Linear Temporal Logic (LTL). https://owl.model.in.tum.de/

#### URIs (github, websites, etc.):
Project page Rabinizer 4: https://rabinizer.model.in.tum.de/
Project page Rabinizer 3: https://www7.in.tum.de/~kretinsk/rabinizer3.html
Project page Rabinizer 2: https://www7.in.tum.de/~kretinsk/rabinizer2.html

#### Last commit date:
-

#### Last publication date:
18 July 2018

#### List of related papers:
[Rabinizer 4: From LTL to Your Favourite Deterministic Automaton](https://doi.org/10.1007/978-3-319-96145-3_30) (CAV 2018)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Automaton
:: LTL
:: PV1 :: can translate LTL formulae into different types of automata
:: Source :: https://doi.org/10.1145/3550355.3552426
