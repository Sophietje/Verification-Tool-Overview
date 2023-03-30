#### Name:
Attestor

#### Application domain/field:
Model checking
Pointer programs

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Java or Java Bytecode program
- LTL formulae (specifications to be checked)
- Declaration of the graph grammar that guides abstraction
- *Optionally*: options such as defining the initial heap configuration, control granularity of abstraction, control garbage collection behaviour, allow re-use of results.

#### Expected input format:
- Java or Java Bytecode program
- LTL formula is passed via a command-line option (`--model-checking`)
- Graph grammar is specified as a JSON-array of rules
- *Options*: given via the command-line

#### Expected output:
1. Computed abstract state space
2. Derived procedure contracts
3. Model checking results, for each LTL formula either: `formula satisfied`, `formula (definitely) not satisfied` or `formula possibly not satisfied`. In case it is (possibly) not satisfied, a counterexample is produced (an abstract trace that violates the LTL formula, possibly a concrete initial heap).
4. General information about the analysis: log messages, details about settings and runtime of analyses

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Symbolic execution is used to construct an abstract state space

#### Comments:
The Github repository has an extensive [wiki](https://github.com/moves-rwth/attestor/wiki) which describes things such as the graph grammar syntax.

It is possible to use a settings file (.attestor) that is a collection of command-line options which can then be imported with the tool.

#### URIs (github, websites, etc.):
https://moves-rwth.github.io/attestor/
Examples: https://github.com/moves-rwth/attestor-examples

#### Last commit date:
17 Dec 2021 (last activity)

#### Last publication date:
18 July 2018

#### List of related papers:
[Let this Graph Be Your Witness!](https://doi.org/10.1007/978-3-319-96142-2_1)

#### Related tools (tools mentioned or compared to in the paper):
[Forester](../Forester.md), [[Groove]], [[Infer]], [[HIP/SLEEK]], [[Korat]], [[Juggernaut]], [[Tvla]]

#### Meta
:: LTL
:: Java
:: PV5 :: checks if a property holds for a program, generates additional properties, provides examples and analysis logs
:: Model checking
:: Source :: https://doi.org/10.1145/3550355.3552426
