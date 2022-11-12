#### Name:
Isabelle/HOL

#### Application domain/field:
Interactive theorem proving
Proof assistant
Deductive verification

#### Type of tool (e.g. model checker, test generator):
Interactive theorem prover/proof assistant

#### Expected input thing:
A 'theory' that you want to proof correct. A theory is a collection of types, functions and theorems.

#### Expected input format:
HOL (for the formula that should be proven)
and Isar (language for writing proof scripts).

#### Expected output:
Whether the mathematical formula has been proven. It is also possible to turn (verified) executable specifications into code (SML, OCaml, Haskell or Scala).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This is an *interactive* theorem prover based on higher-order logic. It is sometimes also called a "proof assistant". You can use it to prove the correctness of mathematical formulas. E.g. you can use it to verify the correctness of a protocol. Note that proving the correctness of something is an *interactive* process, while the tool can deduce some things automatically, it will often require user interaction! This interaction is done through writing proof scripts in the Isar language.
Isabelle is also capable of turning executable specifications directly into code in SML, OCaml, Haskell and Scala.

#### Comments:

#### URIs (github, websites, etc.):
Project page: https://isabelle.in.tum.de/overview.html
Library of examples/applications: https://www.isa-afp.org/
Manual (last updated February 2021): https://isabelle.in.tum.de/dist/library/Doc/System/system.pdf

#### Last commit date:
February 2021

#### Last publication date:
2014 (note this is for papers *about* Isabelle, there are a lot of papers that *use* it that have been published later)

#### List of related papers:
[Data Refinement in Isabelle/HOL](https://doi.org/10.1007/978-3-642-39634-2_10)
[Type Classes and Filters for Mathematical Analysis in Isabelle/HOL](https://doi.org/10.1007/978-3-642-39634-2_21)
[Truly Modular (Co)datatypes for Isabelle/HOL](https://doi.org/10.1007/978-3-319-08970-6_7)
[Extending Sledgehammer with SMT Solvers](https://doi.org/10.1007/978-3-642-22438-6_11)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV6 :: interactive theorem prover
:: Source :: https://doi.org/10.1145/3550355.3552426
