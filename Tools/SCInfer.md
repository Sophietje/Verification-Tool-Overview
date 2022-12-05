A tool to verify masking countermeasures.

#### Name:
SCInfer

#### Application domain/field:
Side channel attacks
Security verification
Power side-channel leaks
Cryptographic algorithms

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Program $P$
- Sets of public $p$
- Secret $k$
- Random $r$ variables
- Empty map $\pi$

#### Expected input format:
?

#### Expected output:
The map indicates per node (in the data dependency graph (DDG) of the program) whether it is perfectly masked (SID), not perfectly masked (NPM) or unknown (UKD).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Author's webpage with link to the VM and source code: https://faculty.sist.shanghaitech.edu.cn/faculty/songfu/

#### Last commit date:
?

#### Last publication date:
18 July 2018

#### List of related papers:
[SCInfer: Refinement-Based Verification of Software Countermeasures Against Side-Channel Attacks](https://doi.org/10.1007/978-3-319-96142-2_12) (CAV '18)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Security
:: PV1 :: determines whether nodes of a cryptographic program are perfectly masked
:: Source :: https://doi.org/10.1007/978-3-319-96142-2 :: https://doi.org/10.1145/3550355.3552426
