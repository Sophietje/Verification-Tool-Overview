#### Name:
TheSy: Theory Synthesis, pronounced Tessy

#### Application domain/field:
Theorem generation
Deductive inference
Theory exploration
Theory synthesis
Lemma discovery

#### Type of tool (e.g. model checker, test generator):
Meta-tool? Synthesis tool?

#### Expected input thing:
Base set of inductive data types and recursive definitions

#### Expected input format:
Own format (`.th` files) or [SMT-LIB](../Formats/SMT-LIB.md) v2.6, based on uninterpreted function theory, limited to universal quantifications

#### Expected output:
Library of lemmas

#### Internals (tools used, frameworks, techniques, paradigms, ...):
TheSy focuses on discovering lemmas.
Lemmas are often used in verification tools such as [Dafny](Dafny.md), [Coq](Provers/Coq.md) and [Isabelle/HOL](Provers/Isabelle-HOL.md) to state background knowledge.
It's technique is based on syntax-guided enumerative synthesis. 

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/eytans/TheSy

#### Last commit date:
29 April 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_6 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '21 paper: [[Hipster]]
Tools for theory exploration: [[IsaCoSy]], [[QuickSpec]]

#### Meta
:: Synthesis
:: PV2 :: discovers lemmas based on data types and recursive definitions