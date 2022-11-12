**HQSpre**, a state-of-the-art tool for simplifying quantified Boolean formulas (QBFs) and the first available preprocessor for dependency quantified Boolean formulas (DQBFs)

#### Name:
HQSpre

#### Application domain/field:
Simplifying
Quantified Boolean formulas (QBFs)
Dependency quantified Boolean formulas (DQBFs)
Formula simplification
Clause elimination
Clause strengthening
Variable elimination

#### Type of tool (e.g. model checker, test generator):
Metatool?

#### Expected input thing:
(Dependency) quantified Boolean formula ((D)QBF)

#### Expected input format:
[QDIMACS](../Formats/QDIMACS.md) or [[DQDIMACS]] format

#### Expected output:
Simplified formula

#### Internals (tools used, frameworks, techniques, paradigms, ...):
One of the motivations behind this tool is that it can be used to simplify formulas before the solver is called. This may reduce the overall computation time and may make some instances feasible to solve which cannot be solved without preprocessing.

Some of the techniques used to simplify the formula depend on a SAT solver, for this they use the [[Antom]] SAT solver.

#### Comments:
-

#### URIs (github, websites, etc.):
Source code: https://projects.informatik.uni-freiburg.de/projects/dqbf/files

#### Last commit date:
30 August 2018

#### Last publication date:
1 September 2019

#### List of related papers:
[The (D)QBF Preprocessor HQSpre – Underlying Theory and Its Implementation1](https://doi.org/10.3233/SAT190115) (Journal on Satisfiability, Boolean Modeling and Computation '19)
[HQSpre – An Effective Preprocessor for QBF and DQBF](https://doi.org/10.1007/978-3-662-54577-5_21) (TACAS 
'17)

#### Related tools (tools mentioned or compared to in the paper):
QBF solvers: [[AIGSolve]], [[AQuA]], [CAQE](Solvers/CAQE.md), [[DepQBF]], [[Qesto]], [[RAReQS]], [[HQS]]
Other preprocessors: [[sQueezeBF]], [[Bloqqer]]

#### Meta
:: PV1 :: simplifies quantified Boolean formulas and dependency quantified Boolean formulas
:: QBF
:: Source :: https://doi.org/10.1145/3550355.3552426