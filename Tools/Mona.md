Tool that translates formulas to finite-state automata

#### Name:
MONA

#### Application domain/field:
Finite-state automata

#### Type of tool (e.g. model checker, test generator):
Translator

#### Expected input thing:
WS1S (weak monadic Second-order theory of 1 successor) or WS2S formula 

#### Expected input format:
MONA has its own syntax. The tool expects a `.mona` file.

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
MONA translates WS1S and WS2S formulas into minimum DFAs (Deterministic Finite Automata) and GTAs (Guided Tree Automata), respectively.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www.brics.dk/mona/index.html
User manual: https://www.brics.dk/mona/mona14.pdf

#### Last commit date:
8 February 2020

#### Last publication date:
2002

#### List of related papers:
[Mona: Monadic second-order logic in practice](https://doi.org/10.1007/3-540-60630-0_5) (TACAS 1995)
[MONA IMPLEMENTATION SECRETS](https://doi.org/10.1142/S012905410200128X) (Journal of Foundations of Computer Science 2002)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Automaton
:: PV2 :: translates WS1S and WS2S into minimum DFAs and GTAs
:: Source :: https://doi.org/10.1145/3550355.3552426
