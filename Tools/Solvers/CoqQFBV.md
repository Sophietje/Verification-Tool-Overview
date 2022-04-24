SMT solver for `QF_BV` (quantifier-free bit-vector) logic.

#### Name:
CoqQFBV

#### Application domain/field:
SMT solving
Quantifier-Free Bit-Vector (`QF_BV`) logic

#### Type of tool (e.g. model checker, test generator):
SMT solver for `QF_BV` logic

#### Expected input thing:
SMT `QF_BV` query

#### Expected input format:
[SMT-LIB](../../Formats/SMT-LIB.md) v2

#### Expected output:
Boolean formula such that the query is satisfiable if and only if the Boolean formula is satisfiable.
Output is generated in the [DIMACS](../../Formats/DIMACS.md) format.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This is a certified SMT solver for quantifier-free bit-vector (`QF_BV`) formulas. It has been specified and verified in the proof assistant [Coq](../Provers/Coq.md).

It takes a `QF_BV` query in [SMT-LIB](../../Formats/SMT-LIB.md) format. This is converted into a formal `QF_BV` expression. Then a CNF formula is constructed. Then it uses [Kissat](SAT/Kissat.md) to solve the CNF formula. If the result is unsat with a certificate, then the certificate is verified with [GRAT](../GRAT.md). If the results is sat with assignments, then this is translated back to SMT assignments and the tool will verify whether these assignments satisfy the `QF_BV` expression.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/fmlab-iis/coq-qfbv

#### Last commit date:
9 September 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_7 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
[Boolector](SMT/Boolector.md), [[Bitwuzla]], [CVC4](SMT/CVC4.md)

#### Meta
:: SMT
:: PV2 :: produces a satisfiability formula for a query