#### Name:
cake_lpr

#### Application domain/field:
Proof checking

#### Type of tool (e.g. model checker, test generator): 
SMT solver

#### URIs (github, websites, etc.):
https://github.com/tanyongkiam/cake_lpr

#### Expected input:
A proof in LPR (Linear Propagation Redundancy)

#### Expected output:
SAT? or VERIFIED UNSAT or resource exhaustion error

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Built on top of [[CakeML]]; [[HOL]]4
The same paper has a tool to convert PR to LPR


#### Last publication date:
Publication: conf/tacas/TanHM21
Commit: 04.01.2021

#### List of related papers:

#### Comments:
LPR is somewhat weaker than PR
PR generalises RAT (Resolution Asymmetric Tautology)
RAT is a de facto standard