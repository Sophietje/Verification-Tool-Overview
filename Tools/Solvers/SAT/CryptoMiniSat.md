SAT solver optimized for cryptographic problems

#### Name:
CryptoMiniSat

#### Application domain/field:
SAT solving
Cryptography

#### Type of tool (e.g. model checker, test generator):
SAT solver

#### Expected input thing:
Boolean formula in conjunctive normal form (CNF)

#### Expected input format:
[DIMACS](../../../Formats/DIMACS.md) format with the extension of XOR clauses.

#### Expected output:
`SATISFIABLE`, `UNSATISFIABLE` or `UNKNOWN`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
They extended the solver's input language with the XOR operation which is often used in cryptographic 

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www.msoos.org/cryptominisat5/
Repository: https://github.com/msoos/cryptominisat/

#### Last commit date:
29 Mar 2023 (last activity)

#### Last publication date:
2009

#### List of related papers:
[Extending SAT Solvers to Cryptographic Problems](https://doi.org/10.1007/978-3-642-02777-2_24) (SAT '09)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: SAT
:: PV4 :: produces a satisfiability result for a formula in CNF
