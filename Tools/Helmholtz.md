Verifier for smart contracts written in the Michelson language for the Tezos blockchain.

#### Name:
Helmholtz

#### Application domain/field:
Smart contracts
Blockchain
Cryptocurrency
Static verification
Refinement types

#### Type of tool (e.g. model checker, test generator): 
Static verifier, auto-active verifier?

#### Expected input thing:
Michelson program annotated with a user-defined specification.
The user-defined specification should be expressed in a refinement type. The user may also need to provide additional annotations such as loop invariants.

#### Expected input format:
Michelson (language)

#### Expected output:
`VERIFIED` if the program satisfies the specification. Otherwise, `UNVERIFIED`.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Z3](Solvers/SMT/Z3.md) to discharge generated verification conditions.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www.fos.kuis.kyoto-u.ac.jp/projects/Helmholtz/
Try online: https://www.fos.kuis.kyoto-u.ac.jp/trylang/Helmholtz
Repository (Helmholtz is part of the repository for Octez): https://gitlab.com/aigarashi/ReFX

#### Last commit date:
20 October 2021

#### Last publication date:
23 March 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-72013-1_14 (TACAS '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Smart contract
:: PV3 :: verifies properties from program annotations