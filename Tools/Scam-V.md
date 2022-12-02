A framework for the automatic validation of abstract observational models.

#### Name:
Scam-V: Side Channel Abstract Model Validator

#### Application domain/field:
Information flow analysis
Side channel attacks
Security verification

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
Program?

#### Expected input format:
HOL?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It has been implemented in the [HOL](Provers/HOL.md)4 theorem prover. It is embedded in [HolBA](HolBA.md).
Scam-V attempts to construct pairs of initial states such that runs of the binary from these states are indistinguishable at the level of the hardware, but distinguishable on the real hardware.

According to the repository, Scam-V:
- Works for small programs
- Cannot handle certain cases such as memory dependent observations

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/kth-step/HolBA
Tutorial: https://github.com/kth-step/HolBA/wiki/HolBA-SCAM-V-tutorial

#### Last commit date:
29 Sep 2022 (default branch)
01 Dec 2022 (last activity)

#### Last publication date:
14 July 2020

#### List of related papers:
[Validation of Abstract Side-Channel Models for Computer Architectures](https://doi.org/10.1007/978-3-030-53288-8_12)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Binary level
:: PV4 :: randomly generates observationally equivalent inputs and checks their equivalence
:: Source :: https://doi.org/10.1145/3550355.3552426
