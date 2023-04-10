#### Name:
JKind

#### Application domain/field:
Model checker
Synchronous systems

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Model
- Properties to be checked

#### Expected input format:
.lus file ([[Lustre]] language)

#### Expected output:
A list of valid properties and invalid properties, including the time it took to verify/falsify each property. 

#### Internals (tools used, frameworks, techniques, paradigms, ...):
SMT-based infinite-state model checker for safety properties.
Models and properties are specified in [[Lustre]].

The JKind architecture consists of 5 separate 'engines':
1. Bounded Model Checking (BMC) engine for standard iterative unrolling to find counterexamples.
2. k-Induction engine to perform the inductive step of k-induction
3. Invariant generation engine that generates invariants based on templates.
4. Property Directed Reachability (PDR) engine to do property directed reachability.
5. Advice engine to generate invariants based on previous JKind runs.

Uses [SMTInterpol](../Solvers/SMT/SMTInterpol.md) as an SMT-solver to prove/falsify properties.

#### Comments:
There exists an Eclipse plug-in with syntax highlighting and static analysis for Lustre code which also runs JKind and reports the results graphically.

#### URIs (github, websites, etc.):
Repository: https://github.com/loonwerks/jkind
Project page: https://loonwerks.com/tools/jkind.html

#### Last commit date:
30 Sep 2022 (last activity)

#### Last publication date:
18 July 2018

#### List of related papers:
[The JKind Model Checker](https://doi.org/10.1007/978-3-319-96142-2_3)

#### Related tools (tools mentioned or compared to in the paper):
Compared to [[Kind 2]], [[Zustre]], [Z3](../Solvers/SMT/Z3.md) (generalized PDR) and [nuXmv](nuXmv.md) (IC3) in the paper.

It is used as a back-end in [[../Provers/SPEAR]], [AGREE](AGREE.md) and [[SIMPAL]].

#### Meta
:: Lustre
:: PV4 :: infers invariants and checks user-specified properties for a Lustre system
:: Source :: https://doi.org/10.1145/3550355.3552426
