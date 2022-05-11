Tool that transpiles [PRISM](Formats/PRISM%20language.md) to [[Dice]] (probabilistic programming language).

#### Name:
Rubicon

#### Application domain/field:
Finite horizon reachability properties
Probabilistic model checking
Markov chains
Probabilistic inference

#### Type of tool (e.g. model checker, test generator):
Transpiler?

#### Expected input thing:
- Program/model
- Property

#### Expected input format:
- *Program*: [PRISM language](Formats/PRISM%20language.md)
- *Property*: Passed as an argument, [PRISM](Checkers/PRISM.md)'s specification language

#### Expected output:
Dice file.
Rubicon can also be used to invoke Dice directly. It will then also provide logging output and the resulting probability on the last line.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Rubicon is used to model check finite-horizon Markov Chains. First it translates Discrete-time Markov Chains (DTMCs) in the [PRISM](Checkers/PRISM.md) language to the [[Dice]] language. Then it runs inference with Dice.

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Artifact for CAV '21: https://zenodo.org/record/4726264
Repository: https://github.com/sjunges/rubicon

#### Last commit date:
10 June 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_27 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Model checking
:: PV1 :: translates properties from PRISM to Dice