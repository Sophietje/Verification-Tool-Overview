#### Name:
MetaVal

#### Application domain/field:
Model checking
Witnesses
Witness validation

#### Type of tool (e.g. model checker, test generator):
Witness validator (used in software model checking)

#### Expected input thing:
- Program
- Specification
- Witness

#### Expected input format:
- *Program*: C code
- *Specification*: SV-COMP format for specifications, `.prp` file
- *Witness*: SV-COMP format for witnesses (https://github.com/sosy-lab/sv-witnesses/)

#### Expected output:
Per witness it reports whether it is confirmed (true/false) and the time it took to check it. 
It also presents a summary of statistics (number of correct, incorrect and unknown witnesses).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [CPAchecker](Checkers/CPAchecker.md).

#### Comments:
A witness is a counterexample that can be used to observe a certain bug/error. This can be useful for debugging, generating tests, and more.
A witness validator is used to verify that the witness is indeed a valid witness.

#### URIs (github, websites, etc.):
Repository: https://gitlab.com/sosy-lab/software/metaval/

#### Last commit date:
January 2021

#### Last publication date:
14 July 2020

#### List of related papers:
[MetaVal: Witness Validation via Verification](https://doi.org/10.1007/978-3-030-53291-8_10)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Model checking
:: PV1 :: checks whether the witness for a specific program and property is valid
:: Source :: https://doi.org/10.1007/978-3-030-53291-8 :: https://doi.org/10.1145/3550355.3552426
