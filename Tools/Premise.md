#### Name:
Premise: Predictive Monitoring with Imprecise Sensors

#### Application domain/field:
Monitoring
Cyber-physical systems
Markov decision process (MDP)
Probabilistic model checking
Runtime verification
Runtime monitoring

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Markov Devision Process (MDP)
- State risk, e.g. the probability that the plane will crash into a vehicle within a given number of steps.

#### Expected input format:
- *Markov Decision Process*: `.nm` file, extended dialect of the [PRISM](Checkers/PRISM.md) language
- *State risk*: PCTL (probabilistic CTL) formula, passed as an argument when calling Premise

#### Expected output:
- File with some model-related statistics
- `.csv` file for each trace, containing the calculated risk for that trace.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Premise is built on top of [Storm](Checkers/Storm.md).
Uses [Z3](Solvers/SMT/Z3.md).

By default Premise will simulate 50 traces of 500 steps each. It is possible to simulate more/less traces of a different length by passing additional options when calling Premise.

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/monitoring-MDPs/premise
Artifact for CAV '21 paper: https://doi.org/10.5281/zenodo.4724623

#### Last commit date:
28 April 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[Runtime Monitors for Markov Decision Processes](https://doi.org/10.1007/978-3-030-81688-9_26) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Probabilistic
:: Monitoring
:: PV3 :: computes the probability of a user-specified risk in a Markov decision process
:: Source :: https://doi.org/10.1145/3550355.3552426