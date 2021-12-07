#### Name:
cake_lpr

#### Application domain/field:
Proof checking

#### Type of tool (e.g. model checker, test generator): 
Proof checker

#### Expected input thing:
A proof in LPR (Linear Propagation Redundancy)

#### Expected input format:

#### Expected output:
SAT? or VERIFIED UNSAT or resource exhaustion error

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Built on top of [[CakeML]]; [HOL](Provers/HOL.md)4
The same paper has a tool to convert PR to LPR

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/tanyongkiam/cake_lpr

#### Last commit date:

#### Last publication date:
Publication: conf/tacas/TanHM21
Commit: 04.01.2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-72013-1_12 (TACAS '21)

#### Comments:
LPR is somewhat weaker than PR
PR generalises RAT (Resolution Asymmetric Tautology)
RAT is a de facto standard