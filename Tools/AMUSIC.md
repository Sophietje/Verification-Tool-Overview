#### Name:
AMUSIC: Approximate Minimal Unsatisfiable Subsets Implicit Counter

#### Application domain/field:
Minimal unsatisfiable sets (MUSes)

#### Type of tool (e.g. model checker, test generator):
Counting tool?

#### Expected input thing:
- Boolean formula in CNF
- Tolerance parameter ε > 0
- Confidence parameter δ ∈(0,1]

#### Expected input format:
A .gcnf or .cnf file for the boolean formula.
The tolerance and confidence parameter can be set with arguments given to the script.

#### Expected output:
Estimate of the amount of MUSes guaranteed to be within (1+ε)-multiplicative factor of the exact count with confidence at least 1-δ

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [CAQE](Solvers/CAQE.md), [CADET](Solvers/CADET.md), [[QRATPre+]], [[muser2]], [UWrMaxSat](Solvers/UWrMaxSat.md), [[pysat]]

#### Comments: 
Tool for approximate counting of minimal unsatisfiable subsets of a given Boolean formula in CNF

#### URIs (github, websites, etc.):
https://github.com/jar-ben/amusic

#### Last commit date:
2 March 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_21

#### Related tools (tools mentioned or compared to in the paper):
MUS enumeration techniques: MARCO, MCSMUS, UNIMUS
