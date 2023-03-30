#### Name:
EXIST

#### Application domain/field:
Probabilistic programs
Invariant generation

#### Type of tool (e.g. model checker, test generator):
Invariant inference tool

#### Expected input thing:
- Number of runs
- Number of states
- Whether to learn a subinvariant or an exact invariant

#### Expected input format:
Has to be passed as parameters to the Python program.
If you want to run it on a different program/benchmark, then one should encode the program in their specific Python files.

#### Expected output:
Invariants

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Infers invariants for probabilistic programs.
Exist will execute the program multiple times on a set of input states. It uses machine learning to learn models encoding possible invariants. 

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/JialuJialu/Exist

#### Last commit date:
03 Feb 2023 (last activity)

#### Last publication date:
2022

#### List of related papers:
[Data-Driven Invariant Learning for Probabilistic Programs](https://doi.org/10.1007/978-3-031-13185-1_3) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Other tool for inferring invariants for probabilistic programs: [[PRINSYS]]
Tool for computing expected values after probabilistic loops: [[MORA]]

#### Meta
:: Probabilistic programs
:: Synthesis
:: Source :: https://doi.org/10.1007/978-3-031-13185-1
