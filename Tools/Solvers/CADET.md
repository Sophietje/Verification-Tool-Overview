#### Name:
CADET: Cal Incremental Determinizer

#### Application domain/field:
QBF solving
2QBF solving

#### Type of tool (e.g. model checker, test generator):
2QBF solver

#### Expected input thing:
2QBF formula

#### Expected input format:
[QDIMACS](../../Formats/QDIMACS.md) or [QAIGER](../../Formats/QAIGER.md) format

#### Expected output:
- `SAT` if the formula is satisfiable. You can also ask for the solution (assignments for all quantifiers) that CADET has computed (will be given as an AIGER circuit). 
- `UNSAT` if the formula is unsatisfiable. The tool will then give an assignment for all universally quantified variables. Results are written in QDIMACS format to stdout.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [PicoSAT](SAT/PicoSAT.md)

#### Comments:
CADET is a 2QBF (Quantified Boolean formulas with forall-exists quantifier alternation) solver

#### URIs (github, websites, etc.):
Repository: https://github.com/MarkusRabe/cadet

#### Last commit date:
27 January 2021

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25543-5_6
https://doi.org/10.1007/978-3-319-40970-2_23

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: QBF
:: PV4 :: produces a satisfiability result for a 2QBF