Exact minimal unsatisfiable subset (MUS) counter that does not rely on exhaustive enumeration.

#### Name:
CountMUST

#### Application domain/field:
Minimal Unsatisfiable Subsets (MUSes)
MUS counting

#### Type of tool (e.g. model checker, test generator):
MUS counter

#### Expected input thing:
Unsatisfiable set F of Boolean clauses (i.e. a Boolean formula in CNF)

#### Expected input format:
If it is a "Plain" MUS then [DIMACS](../Formats/DIMACS.md) `.cnf` format
If it is a "group" MUS then a `.gcnf` file for a "group DIMACS format". 
More detail about the input format is available in the README of the repository.

#### Expected output:
Number of Minimal Unsatisfiable Subsets (MUSes) of F.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [[GANAK]], [[RIME]] and [UWrMaxSat](Solvers/UWrMaxSat.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/jar-ben/exactMUSCounter

#### Last commit date:
11 Jun 2021 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[Counting Minimal Unsatisfiable Subsets](https://doi.org/10.1007/978-3-030-81688-9_15) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [AMUSIC](AMUSIC.md)

#### Meta
:: Minimal Unsatisfiable Subsets (MUSes)
:: PV1 :: counts minimal unsatisfiable subsets of a given boolean formula
:: Source :: https://doi.org/10.1007/978-3-030-81688-9 :: https://doi.org/10.1145/3550355.3552426
