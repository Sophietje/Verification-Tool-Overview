Tool for synthesis of small loop-free programs

#### Name:
SYNUDIC

#### Application domain/field:
Program synthesis
Component-based synthesis (CoS)

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
Sketch of the desired program. 

This consists of a description of the library and a template of a straight-line program. A library describes all the available components that can be used in the program.

#### Expected input format:
`.sketch` file (own format)

#### Expected output:
Program meeting the specification/sketch of the desired program.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Yices](../Solvers/SMT/Yices.md) or [Z3](Z3.md)

SYNUDIC converts the input file into a (EF-)Yices formula or an exists SMT formula. It then calls an SMT solver.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/adriagascon/synudic

#### Last commit date:
21 September 2017

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63390-9_5 (CAV '17)
https://doi.org/10.1007/978-3-319-21401-6_33 (CADE '15)

#### Related tools (tools mentioned or compared to in the paper):
