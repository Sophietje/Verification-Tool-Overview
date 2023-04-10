SMT-based bounded model checker that provides bit-precise verification for C/C++ programs

#### Name:
ESBMC

#### Application domain/field:
SMT-based model checking
Bounded model checking
Multi-threaded programs

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- C program
- Possibly a property file or assertions in the code to express properties that should be checked
- Parameters to indicate the type of analysis that should be done

#### Expected input format:
`. c` file and parameters when calling ESBMC.
The property file should be in the format used by SV-COMP.

#### Expected output:
`VERIFICATION SUCCESSFUL` or `VERIFICATION FAILED`, followed by more detail about the counterexample that the tool found.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
ESBMC v6.0 employs a k-induction algorithm to both falsify and prove safety properties in C programs

Some of the parameters/analyses that ESBMC supports are:
- `--k-induction` to enable k-induction
- `--floatbv` to enable floating-point SMT encoding
- `--interval-analysis`, which enables invariant generation
- `--memory-leak-check` for memory verification
- `--overflow-check` to check for overflows

As back-ends ESBMC supports the following SMT solvers: [Boolector](Solvers/SMT/Boolector.md), [Z3](Solvers/SMT/Z3.md), [Yices](Solvers/SMT/Yices.md), [MathSAT](Solvers/SMT/MathSAT.md), [CVC4](Solvers/SMT/CVC4.md).

ESBMC is based on [CBMC](Checkers/CBMC.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/esbmc/esbmc
Project page: http://esbmc.org/

#### Last commit date:
08 Apr 2023 (last activity)

#### Last publication date:
8 September 2021

#### List of related papers:
[Model checking C++ programs](https://doi.org/10.1002/stvr.1793) (Software Testing, Verification and Reliability, Vol. 32, Issue 1, '21)
[ESBMC 6.1: automated test case generation using bounded model checking](https://doi.org/10.1007/s10009-020-00571-2) (Journal on STTT '20)
[ESBMC v6.0: Verifying C Programs Using k-Induction and Invariant Inference](https://doi.org/10.1007/978-3-030-17502-3_15) (TACAS '19)
[ESBMC 5.0: an industrial-strength C model checker](https://doi.org/10.1145/3238147.3240481) (ASE '18)
[ESBMC 1.22](https://doi.org/10.1007/978-3-642-54862-8_31) (TACAS '14)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C
:: C++
:: Model checking
:: PV4 :: checks safety properties in C programs, can generate invariants
:: Source :: https://doi.org/10.1145/3550355.3552426
