Program analysis toolkit for (non-)termination analysis and safety checker

#### Name:
VeryMax

#### Application domain/field:
Termination
Safety verification

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
Program or integer transition system

#### Expected input format:
*Program*: Small fragment of C or C++ with assertion(s)
*Integer transition system*: [T2](T2.md) or Pushdown [SMT-LIB](../Formats/SMT-LIB.md)2 specification format

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
VeryMax uses conditional termination arguments to segment the state space for the remainder of the analysis.
VeryMax can be used as a safety analyzer and a (non-)termination prover.

Uses [Barcelogic](Solvers/SMT/Barcelogic.md).

#### Comments:
There are two versions available of VeryMax via the project page. The most recent version is the version that provides (non-)termination analysis. The older version provides a safety checker.

#### URIs (github, websites, etc.):
Project page: https://www.cs.upc.edu/~albert/VeryMax.html

#### Last commit date:
-

#### Last publication date:
31 March 2017

#### List of related papers:
[Proving Termination Through Conditional Termination](https://doi.org/10.1007/978-3-662-54577-5_6) (TACAS '17)
[Speeding up the Constraint-Based Method in Difference Logic](https://doi.org/10.1007/978-3-319-40970-2_18) (SAT '16)
[Compositional safety verification with Max-SMT](https://doi.org/10.1109/FMCAD.2015.7542250) (FMCAD '15)

#### Related tools (tools mentioned or compared to in the paper):
Other tools that participated in the termination category of SV-COMP 2016: [AProVE](AProVE.md), [[Ctrl]], [HipTNT+](HipTNT+.md), [SeaHorn](Checkers/SeaHorn.md), [[Ultimate]]

#### Meta
:: Termination
:: PV3 :: checks (non-)termination of integer transition systems or C programs, or checks assertions in a C program