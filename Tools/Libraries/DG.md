Library providing data structures and algorithms for program analysis and slicing

#### Name:
DG

#### Application domain/field:
Points-to analysis
Call graph construction
Data dependence analysis
LLVM

#### Type of tool (e.g. model checker, test generator):
Library

#### Expected input thing:
Depends on how the library is used.

#### Expected input format:
LLVM IR

#### Expected output:
Depends on how the library is used. 

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Includes algorithms for the computation of NTSCD (non-termination sensitive control dependence), DOD (decisive order dependence) and the NTSCD and DOD closure

DG contains several scripts/tools to deal with bitcode. The main interesting tool seems to be `llvm-slicer` which is a static slicer for LLVM bitcode.

#### Comments:
This was made during the re-implementation of the tool [Symbiotic](Symbiotic.md). Its original purpose was for the construction of dependence graphs for LLVM bitcode.

License: MIT license

#### URIs (github, websites, etc.):
Repository: https://github.com/mchalupa/dg

#### Last commit date:
29 Jun 2022

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_41 (CAV '21)
https://doi.org/10.1007/978-3-030-59152-6_33 (ATVA '20)
https://doi.org/10.1016/j.simpa.2020.100038 (Software Impacts '20)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Library
:: PV0 :: a library that provides data structures and algorithms for program analysis and slicing