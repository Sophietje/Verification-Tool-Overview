Collection of libraries and tools for the analysis and verification of LLVM code and transformations

#### Name:
Alive2

#### Application domain/field:
Compiler
Translation validation
Bounded analysis
Refinement

#### Type of tool (e.g. model checker, test generator):
Translation validation tool for LLVM's IR

#### Expected input thing:
Depends on the library/tool used.

#### Expected input format:
-

#### Expected output:
Depends on the library/tool used.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This framework has been made to find bugs in LLVM. 
*Translation validation*: A technique where an individual translation (e.g. a run of the  compiler) is validated (i.e. verifies that the target code produced on this run correctly implements the submitted source program) instead of proving the correctness of the compiler beforehand. (Source: "Translation Validation" by A. Pnueli, M. Siegel and E. Singerman, TACAS 1998)

It includes the following libraries:
- Alive2 IR
- Symbolic executor
- LLVM to Alive2 IR converter
- Refinement check (i.e. optimization verifier)
- SMT abstraction layer

It includes the following tools:
- Alive drop-in replacement
- Translation validation plugins for clang and LLVM's `opt`
- Standalone translation validation tool: `alive-tv`

Uses [Z3](Z3.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/AliveToolkit/alive2
Online version of `alice-tv` tool: https://alive2.llvm.org/ce/

#### Last commit date:
3 October 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_35 (CAV '21)
https://doi.org/10.1145/3453483.3454030 (PLDI '21)
#### Related tools (tools mentioned or compared to in the paper):