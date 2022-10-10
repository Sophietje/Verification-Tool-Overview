#### Name:
Storm

#### Application domain/field:
Probabilistic model checking
Model checking

#### Type of tool (e.g. model checker, test generator):
Probabilistic model checker

#### Expected input thing:
- Input model: 
	- DTMCs (discrete time markov chains)
	- CTMCs (continuous time markov chains)
	- MDPs (Markov decision processes)
	- GSPN (Generalized Stochastic Petri nets)
	- DFTs (Dynamic fault trees)
	- cpGCL (conditional probabilistic guarded command language) program
	- Explicit model

- Quantitative specification:
	- PCTL (probabilistic computation tree logic, for discrete-time models)
	- CSL (continuous stochastic logic, for continuous-time models)
	- Extensions of the abovementioned logics: Expected rewards, long-run average rewards, conditional probabilities and multi-objective model checking

#### Expected input format:
Storm supports many different input formats:
- *Input model*: 
	- [PRISM](PRISM.md) for DTMCs, CTMCs and MDPs
	- [JANI](../../Formats/JANI.md) for DTMCs, CTMCs and MDPs
	- [[PNML]] or [[GreatSPN]] for GSPNs
	- [[Galileo]] format for DFTs
	- [[cpGCL]]
	- Explicit format
- *Specification*:  
	- "Extended subset" of the [PRISM](PRISM.md) property language
	- Embedded in the JANI model

#### Expected output:
Depends on the property. It can give the probability of a certain outcome, but also whether a property is true or false. 
It will also give information about the model such as the number of states and transitions.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It uses the following solvers: [[Eigen]], [[gmm++]], [CUDD](../Libraries/CUDD.md), [Sylvan](../Sylvan.md), [Gurobi](../Solvers/Gurobi.md), [GLPK](../Libraries/GLPK.md), [Z3](../Solvers/SMT/Z3.md), [MathSAT](../Solvers/SMT/MathSAT.md), [SMT-LIB](../../Formats/SMT-LIB.md)

#### Comments:
There is also a fuzzer that is called [STORM](https://practical-formal-methods.github.io/storm/).

#### URIs (github, websites, etc.):
Project page: https://www.stormchecker.org/
Some benchmarks from papers are available via http://www.stormchecker.org/benchmarks.html
Repository: https://github.com/moves-rwth/storm

#### Last commit date:
7 October 2021

#### Last publication date:
6 July 2021

#### List of related papers:
[The probabilistic model checker Storm](https://doi.org/10.1007/s10009-021-00633-z) (STTT '21)
[A Storm is Coming: A Modern Probabilistic Model Checker](https://doi.org/10.1007/978-3-319-63390-9_31) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Probabilistic
:: PV5           :: computes how a given property is related to a given specification
:: Model checking