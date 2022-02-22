#### Name:
ADAC

#### Application domain/field:
Approximate computing (field aiming at reducing system resource demands, e.g. power demands)
Circuit synthesis
Circuit verification

#### Type of tool (e.g. model checker, test generator):
Framework to design approximate arithmetic circuits

#### Expected input thing:
- A golden combinational circuit in Verilog implementing the correct functionality
- Error metric (e.g. mean error, Hamming distance, etc.)
- Threshold on the error metric representing the maximal permissible error
- Time limit on the overall design process
- File specifying sizes of gates available to the design process

#### Expected input format:
- Circuit in [Verilog](../Formats/Verilog.md) format
- Error metric, threshold on error metric and time limit seem to be specified in a configuration file (.conf)

#### Expected output:
Approximate circuit satisfying the error threshold and with minimal estimated chip area (in gate-level Verilog format).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Implemented as a module of [ABC](Frameworks/ABC.md).
Uses [[Yosys]], [[iprove]], [MiniSat](Solvers/SAT/MiniSat.md).

#### Comments:

#### URIs (github, websites, etc.):
https://github.com/imatyas/ADAC (this is linked in the paper but it contains very little useful information)

#### Last commit date:
2 February 2018

#### Last publication date:
15 April 2020

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_35
https://doi.org/10.1007/978-3-030-45093-9_58

#### Related tools (tools mentioned or compared to in the paper):
[[SALSA]], [[SASIMI]] are mentioned as general-purpose methods for approximating circuits independently of their structure.

#### Meta
:: Hardware
:: PV1           :: synthesises an approximate circuit from a given one and a set of constraints