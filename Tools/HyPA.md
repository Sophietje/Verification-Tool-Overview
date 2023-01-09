#### Name:
HyPA (Hyperproperty Verification with Predicate Abstraction)

#### Application domain/field:
Hyperproperties
Temporal hyperproperties
Infinite-state systems
Predicate abstraction

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Symbolic Transition System (STS)
- OHyperLTL property
- predicates to be used for the abstraction

#### Expected input format:
`.hypa` file listing the following:
- list of files for the symbolic transition systems
- file that contains the safety automaton
- quantifier structure of the hyperproperty
- file containing the predicates that should be used

- *STS*: file listing variables, locations, transitions, and where the program is observed. More details on this format can be found in the repo.
- *Property*: Specified as a safety automaton, similar to how the STS is specified. More details about the format can be found in the repo.
- *Predicates*: More details about the format can be found in the repo.

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Used to verify $\forall^k \exists^l$-safety properties within a given abstraction. This means that for any $k$ traces, there exist $l$ traces such that the resulting $k+l$ traces do not interact badly.
It can also be used for k-safety verification, i.e. no bad interaction occurs between any k traces. A k-safety property is equivalent to a $\forall^k \exists^l$-safety property where $l = 0$.

It uses the temporal logic Observation-based HyperLTL (OHyperLTL), an extension of HyperLTL.

Uses [Z3](Tools/Solvers/SMT/Z3.md) to discharge SMT queries.

#### Comments:
-

#### URIs (github, websites, etc.):
Artifact: https://doi.org/10.6084/m9.figshare.19697656
Repository: https://github.com/hypa-tool/hypa

#### Last commit date:
26 August 2022

#### Last publication date:
7 August 2022

#### List of related papers:
[Software Verification of Hyperproperties Beyond k-Safety](https://doi.org/10.1007/978-3-031-13185-1_17) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV3 :: checks $\forall^k \exists^l$-safety properties of a model
:: Hyperproperties
:: HyperLTL
:: Inﬁnite-state systems
:: Predicate abstraction
:: Source :: https://doi.org/10.1007/978-3-031-13185-1