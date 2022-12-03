#### Name:
SAW: Safety Analysis of Weakly-hard Systems

#### Application domain/field:
Weakly-hard systems
Safety verification

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
Model file that specifies
- Dynamic system $f$
- Sampling period $\delta$
- Safe state region $X$
- Weakly-hard constraint $(m,K)$
- Control law $\pi$

_Optional_: Configuration file of [[Flow\*]]. This is set by default but can be customized.

#### Expected input format:
?

#### Expected output:
- $X_s$: Safe initial set 
- $\Gamma_S$: Largest set from which the system will not leave the safe region.
- $\Gamma_I$: Largest subset of $\Gamma_S$ that satisfies the inductiveness

#### Internals (tools used, frameworks, techniques, paradigms, ...):
SAW focuses on the analysis of weakly-hard systems. Weakly-hard systems are introduced as systems where deadlines should be met ("hard" systems) though it is allowed to miss an occasional deadline ("weakly").
SAW computes a tight estimation of the safe initial set for infinite-time safety verification of general nonlinear weakly-hard systems.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/551100kk/SAW

#### Last commit date:
29 Jan 2020 (default branch)
29 Jan 2020 (last activity)

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_26

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV2 :: generates several safe regions of weakly hard system
:: Source :: https://doi.org/10.1145/3550355.3552426
