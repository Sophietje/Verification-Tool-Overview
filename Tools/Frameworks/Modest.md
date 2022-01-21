Toolset for modelling and analysis of hybrid, real-time distributed and stochastic systems

#### Name:
Modest Toolset

#### Application domain/field:
Model checking
Hybrid systems
Real-time systems
Distributed systems
Stochastic systems

#### Type of tool (e.g. model checker, test generator):
Combination of several tools include model checkers and translators.

#### Expected input thing:
?

#### Expected input format:
Modest toolset (own) format or [JANI](../../Formats/JANI.md) format.

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The tool consists of the following tools:
- [mcsta](../Checkers/mcsta.md): disk-based explicit-state model checker for STA, PTA and MDP
- [[modes]]: statistical model checker for SHA, STA, PTA and MDP
- [[prohver]]: safety model checker for SHA
- [[mosta]]: generates a graphical representation of a SHA
- [[moconv]]: converts models between Modest's input language to the [JANI](../../Formats/JANI.md) format and back

#### Comments:
STA: Stochastic Timed Automata
PTA: Probabilistic Timed Automata
MDP: Markov Decision Processes
SHA: Stochastic Hybrid Automata

#### URIs (github, websites, etc.):
Project page: https://www.modestchecker.net/
Tutorial for modelling and analysing Markov automata in Modest: https://doi.org/10.1007/978-3-030-31423-1_8

#### Last commit date:
9 July 2021

#### Last publication date:
2020

#### List of related papers:
https://doi.org/10.1007/978-3-642-54862-8_51
https://doi.org/10.1007/978-3-030-53291-8_26

#### Related tools (tools mentioned or compared to in the paper):
This toolset includes the model checker [mcsta](../Checkers/mcsta.md).

#### Meta
:: Framework