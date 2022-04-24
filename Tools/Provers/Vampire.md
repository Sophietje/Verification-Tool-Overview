First-order theorem prover

#### Name:
Vampire

#### Application domain/field:
Theorem proving
First-order logic

#### Type of tool (e.g. model checker, test generator):
Automatic theorem prover

#### Expected input thing:
- First-order logic theorem
- *Optional:* Memory-limit and/or time-limit

#### Expected input format:
- *First-order logic theorem*: [[TPTP]] syntax (`.tptp` file)
- *Memory/time-limit*: parameter when calling Vampire

#### Expected output:
Reason for termination (refutation was found, time/memory limit was reached, satisfiability detected, ...)
It also prints some statistics about the proof attempt.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Vampire uses proof by refutation to try and determine whether a conjecture is correct. If Vampire finds a refutation, then it will show the  inference steps that were taken, i.e. it'll show a proof.

Uses [MiniSat](../Solvers/SAT/MiniSat.md), [Z3](../Solvers/SMT/Z3.md).

#### Comments:
License: BSD 3-Clause license

#### URIs (github, websites, etc.):
Project page: https://vprover.github.io/
Project page (old one?): http://www.vprover.org/
Repository: https://github.com/vprover/vampire

#### Last commit date:
18 October 2021

#### Last publication date:
2017

#### List of related papers:
https://doi.org/10.1145/3009837.3009887 (POPL '17)
https://doi.org/10.1007/978-3-642-39799-8_1 (CAV '13)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV6 :: can produce proofs for theorems in first order logic