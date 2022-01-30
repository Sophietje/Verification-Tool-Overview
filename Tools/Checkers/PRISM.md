Probabilistic model checker, specifically for quantitative verification of (priced) probabilistic timed automata

#### Name:
PRISM

#### Application domain/field:
Model checking
Probabilistic model checking
Symbolic model checking
Probabilistic timed automata

#### Type of tool (e.g. model checker, test generator):
Probabilistic model checker

#### Expected input thing:
- Model (e.g. a probabilistic automata)
- Property to check (e.g. "what is the probability of a failure causing the system to shut down within 4 hours?")

#### Expected input format:
PRISM language

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
PRISM can be used to analyse many different types of probabilistic models, including:
- Discrete-time Markov chains (DTMCs)
- Continuous-time Markov chain (CTMCs)
- Markov decision processes (MDPs)
- Probabilistic automata (PAs)
- Probabilistic timed automata (PTAs)
- Partially observable Markov decision processes (POMDPs)
- Partially observable probabilistic timed automata (POPTAs)
Such models can be used to analyse systems from domains such as communication protocols, randomised distributed algorithms, security protocols and biological systems.

It includes several different techniques that can be used to analyse systems, including:
- Approximate/statistical model checking
- Quantitative abstraction refinement
- Symmetry reduction

#### Comments:
Along with the tool, there also exists a [PRISM language](../../Formats/PRISM%20language.md).

#### URIs (github, websites, etc.):
Project page: https://www.prismmodelchecker.org/
Repository: https://github.com/prismmodelchecker/prism

#### Last commit date:
16 July 2021

#### Last publication date:
?

#### List of related papers:
https://doi.org/10.1007/3-540-46029-2_13 (TOOLS '02)
https://doi.org/10.1007/978-3-642-22110-1_47 (CAV '11)
https://doi.org/10.1007/978-3-662-49674-9_20 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
[PRISM-PSY](../PRISM-PSY.md), [PRISM-games](PRISM-games.md)

#### Meta
:: Automaton
:: Probabilistic
:: PV3 :: model checker for probabilistic timed automata