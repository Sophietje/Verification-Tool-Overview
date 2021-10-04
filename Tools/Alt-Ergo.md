SMT solver

#### Name:
Alt-Ergo

#### Application domain/field:
SMT solving

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SMT formula

#### Expected input format:
One of the following:
- `.ae` file for its native input language
- `.why`: deprecated but still accepted
- `.mlw`: deprecated but still accepted
- `.psmt2`: polymorphic extension of the [SMT-LIB](SMT-LIB.md) 2 format
- `.smt2`: [SMT-LIB](SMT-LIB.md) 2 format

#### Expected output:
`Valid`, `Invalid` or `I don't know` if the user used its native input language (`.ae` files). It can also output in the SMT-LIB 2 form if asked.
`unsat`, `sat` or `unknown` if the user used the [SMT-LIB](SMT-LIB.md) 2 input format (i.e. `.psmt2` or `.smt2` files)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Alt-Ergo is used by [Frama-C](Frama-C), [SPARK](SPARK.md), [Why3](Why3.md), [[Atelier-B]] and [[Caveat]].

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://alt-ergo.ocamlpro.com/
Repository: https://github.com/OCamlPro/alt-ergo
Documentation: https://ocamlpro.github.io/alt-ergo/index.html
Try online: https://try-alt-ergo.ocamlpro.com/

#### Last commit date:
13 September 2021

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63390-9_22 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):



