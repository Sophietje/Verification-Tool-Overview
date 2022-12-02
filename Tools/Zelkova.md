A policy analysis tool to reason about the semantics of AWS access control policies.

#### Name:
Zelkova

#### Application domain/field:
Cloud computing
Access control policies
Security

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
AWS policy

#### Expected input format:
- *AWS policy/policies*: AWS policy language, in JSON structure

#### Expected output:
Set of declarative statements about what is true of the system.
The user should check whether these findings are acceptable or not.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Tool that encodes access policies as logical formulas and uses SMT solvers to answer questions about these policies.

Uses [Z3](Solvers/SMT/Z3.md), [CVC4](Solvers/SMT/CVC4.md) and [[Z3Automata]] (in-house extension of Z3 to deal with regex).

#### Comments:
The way this tool should be used has significantly changed by the CAV '22 paper. The tool now returns a detailed set of findings about the system instead of letting the user write specifications.

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
2022

#### List of related papers:
[A Billion SMT Queries a Day](https://doi.org/10.1007/978-3-031-13185-1_1) (CAV 2022)
[Semantic-based Automated Reasoning for AWS Access Policies using SMT](https://doi.org/10.23919/FMCAD.2018.8602994) (FMCAD '18)

#### Related tools (tools mentioned or compared to in the paper):
[[SecGuru]], [IAM Access Analyzer](IAM%20Access%20Analyzer.md)

#### Meta
:: PV1 :: performs one of built-in checks on an access policy
:: Security
:: Source :: used by [[IAM Access Analyzer]] :: https://doi.org/10.1145/3550355.3552426
