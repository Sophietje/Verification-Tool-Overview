GACAL verifies C programs by searching over the space of possible invariants, using traces of the input program to identify potential invariants. 

#### Name:
GACAL

#### Application domain/field:
Reachability
Invariant generation
Program traces
Conjecture generation

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Program
- Properties to check?

#### Expected input format:
- *Program*: C code
- *Properies*: ?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
GACAL uses the [ACL2s](Provers/ACL2s.md) theorem prover to verify these potential invariants, using an interface provided by ACL2s for connecting with external tools. GACAL iteratively searches for and proves invariants of increasing complexity until the program is verified.

#### Comments:
License: GNU GPLv3

#### URIs (github, websites, etc.):
Repository: https://gitlab.com/acl2s/conjecture-generation/gacal
SV-COMP 2020 submission/artifact: http://doi.org/10.5281/zenodo.3681607

#### Last commit date:
16 January 2020

#### Last publication date:
17 April 2020

#### List of related papers:
[GACAL: Conjecture-Based Verification](https://doi.org/10.1007/978-3-030-45237-7_26) (TACAS '20)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV2 :: generates increasingly stronger invariants for an external prover
:: Source :: https://doi.org/10.1145/3550355.3552426