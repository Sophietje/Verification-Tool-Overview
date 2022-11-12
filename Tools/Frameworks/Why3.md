Why3 environment for deductive program verification is built around a kernel that implements a formal specification language, based on typed first-order logic

#### Name:
Why3

#### Application domain/field:
Deductive verification
Verification conditions

#### Type of tool (e.g. model checker, test generator):
Deductive verifier/verification infrastructure

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Given a [[WhyML]] program, Why3 will generate verification conditions which can be discharged using automated or interactive theorem provers.
- Users can also write [[WhyML]] programs directly and get a correct-by-construction OCaml program.
- [[WhyML]] is a language specifically for Why3. It is used as an intermediate language for the verification of C, Java, or Ada programs.

#### URIs (github, websites, etc.):
Project page: http://why3.lri.fr/
Try online: http://why3.lri.fr/try/
Repository: https://gitlab.inria.fr/why3/why3

#### Last commit date:
14 January 2022

#### Last publication date:
2020

#### List of related papers:
[Abstraction and Genericity in Why3](https://doi.org/10.1007/978-3-030-61362-4_7) (ISoLA '20)
[Why3 — Where Programs Meet Provers](https://doi.org/10.1007/978-3-642-37036-6_8) (ESOP '13)

#### Related tools (tools mentioned or compared to in the paper):
Projects that use Why3: [Frama-C](Frama-C.md), [SPARK](../SPARK.md), [[Krakatoa]]

#### Meta
:: Framework
:: OCaml
:: C
:: Java
:: Ada
:: PV2 :: can generate correct OCaml programs or use external provers to discharge verification conditions
:: Source :: https://doi.org/10.1145/3550355.3552426
