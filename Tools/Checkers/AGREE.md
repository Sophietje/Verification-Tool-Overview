#### Name:
AGREE: Assume Guarantee Reasoning Environment

#### Application domain/field:
Model checking
Cyber-physical systems
System design verification
Assume-guarantee contracts

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
AADL model

#### Expected input format:
`.aadl` file

#### Expected output:
Per property it indicates whether it could be verified in the GUI. If it could not be verified there the user can view a counterexample that demonstrates the failure.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Infinite-state model checker.
- Can analyse systems with real-valued variables.
- Translates an AADL model and the corresponding contracts into Lustre, then uses JKind for the back-end analysis.
- Uses [Z3](../Solvers/SMT/Z3.md), [JKind](JKind.md)

#### Comments:

#### URIs (github, websites, etc.):
Project page: http://loonwerks.com/tools/agree.html
Repository: https://github.com/loonwerks/AGREE

#### Last commit date:
29 Sep 2022

#### Last publication date:
September 2021

#### List of related papers:
https://doi.org/10.1016/j.ress.2021.107649 (Reliability Engineering & System Safety '21)
https://doi.org/10.1007/978-3-642-28891-3_13 (NFM '12)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: AADL
:: PV3           :: checks properties against an AADL model
:: Model checking