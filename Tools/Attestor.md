#### Name:
Attestor

#### Application domain/field:
Model checking
Pointer programs

#### Type of tool (e.g. model checker, test generator):
Model checker

#### URIs (github, websites, etc.):
https://moves-rwth.github.io/attestor/

#### Expected input:
- Java or Java Bytecode program
- LTL formulae (specifications to be checked)
- Declaration of the graph grammar that guides abstraction
- *Optionally*: options such as defining the initial heap configuration, control granularity of abstraction, control garbage collection behaviour, allow re-use of results.

#### Expected output:
1. Computed abstract state space
2. Derived procedure contracts
3. Model checking results, for each LTL formula either: `formula satisfied`, `formula (definitely) not satisfied` or `formula possibly not satisfied`. In case it is (possibly) not satisfied, a counterexample is produced (an abstract trace that violates the LTL formula, possibly a concrete initial heap).
4. General information about the analysis: log messages, details about settings and runtime of analyses

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Symbolic execution is used to construct an abstract state space

#### Last publication date:
2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_1
