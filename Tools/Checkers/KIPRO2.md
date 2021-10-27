KIPRO2: k-Induction for probabilistic programs
(note: 2 is part of the name, not a version number)

#### Name:
KIPRO2 (sometimes stylized as kipro2)

#### Application domain/field:
Model checking
Bounded model checking (BMC)
k-induction
Probabilistic programs

#### Type of tool (e.g. model checker, test generator):
Probabilistic model checker

#### Expected input thing:
- pGCL program
- Pre-/post-expectations
- Checker to use: kind/bmc/both (i.e. k-induction, bounded model checking, or both)

#### Expected input format:
- *pGCL program*: `.pgcl` file
- *Pre-/post-expectations*: parameters when executing the tool, or as comment in the model ("// ARGS: --post [arg] --pre [arg] ")
- *Checker*: parameter when executing the tool, or as a comment in the model ("// ARGS: --checker [arg]")

#### Expected output:
Whether the property could be proven, if not then a counterexample is provided.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It performs in parallel latticed k-induction and BMC (bounded model checking) to fully automatically verify upper bounds on expected values of `{pGCL}` programs. It can also reason about expected values, e.g. expected runtimes, of such programs.

Uses [Z3](Z3.md), [[PySMT]]

#### Comments:
License: Apache-2.0 license

#### URIs (github, websites, etc.):
Repository: https://github.com/moves-rwth/kipro2

#### Last commit date:
29 July 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_25 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
