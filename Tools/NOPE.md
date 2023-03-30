Tool to determine whether a syntax-guided synthesis problem is unrealizable (i.e. has no solution).

#### Name:
NOPE

#### Application domain/field:
Program synthesis
Syntax-guided synthesis (SyGuS)

#### Type of tool (e.g. model checker, test generator):
Property checker?

#### Expected input thing:
SyGuS problem

#### Expected input format:
?

#### Expected output:
`realizable` or `unrealizable`.
It is also possible that a time out occurs.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
**Unrealizability problem**: Given syntax-guided synthesis (SyGuS), establish whether the problem is *unrealizable* (i.e. has no solution)

Given an unrealizability problem of the form $sy = (\psi, G)$, it returns **unrealizable** if no expression-tree in $L(G)$ satisfies $\psi$. If it returns **realizable**, some $e \in L(G)$ satisfies $\psi$. 

Uses [SeaHorn](Checkers/SeaHorn.md), [[ESolver]], [Z3](Solvers/SMT/Z3.md).

#### Comments:
There exist SyGuS problems for which the algorithm cannot prove unrealizability (i.e. the algorithm is incomplete) but the authors argue that it works for many SyGuS instances.

#### URIs (github, websites, etc.):
Repository (not linked in paper, found via author's webpage): https://github.com/Herbping/Nope

#### Last commit date:
27 Mar 2020 (last activity)

#### Last publication date:
12 July 2019

#### List of related papers:
[Proving Unrealizability for Syntax-Guided Synthesis](https://doi.org/10.1007/978-3-030-25540-4_18) (CAV'19)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: given a syntax-guided synthesis problem, checks whether it is realisable
:: Source :: https://doi.org/10.1007/978-3-030-25540-4 :: https://doi.org/10.1145/3550355.3552426
