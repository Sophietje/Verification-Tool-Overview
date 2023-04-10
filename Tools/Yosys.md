Framework for (Verilog) RTL synthesis tools.

#### Name:
yosys - Yosys Open SYnthesis Suite

#### Application domain/field:
RTL synthesis
Verilog
Circuit architecture design

#### Type of tool (e.g. model checker, test generator):
Synthesis framework

#### Expected input thing:
- Design
- Synthesis script

#### Expected input format:
- *Design*: [Verilog](../Formats/Verilog.md)
- *Synthesis script*:  ?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
yosys supports several types of analyses, including:
- Converting Verilog to BLIF/EDIF/BTOR/SMT-LIB/etc.
- Synthesis algorithms for various application designs
- Mapping to ASIC standard cell libraries

#### Comments:
License: ISC

#### URIs (github, websites, etc.):
Repository: https://github.com/YosysHQ/yosys
Project page: https://yosyshq.net/yosys/

#### Last commit date:
10 Apr 2023 (last activity)

#### Last publication date:
2019

#### List of related papers:
[Yosys+nextpnr: An Open Source Framework from Verilog to Bitstream for Commercial FPGAs](https://doi.org/10.1109/FCCM.2019.00010) (FCCM '19)
[Methodology and Example-Driven Interconnect Synthesis for Designing Heterogeneous Coarse-Grain Reconfigurable Architectures](https://doi.org/10.1007/978-3-319-01418-0_12) (Models, Methods, and Tools for Complex Chip Design '13)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Synthesis
:: Framework
:: PV2 :: converts from Verilog to various formats and connects to other libraries
:: Source :: https://doi.org/10.1145/3550355.3552426
