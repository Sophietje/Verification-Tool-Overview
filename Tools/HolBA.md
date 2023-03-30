Framework/set of tools for binary analysis in HOL.

#### Name:
HolBA

#### Application domain/field:
Binary analysis
Binary code
Machine checkable proofs
Binary Intermediate Representation (BIR)

#### Type of tool (e.g. model checker, test generator):
Binary analysis framework

#### Expected input thing:
Depends on the subtool that is used.

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Tool for binary analysis in [HOL](Provers/HOL.md)4.

It has the following tools:
- backlifter: gets ISA-level contracts from BIR contracts
- cfg: Control Flow Graph utilities
- comp: Composition of contracts
- exec: Concrete execution
- lifter: Transpiler from binary to BIR
- pass: Passification utility
- scamv: Abstract side channel model validation framework
- wp: Weakest precondition propagation

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/kth-step/HolBA

#### Last commit date:
29 Mar 2023 (last activity)

#### Last publication date:
8 September 2020

#### List of related papers:
[TrABin: Trustworthy analyses of binaries](https://doi.org/10.1016/j.scico.2019.01.001) (SCP 2019)

#### Related tools (tools mentioned or compared to in the paper):
[Scam-V](Scam-V.md)
[[Valgrind]]

#### Meta
:: Binary level
:: PV5 :: library for semi-automatic analysis of binary code
:: Framework
:: Source :: https://doi.org/10.1145/3550355.3552426
