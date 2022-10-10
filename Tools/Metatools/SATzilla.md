An automatic algorithm portfolio for SAT based on empirical hardness models

#### Name:
SATzilla

#### Application domain/field:
SAT solving
Algorithm selection
Solver selection

#### Type of tool (e.g. model checker, test generator):
Solver selector for SAT problems

#### Expected input thing:
SAT problem

#### Expected input format:
?

#### Expected output:
SATzilla runs the algorithm with the best predicated runtime until the instance is solved or the allotted time is used up.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- SAT solvers in `SATzilla07`: [[Eureka]], [Kcnfs06](../Solvers/SAT/kcnfs.md), [March\_dl04](../Solvers/SAT/march_dl.md), [MiniSat](../Solvers/SAT/MiniSat.md) 2.0, [[Rsat]] 1.03, [[Vallst]], [Zchaff_Rand](../Solvers/SAT/zChaff.md).
- Candidate SAT solvers in `SATzilla09`: March\_dl04 ([march_dl](../Solvers/SAT/march_dl.md)?), March\_pl ([march_eq](../Solvers/SAT/march_eq.md)?), [MiniSat](../Solvers/SAT/MiniSat.md) 2.0, [[Vallst]], [Zchaff_Rand](../Solvers/SAT/zChaff.md), [Kcnfs04](../Solvers/SAT/kcnfs.md), [[TTS]] 4.0, [PicoSAT](../Solvers/SAT/PicoSAT.md) 8.46, [[MXC]] 08, [MiniSat](../Solvers/SAT/MiniSat.md) 2007, [[Rsat]] 2.0.
- Local search solvers in `SATzilla09`: gnovelty+, Ranov (both are variants of [[gNovelty]]), Ag2wsat0, Ag2wsat+ (both are variants of [[adaptG2WSAT]]), [[SATenstein]].

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://www.cs.ubc.ca/labs/beta/Projects/SATzilla

#### Last commit date:

#### Last publication date:
2009

#### List of related papers:
https://www.cs.ubc.ca/labs/beta/Projects/SATzilla/SATzilla2009.pdf (SAT Competition '09)
[SATzilla: Portfolio-based Algorithm Selection for SAT](https://doi.org/10.1613/jair.2490) (Journal of Artificial Intelligence Research '08)
[
              SATzilla-07: The Design and Analysis of an Algorithm Portfolio for SAT](https://doi.org/10.1007/978-3-540-74970-7_50) (CP '07)

#### Related tools (tools mentioned or compared to in the paper):
`\*zilla`: newest version of SATzilla.

#### Meta
:: PV2 :: decides which solver to call per instance based on predictors