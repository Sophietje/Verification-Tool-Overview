#### Name:
ADAC

#### Application domain/field:
Approximate computing (field aiming at reducing system resource demands, e.g. power demands)
Circuit synthesis
Circuit verification

#### Type of tool (e.g. model checker, test generator):
Framework to design approximate arithmetic circuits

#### URIs (github, websites, etc.):
https://github.com/imatyas/ADAC

#### Expected input:
- A golden combinational circuit in Verilog implementing the correct functionality
- Error metric (e.g. mean error, Hamming distance, etc.)
- Threshold on the error metric representing the maximal permissible error
- Time limit on the overall design process
- File specifying sizes of gates available to the design process

#### Expected output:
Approximate circuit satisfying the error threshold and with minimal estimated chip area

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Implemented as a module of [[ABC]].
Uses [[Yosys]], [[iprove]], [[MiniSat]].

#### Last publication date:
15 April 2020

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_35
https://doi.org/10.1007/978-3-030-45093-9_58

