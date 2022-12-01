#### Name:
MU-CSeq

#### Application domain/field:
Multi-threaded programs
Sequentialization
Memory unwinding

#### Type of tool (e.g. model checker, test generator):
Concurrency preprocessor/code-to-code translator

#### Expected input thing:
- Multi-threaded program
- Specification file

#### Expected input format:
- *Multi-threaded program*: C program
- *Specification file*: ?

#### Expected output:
Sequentialized version of the original program.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
*Sequentialization*: Translate a concurrent program into a sequential one, using a code-to-code translation that preserves the property of interest. This sequential code is then analyzed using a symbolic sequential verification tool, e.g. [CBMC](Checkers/CBMC.md).

#### Comments:
-

#### URIs (github, websites, etc.):
MU-CSeq 0.4/Artifact of TACAS '16 paper: http://users.ecs.soton.ac.uk/gp4/cseq/mu-cseq-0.4.zip
Project page: https://github.com/CSeq/Overview#mu-cseq

#### Last commit date:
29 May 2021 (last activity)
29 May 2021 (last activity)
29 May 2021 (last activity)

#### Last publication date:
9 April 2016

#### List of related papers:
[MU-CSeq 0.4: Individual Memory Location Unwindings](https://doi.org/10.1007/978-3-662-49674-9_65) (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV2 :: sequentialises a parallel C program
:: C
:: Source :: https://doi.org/10.1145/3550355.3552426
