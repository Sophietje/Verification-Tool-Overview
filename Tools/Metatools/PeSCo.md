PeSCo is a tool for predicting a (likely best) sequential combination of verifiers on a given verification task and then running it

#### Name:
PeSCo: Predicting Sequential Combinations of Verifiers

#### Application domain/field:
Machine learning
Configurations
Rank prediction
Performance prediction

#### Type of tool (e.g. model checker, test generator):
Meta-tool, predicts which combination of verifier configurations to use

#### Expected input thing:
- Program
- Specification(s) to check

#### Expected input format:
- *Program*: `.c` file
- *Specification(s)*: `.spc` file
	- If given `default.spc`, it will look for labels named ERROR (case insensitive) and assertions in the source code.

#### Expected output:
In the console, or in an interactive HTML report, it reports whether the specification holds (result is `TRUE`) or not (result is `FALSE`).
If the specification does not hold, a counterexample is also generated.
It also generates visualizations of the program (e.g. abstract reachability tree), coverage information, and time statistics.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
PeSCO uses machine learning to learn a ranking of verifiers on verification tasks. This ordering of verifiers is based on the SV-COMP scoring schema.
It uses [CPAchecker](../Checkers/CPAchecker.md) (with different configurations) as base verifiers.
It uses [MathSAT](../Solvers/SMT/MathSAT.md) 5.

PeSCo is integrated in [CPAchecker](../Checkers/CPAchecker.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository (fork of CPAChecker into which PeSCo is integrated): https://github.com/cedricrupb/cpachecker

#### Last commit date:
18 August 2021

#### Last publication date:
4 April 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-17502-3_19 (TACAS '19)
https://doi.org/10.1145/3121257.3121262 (earlier rank prediction approach that was extended in the TACAS '19 paper, SWAN '17)

#### Related tools (tools mentioned or compared to in the paper):
-
