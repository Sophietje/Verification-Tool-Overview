#### Name:
fault

#### Application domain/field:
Hardware verification
Computer-aided design

#### Type of tool (e.g. model checker, test generator):
Test generator framework

#### Expected input thing:
The user should construct a Tester object with a [[magma]] circuit. The user should then record a sequence of test actions using the Tester's API class.

#### Expected input format:
Python code

#### Expected output:
Whether the tests pass or fail

#### Internals (tools used, frameworks, techniques, paradigms, ...):
fault is an embedded domain-specific language that allows the user to *construct test generators*. 
It has been designed to support [[magma]], which is an embedded hardware construction language.
It has several different backend targets including [Verilog](../Formats/Verilog.md), [[SPICE]], [[Verilog-AMS]] for simulation and [CoSA](CoSA.md) for model checking.

#### Comments:

#### URIs (github, websites, etc.):
Repository: 
https://github.com/leonardt/fault

#### Last commit date:
16 April 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_19

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Hardware