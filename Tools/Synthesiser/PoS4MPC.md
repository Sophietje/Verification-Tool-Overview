#### Name:
PoS4MPC: Policy Synthesis for MPC

#### Application domain/field:
Synthesis
Security policy
Symbolic execution

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
- MPC (multi-party computation) program

#### Expected input format:
C program

#### Expected output:
Computes a security policy for the given program such that the number of secret variables that are declared is as low as possible.
The program is transformed into Obliv-C such that it can be compiled into executable implementations.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [KLEE](../../Tools/KLEE.md) as symbolic execution engine.

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/SPoS4/PoS4MPC

#### Last commit date:
20 January 2022
20 Jan 2022 (last activity)

#### Last publication date:
7 August 2022

#### List of related papers:
[Computer Aided Verification](https://doi.org/10.1007/978-3-031-13185-1) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Security
:: C
:: Synthesis
:: PV2 :: synthesises security policy for secure multi-party computation
:: Source :: https://doi.org/10.1007/978-3-031-13185-1
