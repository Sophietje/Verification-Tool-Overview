Ultimate Taipan is a software model checker which combines trace abstraction and abstract interpretation

#### Name:
Ultimate Taipan

#### Application domain/field:
Software model checking
Model checking

#### Type of tool (e.g. model checker, test generator):
Software model checker

#### Expected input thing:
- Program
- Specification/property 
- Architecture
- Memory model
- *Optional*: witness

#### Expected input format:
- *Program*: one C file.
- *Specification*: `.prp` file from SV-COMP
- *Architecture*: the value `32bit` or `64bit`
- *Memory model*: the value `precise` or `simple` (this needs to be specified, but the tool always assumes `precise`)
- *Optional witness*: `.graphml` file

#### Expected output:
Whether the specification holds. If it does not hold then it will store a human readable counterexample in the file `UltimateCounterExample.errorpath` and a violation witness to `witness.graphml`.

If passed the argument `--validate` then it will validate the provided witness.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Implemented on top of the program analysis framework [Ultimate](https://doi.org/10.1007/978-3-662-54580-5_31). 
Uses [Z3](../Solvers/SMT/Z3.md) and [CVC4](../Solvers/SMT/CVC4.md)

#### Comments:
License: LGPLv3

#### URIs (github, websites, etc.):
Project page: https://monteverdi.informatik.uni-freiburg.de/tomcat/Website/?ui=tool&tool=taipan
Try online: https://monteverdi.informatik.uni-freiburg.de/tomcat/Website/?ui=int&tool=taipan
Repository (of the Ultimate framework): https://github.com/ultimate-pa/ultimate/

#### Last commit date:
10 October 2021 (this is for the complete Ultimate framework, it is unclear when the Taipan part is last updated)

#### Last publication date:
17 April 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-45237-7_32 (TACAS '20, Competition contribution)
https://doi.org/10.1007/978-3-319-89963-3_31 (TACAS '18, Competition contribution)
https://doi.org/10.1007/978-3-662-54580-5_31 (TACAS '17, Competition contribution)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C
:: PV4 :: checks properties of a C program for a specified architecture and memory model
:: Model checking
