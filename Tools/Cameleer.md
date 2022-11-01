Deductive verifier for OCaml

#### Name:
Cameleer

#### Application domain/field:
Deductive verification
Functional programming

#### Type of tool (e.g. model checker, test generator):
Deductive verifier

#### Expected input thing:
GOSPEL-annotated OCaml program.
The annotations are in the form of things such as preconditions, (exceptional) postconditions and loop (in)variants.

#### Expected input format:
`.ml` file

#### Expected output:
It will launch the Why3 IDE from which one can use different theorem provers to discharge all proof obligations.
The tool tries to translate a Why3 error back to the OCaml program if the input program is not accepted for some reason.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Cameleer takes a GOSPEL-annotated OCaml program and translates it into WhyML.
Uses [Why3](Frameworks/Why3.md), [Alt-Ergo](Solvers/SMT/Alt-Ergo.md), [CVC4](Solvers/SMT/CVC4.md), [Z3](Solvers/SMT/Z3.md) and [GOSPEL](../Formats/GOSPEL.md).

#### Comments:
It does not support the complete OCaml language yet. Some things that are not supported include Generalized Algebraic Data Types (GADTs) and polymorphic variants.

#### URIs (github, websites, etc.):
Project page: https://mariojppereira.github.io/cameleer.html
Repository: https://github.com/ocaml-gospel/cameleer
Artifact for CAV '21 paper: https://zenodo.org/record/4724119

#### Last commit date:
27 September 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[Cameleer: A Deductive Verification Tool for OCaml](https://doi.org/10.1007/978-3-030-81688-9_31) (CAV '21)
[GOSPEL—Providing OCaml with a Formal Specification Language](https://doi.org/10.1007/978-3-030-30942-8_29) (FM '19, paper that introduces the GOSPEL specification language for OCaml)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: OCaml
:: PV6 :: generates a proof of desired properties, can be used interactively