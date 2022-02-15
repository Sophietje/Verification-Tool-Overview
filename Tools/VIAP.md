an automated system for verifying safety properties of procedural programs with integer assignments and loops

#### Name:
VIAP (Verifier for Integer Assignment Programs)

#### Application domain/field:
Recurrence solving
Safety verification

#### Type of tool (e.g. model checker, test generator):
Monoverifier

#### Expected input thing:
C program with user-provided assertions

#### Expected input format:
C99

#### Expected output:
TRUE (safe) / FALSE (counterexample produced) / UNKNOWN (otherwise)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
C is translated to a set of first order axioms
[[SymPy]] is used as an algebraic simplifier
[Z3](Solvers/SMT/Z3.md) as a theorem prover tries to prove postconditions

#### Comments:
-

#### URIs (github, websites, etc.):
SV-Comp: https://gitlab.com/sosy-lab/sv-comp/archives/-/blob/master/2018/viap.zip
GitHub: https://github.com/VerifierIntegerAssignment/VIAP_ARRAY

#### Last commit date:
6 Apr 2019

#### Last publication date:
4 Apr 2019

#### List of related papers:
https://doi.org/10.1109/SYNASC.2017.00032 (SYNASC'17)
https://doi.org/10.1007/978-3-030-03592-1_3 (VSSTE'18)
https://doi.org/10.1007/978-3-030-17502-3_23 (TACAS'19)

#### Related tools (tools mentioned or compared to in the paper):