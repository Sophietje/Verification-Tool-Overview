#### Name:
FACTEST: Fast Controller Synthesis framework

#### Application domain/field:
Non-linear vehicles
Autonomous systems
Controller synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
- Environment, consisting of:
	- Obstacles
	- Borders
	- Initial set
	- Goal set
- Model, consisting of:
	- Dynamics of the vehicle
	- Control law
- Error bounds:
	- Lyapunov function $V(e(t))$ for the tracking error $e$

#### Expected input format:
Python, it expects certain function names, and return values.

#### Expected output:
A reference trajectory and reference input for every partition (or none if it could not be found)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
FACTEST synthesizes a controller for non-linear systems with reach-avoid requirements. 
*Non-linear systems/vehicles* are vehicles such as cards, drones, and underwater vehicles.
The *reach-avoid requirement* states that a certain goal set should be reached while avoiding any obstacles in the trajectory.

Uses [[Pypoman]], [Yices](../Solvers/SMT/Yices.md), [[SciPy]], [[NumPy]]

#### Comments:
Note, the paper that introduced [RealSyn](RealSyn.md) is mentioned as previous work on the project page.

#### URIs (github, websites, etc.):
Project page: https://kmmille.github.io/FACTEST/index.html
Repository: https://github.com/kmmille/FACTEST

#### Last commit date:
1 December 2020

#### Last publication date:
14 July 2020

#### List of related papers:
[Fast and Guaranteed Safe Controller Synthesis for Nonlinear Vehicle Models](https://doi.org/10.1007/978-3-030-53288-8_31)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Synthesis
:: PV2 :: synthesises a controller for non-linear systems with reach-avoid requirements