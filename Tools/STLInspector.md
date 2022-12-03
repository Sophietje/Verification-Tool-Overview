Tool for the systematic validation of Signal Temporal Logic (STL) specifications against informal textual requirements.

#### Name:
STLInspector

#### Application domain/field:
Signal Temporal Logic (STL)
Requirements
Mutation testing

#### Type of tool (e.g. model checker, test generator):
Debug/testing tool for STL specifications

#### Expected input thing:
STL formula

#### Expected input format:
Own textual format

#### Expected output:
User is presented with test signals for which needs to be decided whether or not the signal satisfies the informal requirement. If an error was found, the user can change the STL candidate and continue inspection.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
STLInspector tries to identify typical faults that occur in the process of formalizing requirements by mutating a candidate STL specification.
The requirements engineer is used as an oracle.

Uses [ANTLR](Not-verifiers/ANTLR.md), [Z3](Solvers/SMT/Z3.md).

#### Comments:
License: Apache License 2.0

#### URIs (github, websites, etc.):
Repository: https://github.com/STLInspector/STLInspector

#### Last commit date:
30 Sep 2019 (default branch)
30 Sep 2019 (last activity)

#### Last publication date:
13 July 2017

#### List of related papers:
[STLInspector: STL Validation with Guarantees](https://doi.org/10.1007/978-3-319-63387-9_11) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
Tool to formalize specifications: [[Vispec]]
Tool to debug specifications (subset of PSL): [[RATSY]]

#### Meta
:: STL
:: PV1 :: aids the creation of signal temporal logic specs
:: Source :: https://doi.org/10.1007/978-3-319-63387-9 :: https://doi.org/10.1145/3550355.3552426
