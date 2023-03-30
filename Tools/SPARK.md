Deductive verifier for the Ada language
"consists of a programming language, a verification toolset and a design method"

#### Name:
SPARK

#### Application domain/field:
Deductive verification
Language
Runtime verification
Static verification

#### Type of tool (e.g. model checker, test generator):
Deductive verifier

#### Expected input thing:
Ada program with specifications.
Specifications are written in the form of, e.g. preconditions, postconditions and loop invariants.

#### Expected input format:
SPARK, subset of the Ada language

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The functional specification features in SPARK are executable. So the verification can be done dynamically or statically.

The name SPARK is used for the verifier, but also for the language, which is a subset of Ada.

SPARK uses [[GNATprove]] for the verification.
SPARK uses [Why3](Frameworks/Why3.md) to generate verification conditions. It uses [Alt-Ergo](Solvers/SMT/Alt-Ergo.md), [CVC4](Solvers/SMT/CVC4.md) and/or [Z3](Solvers/SMT/Z3.md) to discharge the verification conditions.

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Project page: https://www.adacore.com/about-spark
User's Guide: https://docs.adacore.com/spark2014-docs/html/ug/#
Repository: https://github.com/AdaCore/spark2014
Tutorial: https://learn.adacore.com/courses/intro-to-spark/index.html

#### Last commit date:
30 Mar 2023 (last activity)

#### Last publication date:
19 December 2020

#### List of related papers:
[Verification of Programs with Pointers in SPARK](https://doi.org/10.1007/978-3-030-63406-3_4) (ICFEM '20)
[Recursive Data Structures in SPARK](https://doi.org/10.1007/978-3-030-53291-8_11) (CAV '20)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
SPARK        :: Ada
:: PV4  :: checks user-specified specifications and absence of runtime errors for Ada programs
:: Source :: https://doi.org/10.1145/3550355.3552426
