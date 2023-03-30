BCV-based solver for DS-inclusion.

#### Name:
QuIP

#### Application domain/field:
Quantitative inclusion
Automata
Discounted-sum inclusion
Weighted automata

#### Type of tool (e.g. model checker, test generator):
Property checker (DS-inclusion)

#### Expected input thing:
- Weighted automata P, Q
- Discounted-factor $d$

#### Expected input format:
?

#### Expected output:
Whether $P \subseteq_d Q$

#### Internals (tools used, frameworks, techniques, paradigms, ...):
BCV is an algorithm for solving DS-inclusion. The name BCV is derived from the name of the authors.
DS-inclusion is about determining the quantitative inclusion for nondeterministic discounted-sum (DS) automata.

Uses [RABIT](../RABIT.md) to check language inclusion and [Reduce](../Reduce.md) for minimizing Büchi automata.

#### Comments:
-

#### URIs (github, websites, etc.):
Possibly the following repository from the first author's github: https://github.com/suguman/QIP/ (*not linked in the paper or on the first author's website*)

#### Last commit date:
26 Sep 2018 (last activity)

#### Last publication date:
18 July 2018

#### List of related papers:
[Automata vs Linear-Programming Discounted-Sum Inclusion](https://doi.org/10.1007/978-3-319-96142-2_9)

#### Related tools (tools mentioned or compared to in the paper):
[DetLP](../DetLP.md)

#### Meta
:: Automaton
:: PV1 :: comparator of two weighted automata
:: Source :: https://doi.org/10.1007/978-3-319-96142-2 :: https://doi.org/10.1145/3550355.3552426
