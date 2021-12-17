#### Name:
LOBER: Lower-Bound Synthesizer

#### Application domain/field:
Lower bound approximation
Cost approximation
Worst-case cost
Resources

#### Type of tool (e.g. model checker, test generator):
Cost approximator?

#### Expected input thing:
?

#### Expected input format:
KoAT file

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
*Cost approximation*: Find a bound for the cost of program's executions. This is useful if you want to know things such as "the program will not exceed X amount of memory".
This program specifically focuses on finding lower bounds of the worst-case cost. 

Uses [Barcelogic](Solvers/SMT/Barcelogic.md), [Z3](Solvers/SMT/Z3.md).

#### Comments:

#### URIs (github, websites, etc.):
Online web interface: http://costa.fdi.ucm.es/lober

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_40 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [[LoAT]]
