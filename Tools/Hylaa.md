A tool for computing simulation-equivalent reachability for linear systems

#### Name:
HyLAA: Hybrid Linear Automata Analyzer

#### Application domain/field:
Hybrid automata
Cyber-physical systems (CPS)
Simulation-equivalent reachability
Simulations

#### Type of tool (e.g. model checker, test generator):
Reachability detector

#### Expected input thing:
- Hybrid automaton $H$
- Initial set $\Theta$
- Time bound $K \cdot h$
- Unsafe locations $U$

#### Expected input format:
Defined in Python

#### Expected output:
- Set of reachable states
- Hylaa can produce static visualisations of the reachable set and live animations during the computation.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [GLPK](Libraries/GLPK.md)

#### Comments:
License: GPL v3

#### URIs (github, websites, etc.):
Repository: https://github.com/stanleybak/hylaa
Project page: http://stanleybak.com/hylaa

#### Last commit date:
21 Mar 2023 (last activity)

#### Last publication date:
13 July 2017

#### List of related papers:
[Simulation-Equivalent Reachability of Large Linear Systems with Inputs](https://doi.org/10.1007/978-3-319-63387-9_20) (CAV '17)
[HyLAA](https://doi.org/10.1145/3049797.3049808) (HSCC '17)
[Rigorous Simulation-Based Analysis of Linear Hybrid Systems](https://doi.org/10.1007/978-3-662-54577-5_32) (TACAS '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Automaton
:: PV1 :: computes a set of safe reachable states for a given hybrid automaton
:: Source :: https://doi.org/10.1007/978-3-319-63387-9 :: https://doi.org/10.1145/3550355.3552426
