Given a timed diagnostic trace (TDT) obtained during model checking a timed automaton model, it suggests possible syntactic repairs of the analyzed model

#### Name:
TarTar

#### Application domain/field:
Repair analysis
Timed diagnostic trace (TDT)
Timed automata
Model checking
Syntactic repair
Automated repair

#### Type of tool (e.g. model checker, test generator):
Automata repair tool

#### Expected input thing:
- Uppaal model
- Which kind of repair to compute
- *Optional*: Timed diagnostic trace of the Uppaal model. If this is not given, TarTar will call Uppaal to compute this.

#### Expected input format:
?

#### Expected output:
One repaired model file for every computed repair and a text file that summarizes which repairs are admissible.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
*Timed diagnostic trace (TDT)*: A timed counterexample that shows a requirement violation. This can be obtained from a model checker.

TarTar can be used for the repair of networks of timed automata (NTA).

Uses [UPPAAL](Frameworks/UPPAAL.md) for model checking and computing TDTs, [Z3](Solvers/SMT/Z3.md) for solving partial MaxSMT problems, [opaal](Checkers/opaal.md) and [LearnLib](Libraries/LearnLib.md) for checking admissibility of a repair, [[LTSMin]].

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/sen-uni-kn/tartar

#### Last commit date:
09 Mar 2023 (last activity)

#### Last publication date:
14 July 2020

#### List of related papers:
[TarTar: A Timed Automata Repair Tool](https://doi.org/10.1007/978-3-030-53288-8_25) (CAV '20)
[Clock Bound Repair for Timed Systems](https://doi.org/10.1007/978-3-030-25540-4_5) (CAV '19)

#### Related tools (tools mentioned or compared to in the paper):
Other repair tools: [[BugAssist]], [[ReAssert]], [[Angelix]], [[S3]], [[SemFix]], [[SketchFix]].

#### Meta
:: Automaton
:: PV2 :: suggests repairs based on a timed diagnostic trace
