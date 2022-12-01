SMT solver for monotonic theories over Booleans and bitvectors

#### Name:
MonoSAT

#### Application domain/field:
SMT solving
SAT Modulo Theory
Satisfiability modulo theories (SMT)
Monotonic theories

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SAT problem

#### Expected input format:
One of several options:
- It can be used via the Python 3 library
- It can be used via the Java library
- It can be used via the commandline, then it requires a `.gnf` file (this is an extension of the [DIMACS](../../../Formats/DIMACS.md) format with e.g. bitvector support)

#### Expected output:
`SAT` or `UNSAT`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The idea is to build an SMT solver for monotonic theories, for which they can create efficient SMT solvers. They claim that many common problems can be solved with this, including reachability, shortest paths, minimum spanning trees, etc.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www.cs.ubc.ca/labs/isd/Projects/monosat/
Repository: https://github.com/sambayless/monosat
Tutorial showing how to use MonoSAT in Python: https://github.com/sambayless/monosat/blob/master/TUTORIAL.md

#### Last commit date:
11 November 2021

#### Last publication date:
2015

#### List of related papers:
https://ojs.aaai.org/index.php/AAAI/article/view/9755 (AAAI Conference on Artificial Intelligence '15)
https://www.cs.ubc.ca/labs/isd/Projects/monosat/sam_bayless_thesis_2017.pdf (thesis '17)

#### Related tools (tools mentioned or compared to in the paper):
[MiniSat](../SAT/MiniSat.md), [[CLASP]]

#### Meta
:: SMT
:: PV4 :: produces a satisfiability result for a formula
