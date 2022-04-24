Model checker for POTL temporal logic
This temporal logic can express context-free properties.

#### Name:
POMC

#### Application domain/field:
Model checking
Explicit-state model checking
Context-free properties
Temporal logic
POTL (Precedence-Oriented Temporal Logic)
Procedural programs

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
One of the following two:
1. POTL formula and an Operator Precedence Automata (OPA)
2. POTL formula and a MiniProc program

#### Expected input format:
`.pomc` file (own format, it contains the POTL formula and the automaton/MiniProc program)

#### Expected output:
`True` or `False` indicating whether the OPA/MiniProc program satisfy the formula.
If a formula is rejected, then a (partial) counterexample trace is also provided.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Given a POTL formula, it builds an automaton equivalent to this formula. Then it checks whether the intersection between this automaton and the input model is empty.

POTL (Precedence-Oriented Temporal Logic) is strictly more expressive than LTL. 

#### Comments:

#### URIs (github, websites, etc.):
Repository: https://github.com/michiari/POMC]
Artifact for CAV '21: https://zenodo.org/record/4723741

#### Last commit date:
21 April 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_18 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV3 :: checks whether a user-specified POTL formula holds for an automaton or MiniProc program
:: Automaton
