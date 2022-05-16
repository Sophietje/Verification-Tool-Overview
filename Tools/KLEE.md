#### Name:
KLEE

#### Application domain/field:
Symbolic execution
Dynamic symbolic execution
Bug finding
Test generation

#### Type of tool (e.g. model checker, test generator):
Symbolic execution engine

#### Expected input thing:
- Program
- Optionally KLEE and/or program options, e.g. whether to check for integer overflows.

#### Expected input format:
- Program: LLVM bitcode file (.bc)
- Optional: options passed as arguments when calling KLEE

#### Expected output:
KLEE generates some statistics (e.g. how many generated tests, running time, number of explored paths, etc.), warnings emitted by KLEE, and other messages emitted by KLEE. 

The output can be found in the terminal or in a text file. Moreover, it also generates a human readable version of the bitcode executed by KLEE, a SQLite file with statistics and an istats file with statistics.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Symbolic execution can be used for several purposes including test generation, bug finding, 

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/klee/klee/
Project page: https://klee.github.io/

#### Last commit date:
19 June 2021

#### Last publication date:
2 June 2020

#### List of related papers:
https://doi.org/10.1007/s10009-020-00570-3
https://doi.org/10.1007/978-3-642-34129-8_23
https://doi.org/10.1109/Trustcom.2015.608
https://llvm.org/pubs/2008-12-OSDI-KLEE.html

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV3 :: checks properties by symbolic execution