Solver for quantified boolean formulas (QBF)

#### Name:
CAQE: Clausal Abstraction for Quantifier Elimination

#### Application domain/field:
Quantified boolean formulas (QBFs)
Boolean theories
QBF solver

#### Type of tool (e.g. model checker, test generator):
QBF (quantified boolean formulas) solver

#### Expected input thing:
quantified Boolean formula (QBF) in prenex conjunctive normal (prenex CNF) form

#### Expected input format:
[QDIMACS](../../Formats/QDIMACS.md) file format

#### Expected output:
Result code `10` for satisfiable and `20` for unsatisfiable instances. 
It can also output in the [QDIMACS](../../Formats/QDIMACS.md) format which has partial assignments to variables.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [PicoSAT](SAT/PicoSAT.md), [MiniSat](SAT/MiniSat.md), [CryptoMiniSat](SAT/CryptoMiniSat.md) and [Lingeling](SAT/Lingeling.md) as underlying SAT solver.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www.react.uni-saarland.de/tools/caqe/
Repository: https://github.com/ltentrup/caqe

#### Last commit date:
24 February 2021

#### Last publication date:
13 July 2017

#### List of related papers:
[On Expansion and Resolution in CEGAR Based QBF Solving](https://doi.org/10.1007/978-3-319-63390-9_25) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: QBF
:: PV4 :: produces a satisfiability result for a quantified boolean formula