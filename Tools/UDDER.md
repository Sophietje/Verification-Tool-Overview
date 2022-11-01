Reduces the unbounded verification problem of Delay Differential Equations (DDEs) to a bounded problem.

#### Name:
UDDER

#### Application domain/field:
Delay Differential Equations (DDEs)
Dynamical systems
Safety verification

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
They focus on verifying safety properties of delayed dynamical systems encoded by Delay Differential Equations (DDEs), where safety properties pertain to an infinite domain.
They present a quantitative method to construct estimations. This reduces the temporally unbounded verification problem to a bounded one.

Implemented in [Wolfram Mathematica](https://www.wolfram.com/mathematica/). Uses [DDE-BIFTOOL](Not-verifiers/DDE-BIFTOOL.md).

#### Comments:
It is called a "prototypical implementation" in the CAV '19 paper.

#### URIs (github, websites, etc.):
Download page: http://lcs.ios.ac.cn/~chenms/tools/

#### Last commit date:
12 May 2019

#### Last publication date:
12 July 2019

#### List of related papers:
[Taming Delays in Dynamical Systems](https://doi.org/10.1007/978-3-030-25540-4_37) (CAV 2019)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV2 :: generates a bounded version of the given unbounded verification problem