Framework for verifying hybrid control systems that are described by a combination of a black-box simulator for trajectories and a white-box transition graph specifying mode switches.

#### Name:
DryVR

#### Application domain/field:
Cyber-physical system
Autonomous systems
Reachability analysis
Gray-box systems
Hybrid control systems

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Transition graph
- Initial set
- Set of unsafe states

#### Expected input format:
JSON file (this used to be a text file in the earlier versions of DryVR)

#### Expected output:
`Safe` or `Unsafe`?
Any reachtubes or counterexamples are also stored in text files.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This framework includes:
- A probabilistic algorithm for learning sensitivity of the continuous trajectories from simulation data
- Bounded reachability analysis that uses the learned sensitivity
- Reasoning techniques for verification of complex systems under long switching sequences, from the reachability analysis of a simpler system under short sequences.

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Documentation: https://dryvr.readthedocs.io/en/latest/index.html
Repository: https://github.com/qibolun/DryVR (last commit: 14 February 2018)
Successor/version 2.0 of DryVR: https://github.com/qibolun/DryVR_0.2 (last commit: 1 May 2018)
Successor of version 2.0 of DryVR: https://gitlab.engr.illinois.edu/dryvrgroup/dryvrtool

#### Last commit date:
1 October 2021

#### Last publication date:
13 July 2017

#### List of related papers:
[DryVR: Data-Driven Verification and Compositional Reasoning for Automotive Systems](https://doi.org/10.1007/978-3-319-63387-9_22) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Automaton
:: PV4 :: produces a satisfiability/reachability result for a hybrid control system
:: Source :: https://doi.org/10.1145/3550355.3552426