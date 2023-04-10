#### Name:
SAW: Software Analysis Workbench

#### Application domain/field:
Software verification
Automated reasoning

#### Type of tool (e.g. model checker, test generator):
Equivalence checker/symbolic execution engine?

#### Expected input thing:
- Program
- *Optional*: A specification, consisting of three components:
	1. A specification of the initial state before execution of the function
	2. A description of how to call the function within that state
	3. A specification of the expected final value of the program state.

#### Expected input format:
- *Program*: C, Java or Cryptol program or its own SAWScript language. 
- *Specifications*: ?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Open-source symbolic analysis engine developed by [Galois](https://galois.com/). It uses symbolic execution to reason about a program. It can be used for bug finding and equivalence checking.
Uses [ABC](Frameworks/ABC.md), [Yices](Solvers/SMT/Yices.md), [Z3](Solvers/SMT/Z3.md).

"SAW was designed with cryptographic implementations in mind, but also supports general purpose imperative programs."

#### Comments:
-

#### URIs (github, websites, etc.):
General info about the project on Galois' website: https://galois.com/project/software-analysis-workbench/
Project page: https://saw.galois.com/
Repository: https://github.com/galoisinc/saw-script
Tutorial: https://saw.galois.com/tutorial.html
Manual: https://saw.galois.com/manual.html

#### Last commit date:
07 Apr 2023 (last activity)

#### Last publication date:
8 November 2016

#### List of related papers:
[Constructing Semantic Models of Programs with the Software Analysis Workbench](https://doi.org/10.1007/978-3-319-48869-1_5) (VSTTE 2016)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: C
:: Java
:: PV5 :: extracts an algorithmic spec from source code and uses it on backend verifiers
:: Source :: https://doi.org/10.1145/3550355.3552426
