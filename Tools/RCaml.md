Refinement type checking and inference system for OCaml

#### Name:
RCaml

#### Application domain/field:
Refinement type checking
Horn constraint solving
Inductive proofs
Relational specifications
Inductive theorem proving
Functional language

#### Type of tool (e.g. model checker, test generator):
Refinement-based verifier

#### Expected input thing:
OCaml program

#### Expected input format:
`.ml` file

#### Expected output:
`Safe` with a proof log/tree, or `Unsafe` and a counterexample/disproof.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://lfp.dip.jp/rcaml/

#### Last commit date:
-

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63390-9_30 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
Automated inductive theorem techniques/tools: [ACL2s](Provers/ACL2s.md), [[SPIKE]], [[CLAM]], [[IsaPlanner]], [[Leon]], [Dafny](Dafny.md), [[Zeno]], [[HipSpec]], [CVC4](Solvers/SMT/CVC4.md).

Other Horn constraint solver: [[𝜇Z]] (extension of [Z3](Solvers/SMT/Z3.md))