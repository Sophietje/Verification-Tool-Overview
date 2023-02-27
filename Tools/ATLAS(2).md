Tool for fully-automated amortised cost analysis of self-adjusting data structures (i.e. splay trees, splay heaps and pairing heaps).

#### Name:
ATLAS

#### Application domain/field:
Data structures
Self-adjusting data structures
Amortised complexity analysis

#### Type of tool (e.g. model checker, test generator):
Complexity analyser

#### Expected input thing:
?

#### Expected input format:
`.ml` file

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Amortised analysis is a method for the worst-case cost/complexity analysis of data structures. In this paper they present a technique to do this amortised cost analysis of self-adjusting data-structures fully automated.

In the CAV '22 paper they extended the tool to deal with probabilistic data structures such as randomised splay trees, randomised meldable heaps and randomised analysis of a binary search tree.

Uses [Z3](Solvers/SMT/Z3.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/lorenzleutgeb/atlas/

#### Last commit date:
03 Nov 2022 (default branch)
15 Nov 2022 (last activity)

#### Last publication date:
6 August 2022

#### List of related papers:
[Automated Expected Amortised Cost Analysis of Probabilistic Data Structures](https://doi.org/10.1007/978-3-031-13188-2_4) (CAV '22)
[ATLAS: Automated Amortised Complexity Analysis of Self-adjusting Data Structures](https://doi.org/10.1007/978-3-030-81688-9_5) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
uses [[Z3]]

#### Meta
:: Complexity
:: PV1 :: checks or infers types by static analysis
:: Source :: https://doi.org/10.1007/978-3-030-81688-9 :: https://doi.org/10.1145/3550355.3552426
