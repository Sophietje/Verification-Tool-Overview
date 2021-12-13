Endicheck is a dynamic analysis tool for detecting endianness bugs, based on [Valgrind](Frameworks/Valgrind.md)

#### Name:
Endicheck

#### Application domain/field:
Endianness bugs
Dynamic analysis
Bug detection

#### Type of tool (e.g. model checker, test generator):
Bug detector

#### Expected input thing:
Program and some annotations to mark the byte-swapping and I/O functions.

#### Expected input format:
C/C++ program. 
The annotations are written in the program source code using the annotations defined in the C header file endicheck.h

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
**Endianness**: ordering of bytes used to represent numbers.

Endicheck was initially created as a fork of [Valgrind](Frameworks/Valgrind.md). 

#### Comments:
License: GPL

#### URIs (github, websites, etc.):
Repository: https://github.com/rkapl/endicheck

#### Last commit date:
30 January 2020

#### Last publication date:
17 April 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-45237-7_15 (TACAS '20)

#### Related tools (tools mentioned or compared to in the paper):
[[Sparse]], [Valgrind](Frameworks/Valgrind.md), [[Memcheck]], [[Hobbes]], [[DataFlowSanitizer]], 