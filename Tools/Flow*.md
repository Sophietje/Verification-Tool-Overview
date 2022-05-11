#### Name:
Flow*

#### Application domain/field:
Hybrid systems
Non-linear hybrid systems
Safety verification
Reachability analysis

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Hybrid system model file which describes the modes, the polynomial dynamics associated with each mode and the transitions between modes
- A specification file includes Taylor Model flowpipes with the state space and unsafe set specifications

#### Expected input format:
?

#### Expected output:
Flow* computes an over-approximation of the reachable states and checks whether this intersects with the unsafe set.
It will output a visualization of the set of reachable states using polyhedral over-approximations of the computed Taylor Model flowpipes.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
License: GNU General Public License

#### URIs (github, websites, etc.):
Project page: https://flowstar.org/
Download page: https://flowstar.org/dowloads/

#### Last commit date:
(Last release: March 2017)

#### Last publication date:
2014

#### List of related papers:
https://doi.org/10.1109/FMCAD.2014.6987596 (FMCAD '14)
https://doi.org/10.29007/1w4t (ARCH 14-15)
https://doi.org/10.1007/978-3-642-39799-8_18 (CAV '13)

#### Related tools (tools mentioned or compared to in the paper):
Other tools for linear hybrid systems analysis: [[HyTech]], [[Checkmate]], [[d/dt]], [[Ariadne]], [[HySAT/iSAT]], [[RealPaver]], [[PHAVer]], [[SpaceEx]].
Other non-linear analysis tools: [[KeYmaera]], [[Ariadne]], [[HySAT/iSAT]].
[[VNODE-LP]]

#### Meta
:: Taylor models
:: PV2 :: generates flowpipes for non-linear hybrid systems