#### Name:
FGL

#### Application domain/field:
Hardware verification
Microprocessors
Microcode verification
Symbolic simulation
Term rewriting

#### Type of tool (e.g. model checker, test generator):
Rewriter/Library for ACL2

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
FGL is described as a term rewriter that transforms expressions acting on fixed-size data into Boolean formulae.
One can then use equivalence checking between two sets of Boolean formulae to show that the implementation result matches the specification.

FGL is integrated into [ACL2](ACL2.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/acl2/acl2/tree/master/books/centaur/fgl

#### Last commit date:

#### Last publication date:
15 July 2021

#### List of related papers:
[Balancing Automation and Control for Formal Verification of Microprocessors](https://doi.org/10.1007/978-3-030-81685-8_2) (CAV '21)
[New Rewriter Features in FGL](https://doi.org/10.4204/EPTCS.327.3) (Workshop on the ACL2 Theorem Prover and its Applications '20)

#### Related tools (tools mentioned or compared to in the paper):
FGL is a rewrite and extension of [[GL]].

#### Meta
:: PV2 :: transforms expressions into Boolean formulae
:: Library
:: Source :: https://doi.org/10.1145/3550355.3552426