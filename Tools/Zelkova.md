A policy analysis tool to reason about the semantics of AWS access control policies.

#### Name:
Zelkova

#### Application domain/field:
Cloud computing
Access control policies
Security

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
Two AWS policies to compare **or** one AWS policy and the name of a built-in Zelkova check.

#### Expected input format:
- *AWS policy/policies*: AWS policy language, in JSON structure
- *Name of Zelkova check*: passed as an argument

#### Expected output:
*When comparing policies*: it returns whether the first policy in the payload is less permissive, more permissive, equivalent or incomparable with respect to the second policy

*For built-in Zelkova check*: returns `true` or `false` based on whether the check is satisfied. It can also return `unknown` if it could not handle a construct in the policy or the solver times out.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Tool that encodes access policies as logical formulas and uses SMT solvers to answer questions about these policies.

Uses [Z3](Solvers/SMT/Z3.md), [CVC4](Solvers/SMT/CVC4.md) and [[Z3Automata]] (in-house extension of Z3 to deal with regex).

#### Comments:
-

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
2018

#### List of related papers:
https://doi.org/10.23919/FMCAD.2018.8602994 (FMCAD '18)

#### Related tools (tools mentioned or compared to in the paper):
[[SecGuru]], [IAM Access Analyzer](IAM%20Access%20Analyzer.md)

#### Meta
