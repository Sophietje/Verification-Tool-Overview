#### Name:
QuaSi

#### Application domain/field:
Syntax-guided synthesis (SyGuS)
Program synthesis
Quantitative objectives

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
QSyGuS problem (SyGuS problem with quantitative objectives)

#### Expected input format:
Extension of the SyGuS format

#### Expected output:
It times out or presents the solution to the QSyGuS problem. 
A solution to the QSyGuS problem is a term, in the language of the provided grammar, such that the Boolean formula constraining the semantic behavior is satisfied, and such that the constraints over the weight $w$ of the synthesized program is true.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Quasi is a tool for specifying and solving QSyGuS problems.

QSyGuS: "syntax-guided synthesis problems with quantitative objectives over the syntax of the synthesized program, e.g. find the most likely program with respect to a given probability distribution"

Uses [CVC4](../Solvers/SMT/CVC4.md), [[ESolver]], [[EUSolver]]

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: *Cannot find one in the paper or on the first author's website.*

#### Last commit date:
-

#### Last publication date:
18 July 2018

#### List of related papers:
[Syntax-Guided Synthesis with Quantitative Syntactic Objectives](https://doi.org/10.1007/978-3-319-96145-3_21)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Synthesis
:: PV2 :: tries to solve a SyGuS problem with quantitative objectives
:: Source :: https://doi.org/10.1145/3550355.3552426
