EBMC is a Model Checker for hardware designs. It includes both bounded and unbounded analysis, i.e., it can both discover bugs and is also able to prove the absence of bugs.

#### Name:
EBMC

#### Application domain/field:
Model checking
Hardware design

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Synthesizable hardware design at register transfer level (RTL)
- Safety or liveness property

#### Expected input format:
- *Hardware design*: [[../../Formats/Verilog]], Netlists (ISCA89 format), System Verilog or SMV file
	- https://www.cprover.org/ebmc/manual/verilog_language_features/ describes the synthesizable subset of Verilog
- *Property*: SystemVerilog assertions or LTL

#### Expected output:
Per failure it will report whether it could prove it (`SUCCESS`) or not (`FAILURE`).
When EBMC refutres a property, it will compute a counterexample (path from initial state to an error state).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
EBMC supports bounded and unbounded analysis. It uses k-induction, bounded model checking (BMC) and a BDD engine.
The BDD engine and k-induction are used for unbounded safety verification. BMC is used to check liveness properties.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://www.cprover.org/ebmc/

#### Last commit date:
2017 (last release)

#### Last publication date:
2008

#### List of related papers:
https://doi.org/10.1007/978-3-540-78163-9_10 (VMCAI '08)
https://doi.org/10.1016/j.entcs.2005.07.021 (Electronic Notes in Theoretical Computer Science '06)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Hardware
:: LTL           :: also can work with SystemVerilog assertions
:: PV2           :: checks assertions/properties against a Verilog/Netlists/… spec