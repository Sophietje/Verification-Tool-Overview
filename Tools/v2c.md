Verilog to C translator

#### Name:
v2c

#### Application domain/field:
Verilog
Hardware circuits
Translation

#### Type of tool (e.g. model checker, test generator):
Translator

#### Expected input thing:
Register Transfer Level (RTL) description of a hardware circuit

#### Expected input format:
[Verilog](../Formats/Verilog.md) Hardware Description Language

#### Expected output:
C program, also called a software netlist.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
By translating a hardware circuit into a C program, allows you to use software verification techniques such as abstract interpretation and symbolic execution.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www.cprover.org/hardware/v2c/

#### Last commit date:
-

#### Last publication date:
9 April 2016

#### List of related papers:
https://doi.org/10.1007/978-3-662-49674-9_38 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
[[HW-CBMC]] for hardware/software co-verification or C-RTL equivalence checking.
[[EBMC]] for bounded model checking of Verilog designs.
[[VerifOx]] for path-based symbolic execution of C programs.

#### Meta
:: Hardware
:: PV2 :: translates a Register Transfer Level hardware circuit description into a C program