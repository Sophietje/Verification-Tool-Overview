MachSMT is an algorithm selection tool for Satisfiability Modulo Theories (SMT) solvers

#### Name:
MachSMT

#### Application domain/field:
Algorithm selection/solver selection
SMT solving

#### Type of tool (e.g. model checker, test generator):
Solver selector for SMT problems

#### Expected input thing:
Input benchmark and its library files

#### Expected input format:
[SMT-LIB](SMT-LIB.md)

#### Expected output:
Ranking of solvers that are expected to have the lowest runtime

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It uses empirical hardness models (EHMs) and pairwise ranking comparators (PWCs) to perform algorithm selection.
To do this, it uses frequencies of grammatical constructs from the [SMT-LIB](SMT-LIB.md) language, an some other syntactical metrics.

Uses [[Bitwuzla]], [[COLIBRI]], [[CVC4]], [[MathSAT5]], [[Q3B]], [[SPASS-SATT]], [[Vampire]], [Yices](../Solvers/SMT/Yices.md), [[Z3]]

#### Comments:
There are in total 3 'tools' that are part of MachSMT, our description above focuses on the primary interface of MachSMT. There is also a tool for building MachSMT's database (`machsmt_build`), and a tool to evaluate the results of `machsmt_build` under k-fold cross validation (`machtsmt_eval`)

#### URIs (github, websites, etc.):
Artifact TACAS '21: https://zenodo.org/record/4458699
Repository (Artifact for TACAS '21): https://github.com/MachSMT/MachSMT

#### Last commit date:
29 June 2021 (for the repository with the TACAS '21 artifact)

#### Last publication date:
23 March 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-72013-1_16 (TACAS '21)

#### Related tools (tools mentioned or compared to in the paper):
[SATzilla](SATzilla.md)

