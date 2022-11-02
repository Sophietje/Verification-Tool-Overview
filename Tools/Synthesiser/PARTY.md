Bounded synthesis tool that supports CTL* synthesis

#### Name:
PARTY

#### Application domain/field:
SMT-based synthesis
Bounded synthesis
Synthesis
Reactive synthesis
CTL* synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
Specification file

#### Expected input format:
- `elli.py`: Acacia+ or TLSF format
- `star.py`: Python

#### Expected output:
- `elli.py`: If realisable, PARTY outputs a Mealy or Moore machine in dot or NuSMV format.
- `star.py`: returns `unknown` or `realizable`
If realisable, then an automaton in dot or [AIGER](../../Formats/AIGER.md) format.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- This tool uses **bounded synthesis**. In bounded synthesis an LTL property is translated to Büchi automata, and the verification of LTL properties can be reduced to deciding emptiness of the product of this automaton and a Kripke structure representing an implementation.
- This tool is actually a collection of several tools for bounded synthesis, the most notable being:
    - The `elli.py` implements Bounded Synthesis, as explained in the CAV '13 paper.
    - The `star.py` extends bounded synthesis to branching logics (CTL*), as explained in the CAV '17 paper.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/5nizza/party-elli

#### Last commit date:
12 April 2020

#### Last publication date:
13 July 2017

#### List of related papers:
[Bounded Synthesis for Streett, Rabin, and $\text {CTL}^{*}$](https://doi.org/10.1007/978-3-319-63390-9_18) (CAV '17)
[PARTY Parameterized Synthesis of Token Rings](https://doi.org/10.1007/978-3-642-39799-8_66) (CAV '13)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Automaton
:: Synthesis
:: LTL
:: PV2 :: generates an automaton from source code or spec