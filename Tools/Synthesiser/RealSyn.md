Synthesis tool for controllers with reach-avoid specifications.

#### Name:
RealSyn

#### Application domain/field:
Controller synthesis
Linear systems
Reach-avoid specifications
Vehicle path planning
Circuit design

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
- System A
- Time bound T
- Set of obstacles O
- Goal G that should be reached
- Q and R: Used for linear quadratic regulator (LQR), they are set to the identity matrices for most examples

#### Expected input format:
?

#### Expected output:
Set of controllers that meet the specification (reach G while avoiding O)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Controller synthesis is asks whether we can generate an input for a given system (or plant) so that it achieves a specification. This is interesting for applications such as vehicle path planning, motion control, and circuit design.
RealSyn synthesizes provably correct controllers for linear systems with reach-avoid specifications.

*Reach-avoid specifications*: Specifications that require the system to reach a goal G while avoiding unsafe states or obstacles O.

Uses [Z3](../Solvers/SMT/Z3.md), [CVC4](../Solvers/SMT/CVC4.md), [Yices](../Solvers/SMT/Yices.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/umangm/realsyn

#### Last commit date:
28 June 2018

#### Last publication date:
18 July 2018

#### List of related papers:
[Controller Synthesis Made Real: Reach-Avoid Specifications and Linear Dynamics](https://doi.org/10.1007/978-3-319-96145-3_19) (CAV 2018)

#### Related tools (tools mentioned or compared to in the paper):
Other controller synthesis algorithms: [[CoSyMa]], [[Pessoa]], [[LTLMop]], [[Tulip]], [[SCOTS]]

#### Meta
:: Synthesis
:: PV2 :: synthesises a set of controllers that meet the reach-avoid specification