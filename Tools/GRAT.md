SAT solver certificate checking tool

#### Name:
GRAT

#### Application domain/field:
SAT solving
Certificate checking

#### Type of tool (e.g. model checker, test generator):
Metatool?

#### Expected input thing:
- SAT problem
- SAT certificate

#### Expected input format:
- *SAT problem*: `.cnf` file ([DIMACS](../Formats/DIMACS.md) format)
- *SAT certificate*: `.sat` file

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
GRAT is supposed to be used as follows: you provide a certificate, if this is verified, then you have strong formal guarantees that the solution produced by the SAT solver was actually correct.

GRAT consists of two programs [[gratgen]] and [[gratchk]]. gratgen converts a DRAT certificate to a GRAT certificate. gratchk will check the output of gratgen against the original formula.

The soundness of gratchk has been formally proven in [Isabelle/HOL](Provers/Isabelle-HOL.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www21.in.tum.de/~lammich/grat/

#### Last commit date:
Last update seems to be from December 2018

#### Last publication date:

#### List of related papers:

#### Related tools (tools mentioned or compared to in the paper):
[[drat-trim]], [[LRAT]]

#### Meta
:: SAT
:: PV1 :: checks correctness of SAT solver certificates