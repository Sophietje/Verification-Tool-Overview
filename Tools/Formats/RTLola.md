Stream-based specification language for real-time properties

#### Name:
RTLola

#### Application domain/field:
Unmanned aerial vehicles
Autonomous aircrafts
Monitoring framework
Real-time specifications

#### Type of tool (e.g. model checker, test generator):
Specification language

#### Expected input thing:
-

#### Expected input format:
-

#### Expected output:
-

#### Internals (tools used, frameworks, techniques, paradigms, ...):
RTLola is a stream specification language. In a specification, input streams collect data from networks, sensors, etc.. These streams are filtered and combined into output streams where data from multiple sources and over multiple points are combined. This allows the use of sliding windows of some real-time length over such data to trigger on certain critical situations. Finally, the RTLola specification can be automatically translated into an FPGA-based monitor.

#### Comments:
-

#### URIs (github, websites, etc.):

#### Last commit date:
-

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53291-8_3

#### Related tools (tools mentioned or compared to in the paper):
-