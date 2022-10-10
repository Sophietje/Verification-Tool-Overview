A System for Sequential Synthesis and Verification

#### Name:
ABC

#### Application domain/field:
Sequential logic circuits
Hardware design
And-Inverter Graphs (AIGs)
Sequential synthesis
Combinational synthesis
Binary logic circuits
Model checking
Equivalence checking

#### Type of tool (e.g. model checker, test generator):
Framework for synthesis and verification of boolean networks

#### Expected input thing:
Binary logic circuit/network

#### Expected input format:
- binary BLIF
- binary PLA
- BENCH format
- subset of EDIF
- subet of Synopsys equation format
- subset of structural Verilog

#### Expected output:
The output can be given in many different formats:
- binary BLIF
- binary PLA
- BENCH format
- Synopsys equation format
- CNF
- DOT format
- GML format

#### Internals (tools used, frameworks, techniques, paradigms, ...):
ABC implements several different techniques including:
- Equivalence checking: Can be used to check if the design after synthesis is equal to the initial design.
- Model checking: Can be used to check safety properties
- Logic synthesis: transforms a Boolean network to satisfy some criteria, e.g. reduce the number of nodes.

All of this is applied to boolean networks, i.e. directed acyclic graphs (DAGs).

#### URIs (github, websites, etc.):
https://people.eecs.berkeley.edu/~alanmi/abc/
https://github.com/berkeley-abc/abc

#### Last commit date:
23 January 2022

#### List of related papers:
[ABC: An Academic Industrial-Strength Verification Tool](https://doi.org/10.1007/978-3-642-14295-6_5) (CAV '10)

#### Related tools (tools mentioned or compared to in the paper):
[[SIS]]

#### Meta
:: Framework
:: PV5           :: versatile verification and synthesis arsenal
:: Synthesis
:: Model checking