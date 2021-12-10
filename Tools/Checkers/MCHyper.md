Hardware model checker for hyperproperties

#### Name:
MCHyper

#### Application domain/field:
Model checking
Information-flow
Hyperproperties

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Circuit description
- HyperLTL formula

#### Expected input format:
- *Circuit*: [[../../Formats/Verilog]] module or [AIGER](../../Formats/AIGER.md) circuit
- *HyperLTL formula*: [EAHyper](../EAHyper.md) or [MCHyper](MCHyper.md) (own) format

#### Expected output:
It will either report that the property is proven, or it will provide a counterexample. 
You can also inspect the generated circuit. The user can also choose to get more verbose output.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
MCHyper is a model checker for synchronous HyperLTL properties. It can handle up to one quantifier alternation.
HyperLTL allows the user to specify temporal properties that relate multiple computation traces, also called hyperproperties. Therefore, the user can check a.o. information-flow properties and noninterference between two traces.

It uses [ABC](../Frameworks/ABC.md) as the backend for checking the reachability of a violation.
If given a Verilog system as input, it will be converted into an Aiger circuit using [[../Yosys]].

#### Comments:

#### URIs (github, websites, etc.):
Try online: https://www.react.uni-saarland.de/tools/online/MCHyper/
Tutorial: https://www.react.uni-saarland.de/tools/online/MCHyper/help.html
Project page: https://www.react.uni-saarland.de/tools/mchyper/
Repository: https://github.com/reactive-systems/MCHyper

#### Last commit date:
28 May 2021

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25540-4_7

#### Related tools (tools mentioned or compared to in the paper):
