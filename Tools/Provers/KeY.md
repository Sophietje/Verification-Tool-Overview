platform for deductive verification of Java programs

#### Name:
KeY

#### Application domain/field:
design contract
floating point
Interactive theorem prover
Deductive verification
Functional verification

#### Type of tool (e.g. model checker, test generator): 
Semi-interactive verifier

#### Expected input thing:
Annotated source code

#### Expected input format:
(Sequential) Java or Java Card 2.2.X program annotated with properties specified in [JML](../../Formats/JML.md) or Java Dynamic Logic ([[JavaDL]]).

#### Expected output:
Whether the specified properties can be proven  correct.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
translates source code to [[JavaDL]].
can translate to the [SMT-LIB](../../Formats/SMT-LIB.md) format and call an external SMT solver.

The user can choose to use the tool in an automatic or interactive fashion. Typically the user would first try to let the prover find a proof automatically, if it then does not succeed, the user can get involved in the proving process.

#### Comments:
?

#### URIs (github, websites, etc.):
Project page: https://www.key-project.org/

#### Last commit date:
Latest stable release is from 18 December 2020 (https://www.key-project.org/download/).

#### Last publication date:
23 March 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-72013-1_13
https://doi.org/10.1007/978-3-319-49812-6
https://doi.org/10.1007/978-3-319-12154-3_4

#### Related tools (tools mentioned or compared to in the paper):
?
