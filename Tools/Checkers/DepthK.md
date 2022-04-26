DepthK is a software verification tool that employs a proof by induction algorithm that combines k-induction with invariant inference

#### Name:
DepthK

#### Application domain/field:
Software verification
Bounded model checking
Model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- C program
- Safety property

#### Expected input format:
- *C program*: `.i` file
- *Safety property*: `.prp` file

#### Expected output:
`TRUE` and a witness if there is no path that violates the safety property, `FALSE` and a witness if there exists a path that violates the safety property or `UNKNOWN` otherwise.
The witness is stored as a `.graphml` file.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses bounded model checking (BMC) or k-induction, combined with invariant inference and witness checking.

Extends [ESBMC](../ESBMC.md) to falsify or prove correctness of a given (safety) property for any depth without manual annotation of loops with invariants.
Uses [CPAchecker](CPAchecker.md), [Ultimate Automizer](../Ultimate%20Automizer.md), [[PAGAI]], [[PIPS]]

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/hbgit/depthk/

#### Last commit date:
9 January 2019

#### Last publication date:
31 March 2017

#### List of related papers:
https://doi.org/10.1007/978-3-662-54580-5_23 (TACAS '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C
:: PV4 :: checks safety properties for a C program
:: Model checking