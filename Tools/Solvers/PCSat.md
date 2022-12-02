Satisfiability checking tool for pfwCSP based on stratified Counterexample-guided Inductive Synthesis (CEGIS).

#### Name:
PCSat

#### Application domain/field:
Constrained Horn Clauses (CHCs)
Constraint-based verification
Counterexample-guided Inductive Synthesis (CEGIS)
Satisfiability checking
Relational verification

#### Type of tool (e.g. model checker, test generator):
Satisfiability checker (for pfwCSP)

#### Expected input thing:
- pfwCSP problem
- Configuration file for the solver
- Solver to use

#### Expected input format:
- `.clp` or `.smt2` file which describes the pfwCSP
- `.json` file for configuration of the solver
- "pcsp": textual argument that is given to indicate the solver that should be used

#### Expected output:
`sat`, `unsat` or `unknown`?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Z3.md)

**pfwCSP**: new class of predicate Constraint Satisfaction Problems. This allows constraints that are arbitrary (i.e. possibly non-Horn) clauses modulo first-order theories over predicate variables that can be functional predicates, well-founded predicates or ordinary predicates. This is a generalization over Constrained Horn Clauses.

#### Comments:
Note: the authors sometimes call PCSat a (second-order) constraint solver

#### URIs (github, websites, etc.):
Repository (contains [MuVal](../MuVal.md) and PCSat): https://github.com/hiroshi-unno/coar

#### Last commit date:
11 May 2021 (default branch)
11 May 2021 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[Constraint-Based Relational Verification](https://doi.org/10.1007/978-3-030-81685-8_35) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: CHC
:: PV2 :: generates an SMT problem from a pfwCSP spec, requires an external solver
:: Source :: https://doi.org/10.1145/3550355.3552426
