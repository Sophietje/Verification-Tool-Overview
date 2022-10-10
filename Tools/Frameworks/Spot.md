A platform for LTL and ω-automata manipulation

#### Name:
Spot

#### Application domain/field:
Linear Temporal Logic (LTL)
Property Specification Language (PSL)
ω-automata
Model checking
Formula manipulation
Automata manipulation

#### Type of tool (e.g. model checker, test generator):
Library & set of command-line tools to manipulation automata and LTL formulas

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Spot is split into three libraries:
- `libbddx`: customized version of [[BuDDy]], for representing Binary Decision Diagrams
- `libspot`: main library, contains data structures & algorithms
- `libspot-ltsmin`: code to interface with state-spaces generated as shared libraries by LTSmin

Spot also contains the following command-line tools (see also: https://spot.lrde.epita.fr/tools.html):
- `randltl`: generates random LTL/PSL formulas
- `genltl`: generates LTL formulas from scalable patterns
- `ltlfilt`: filter, converts, and transforms LTL/PSL formulas
- `randaut`: generates random ω-automata
- `autfilt`: filters, converts, and transforms ω-automata
- `ltl2tgba`: translates LTL/PSL formula into generalized Büchi automata, or deterministic parity automata
- `ltl2tgta`: translates LTL/PSL formula into Testing automata
- `dstar2tgba`: converts ltl2dstar automata into Generalized Büchi automata
- `ltlcross`: cross-compares LTL/PSL-to-automata translators to find bugs
- `ltlgrind`: mutates LTL/PSL formulas to help reproduce bugs on smaller ones
- `ltldo`: runs LTL/PSL formulas through other translators, providing uniform input and output interfaces
- `ltlsynt`: synthesizes AIGER circuits from LTL/PSL specifications

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Project page: https://spot.lrde.epita.fr/
Try online: https://spot-sandbox.lrde.epita.fr/

#### Last commit date:
17 January 2022 (last release date)

#### Last publication date:
21 October 2019

#### List of related papers:
[Generic Emptiness Check for Fun and Profit](https://doi.org/10.1007/978-3-030-31784-3_26) (ATVA '19)
[Spot 2.0 — A Framework for LTL and 
                  
                    
                  
                  $$\omega $$
                -Automata Manipulation](https://doi.org/10.1007/978-3-319-46520-3_8) (ATVA '16)

#### Meta
:: Framework
:: PV1 :: manipulates LTL formulae and ω-automata