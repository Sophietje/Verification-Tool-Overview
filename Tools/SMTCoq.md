Plug-in for the integration of external solvers into the Coq proof assistant

#### Name:
SMTCoq

#### Application domain/field:
Proof assistants
SMT solvers
SAT solvers
Proof certificates

#### Type of tool (e.g. model checker, test generator):
Metatool

#### Internals (tools used, frameworks, techniques, paradigms, ...):
SMTCoq is a plugin for the [Coq](Provers/Coq.md) proof assistant. It allows users to use external solvers ([[SAT]] or [[SMT]]) inside Coq. If these solvers succeed in proving a goal and return a proof witness or certificate, SMTCoq can use this to reconstruct a proof of the goal within Coq automatically.

Uses [CVC4](Solvers/SMT/CVC4.md), [zChaff](Solvers/SAT/zChaff.md), [veriT](Solvers/SMT/veriT.md).

SMTCoq is also available as an opam package.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://smtcoq.github.io/
Repository: https://github.com/smtcoq/smtcoq

#### Last commit date:
17 Oct 2022 (default branch)
28 Nov 2022 (last activity)

#### Last publication date:
13 July 2017

#### List of related papers:
[SMTCoq: A Plug-In for Integrating SMT Solvers into Coq](https://doi.org/10.1007/978-3-319-63390-9_7) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: imports other solvers' proof witnesses and certificates to Coq
:: Source :: https://doi.org/10.1145/3550355.3552426
