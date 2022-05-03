Automatically infers Python 3 type annotations

#### Name:
Typpete

#### Application domain/field:
Type inference
Type annotations

#### Type of tool (e.g. model checker, test generator):
Type inferer

#### Expected input thing:
Program

#### Expected input format:
(large subset of) Python 3

#### Expected output:
Program with type annotations, a type error, or an error indicating use of unsupported language features.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Typpete automatically infers sound (non-gradual) type annotations for Python 3 programs. It can be used as a preprocessor for other analysis or verification tools.

Uses [Z3](Solvers/SMT/Z3.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/caterinaurban/Typpete

#### Last commit date:
6 December 2018

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_2 (CAV '18)

#### Related tools (tools mentioned or compared to in the paper):
Other type inference tools for Python: [[Pytype]], [[Starkiller]], [[MyPy]], [[PyAnnotate]]

#### Meta
:: Python
:: PV2 :: infers type annotations for Python programs