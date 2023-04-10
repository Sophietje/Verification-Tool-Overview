#### Name:
LEGION

#### Application domain/field:
Model checking
Bounded model checking
Sequential programs
Termination

#### Type of tool (e.g. model checker, test generator):
Bounded model checker

#### Expected input thing:
Program (with an entry-point procedure called `main`)
Property? (unclear, possibly assertions in the program)

#### Expected input format:
[Boogie](../../Tools/Frameworks/Boogie.md) program

#### Expected output:
Whether the program is safe, unsafe (with counterexample trace) or undecided

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The verification question that they focus on is whether there exists a terminating execution of P. In other words, whether there is any execution of `main` that reaches its return statement. If no such execution exists, then the program is considered safe. 
They require the program to not contain any loops or recursive procedure calls. Such calls must be unrolled to a pre-determined depth before starting verification.

Uses [Z3](../../Tools/Solvers/SMT/Z3.md) to solve SMT queries.

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/boogie-org/corral (branch:legion).

#### Last commit date:
6 May 2022 (branch: legion)
10 Apr 2023 (last activity)

#### Last publication date:
7 August 2022

#### List of related papers:
[Proof-Guided Underapproximation Widening for Bounded Model Checking](https://doi.org/10.1007/978-3-031-13185-1_15) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '22 paper: [[CORRAL]]

#### Meta
:: Model checking
:: Source :: https://doi.org/10.1007/978-3-031-13185-1
