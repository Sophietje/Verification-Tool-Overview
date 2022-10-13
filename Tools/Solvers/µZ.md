#### Name:
µZ

#### Application domain/field:
Fixed points
Constraints
SMT solving

#### Type of tool (e.g. model checker, test generator):
Fixed point engine/calculator

#### Expected input thing:
- Set of relations
- Rules (Horn clauses)
- Ground facts (unit clauses)

#### Expected input format:
One of the following:
- [SMT-LIB](SMT-LIB.md) 2 format, extended with commands `rule` and `query` to add rules and start the fix-point search
- Bddbddb format
- Tuple format

#### Expected output:
It computes fixed points with constraints.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
Part of [Z3](SMT/Z3.md)

#### URIs (github, websites, etc.):
Repository of [Z3](SMT/Z3.md) (µZ is part of this tool): https://github.com/Z3Prover/z3

#### Last commit date:
30 Sep 2022

#### Last publication date:
2011

#### List of related papers:
https://doi.org/10.1007/978-3-642-22110-1_36 (CAV' 11)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: computes fixed points of a set of constraints