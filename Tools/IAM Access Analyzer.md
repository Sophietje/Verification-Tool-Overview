Tool to help users reason about the semantics of their Identity and Access Management (IAM) policies.

#### Name:
IAM Access Analyzer

#### Application domain/field:
Security policies
Cloud
Identity and Access Management (IAM)
Resource policies
Access control policy
Predicate abstraction

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Policy $p$
- Set of partially ordered predicates $\Phi$

#### Expected input format:
- *Policy*: IAM policy language
- *Set of predicates*: ?

#### Expected output:
Minimal covering of $p$ comprising only irreducible findings

Findings are presented through a web console and APIs.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Zelkova](Zelkova.md) as access oracle.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://aws.amazon.com/iam/

#### Last commit date:
-

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_9 (CAV '20)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Security
:: PV2 :: generates findings covering a given access policy