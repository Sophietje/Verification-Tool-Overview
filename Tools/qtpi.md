Quantum protocol programming language & simulator

#### Name:
qtpi, sometimes stylized as Qtpi

#### Application domain/field:
Quantum cryptographic protocols
Concurrent quantum systems
Quantum communication
Process-calculus

#### Type of tool (e.g. model checker, test generator):
Framework?
Programming language and simulator/interpreter

#### Expected input thing:
Quantum protocol and simulation settings (e.g. length of messages, length of hash key, minimum number of checkbits, number of sigmas, number of trials)

#### Expected input format:
Own `.qtp` format

#### Expected output:
Statistics about the simulation: number of qubits per trial, number of qubits that were interfered with, number of trials that succeeded.
It is also possible to inspect a sample execution trace.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This tool was inspired by [[CQP]]. 

qtpi takes a single execution path, making probabilistic choices between outcomes.

The programs are statically checked to ensure that they obey real-world restrictions on the use of qubits (no cloning, no sharing).

#### Comments:
License: GPL v2.0

#### URIs (github, websites, etc.):
Repository: https://github.com/mdxtoc/qtpi
TACAS '20 artifact: https://doi.org/10.6084/m9.figshare.11882592

#### Last commit date:
03 Sep 2022

#### Last publication date:
17 April 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-45237-7_16 (TACAS '20)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Simulation
:: Protocol
:: PV1 :: checks that quantum programs obey real-world restrictions and simulates quantum programs