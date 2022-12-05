#### Name:
Alloy Analyzer

#### Application domain/field:
State machines with complex structured state

#### Type of tool (e.g. model checker, test generator):
Constraint solver

#### Expected input thing:
Model (with assertions/properties)

#### Expected input format:
[[Alloy]] language

#### Expected output:
Counterexample or "assertion may be valid"

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The Alloy Analyzer translates the given problem into a boolean formula which is then handed to a SAT solver. When the SAT solver is done, the solution is translated back into the language of the original model. The user needs to specify a scope that bounds the size of the domains thereby making the problem finite and thus reducible to a boolean formula.
Uses SAT solvers to refute a formula.

It uses [Sat4j](Sat4j.md), [MiniSat](SAT/MiniSat.md), [plingeling](SAT/plingeling.md) and [Glucose](SAT/Glucose.md) for SAT solving.

#### Comments:
Domains (in the model) are bound by the user, resulting in a finite problem.

#### URIs (github, websites, etc.):
Project page: https://alloytools.org/
Repository: https://github.com/AlloyTools/org.alloytools.alloy

#### Last commit date:
04 Nov 2022 (default branch)
04 Nov 2022 (last activity)

#### Last publication date:

#### List of related papers:

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV3 :: checks user-specified assertions in Alloy models
:: Source :: used by [[Mapping Synthesis Tool]] :: https://doi.org/10.1145/3550355.3552426
