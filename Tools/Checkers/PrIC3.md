Symbolic model checking of Markov decision processes (MDPs).

#### Name:
PrIC3

#### Application domain/field:
Model checking
Symbolic model checking
Probabilistic model checking
Markov decision processes (MDPs)

#### Type of tool (e.g. model checker, test generator):
Probabilistic model checker

#### Expected input thing:
- Global MDP `M`
- Set of bad states `B`
- Threshold $\lambda$

#### Expected input format:
- *MDP*: [PRISM](PRISM.md) guarded command language
- *Set of bad states*: ?
- *Threshold*: ?

#### Expected output:
`true` or `false`.
If the tool returns `false`, it will provide a *possible* counterexample. This can be caused by two reasons: either the MDP is indeed unsafe, or the heuristic was inappropriate. The counterexample consists of a subsystem of states of the MDP witnessing $Pr^{max}(s_I \models \lozenge B) > \lambda$

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Extension of [[IC3]], for quantitative reachability in MDPs.
Uses efficient data structures from [Storm](Storm.md) and uses [Z3](../Solvers/SMT/Z3.md).

#### Comments:
It is called a 'prototypical implementation' in the CAV '20 paper.

#### URIs (github, websites, etc.):
Repository: https://github.com/moves-rwth/PrIC3

#### Last commit date:
30 September 2020

#### Last publication date:
14 July 2020

#### List of related papers:
[PrIC3: Property Directed Reachability for MDPs](https://doi.org/10.1007/978-3-030-53291-8_27)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Probabilistic
:: Model checking
:: PV1 :: checks if the Markov decision process is safe