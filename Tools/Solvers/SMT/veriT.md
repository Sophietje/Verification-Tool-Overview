SMT solver

#### Name:
veriT

#### Application domain/field:
Satisfiability Modulo Theories (SMT)
Proof-producing
SMT solving

#### Type of tool (e.g. model checker, test generator):
SMT solver

#### Expected input thing:
SMT problem

#### Expected input format:
[SMT-LIB](../../../Formats/SMT-LIB.md) 2.0 or [DIMACS](../../../Formats/DIMACS.md)

#### Expected output:
`unsat`, `sat` or an error (in case of e.g. a timeout)
veriT can also produces a proof that can be checked with an external tool if the input problem deduced to be unsatisfiable. This proof is presented in veriT's own format.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
veriT is complete for quantifier-free formulas with uninterpreted functions and linear arithmetic on real numbers and integers. It also offers good support for quantifiers.
veriT can produce a proof that can be checked with external tools.

#### Comments:
License: BSD License

#### URIs (github, websites, etc.):
Project page: https://www.verit-solver.org/
Download page: https://www.verit-solver.org/download/
Reference for the veriT proof format: https://www.verit-solver.org/download/tip/proofonomicon.pdf

#### Last commit date:
17 November 2021

#### Last publication date:
4 January 2019

#### List of related papers:
[Scalable Fine-Grained Proofs for Formula Processing](https://doi.org/10.1007/s10817-018-09502-y) (Journal of Automated Reasoning '20)
[Congruence Closure with Free Variables](https://doi.org/10.1007/978-3-662-54580-5_13) (TACAS '17)
[veriT: An Open, Trustable and Efficient SMT-Solver](https://doi.org/10.1007/978-3-642-02959-2_12) (CADE '09)

#### Related tools (tools mentioned or compared to in the paper):
Other solvers: [[CVC3]], [Z3](Z3.md)

#### Meta
:: SMT
:: PV6 :: produces a proof for satisfiability of a formula
