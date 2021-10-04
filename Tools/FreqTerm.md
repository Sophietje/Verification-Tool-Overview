#### Name:
FreqTerm

#### Application domain/field:
Program termination
Syntax-guided synthesis (SyGuS)

#### Type of tool (e.g. model checker, test generator):
Termination prover

#### Expected input thing:
Program encoded as a system of linear constrained Horn clauses (CHCs).

#### Expected input format:
? (Looks like [[SMT-LIB]] v2)

#### Expected output:
`terminates` or `unknown`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Tool to prove program termination and non-termination using syntax-guided synthesis.
Uses [[Spacer3]], [µZ](µZ.md) [[AE-VAL]], [[Z3]]. It is developed on top of [[FreqHorn]].

#### Comments:

#### URIs (github, websites, etc.):
Repository: https://github.com/grigoryfedyukovich/aeval/tree/term

#### Last commit date:
10 February 2018

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_7

#### Related tools (tools mentioned or compared to in the paper):