#### Name:
DetLP

#### Application domain/field:
Quantitative inclusion
Discounted-Sum automata (DS-automata)

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Weighted automata $P$
- Weighted automata $Q$
- Discount-factor $d > 1$

#### Expected input format:
- Weighted automata should be in `.txt` files according to a specific format described in the code.
- The discount-factor can be passed when calling the python script.

#### Expected output:
True if $P\subseteq_dQ$

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Linear-programming based DS-inclusion
DS-inclusion: quantitative inclusion for discounted-sum weighted automata
Quantitative inclusion: comparing quantitative dimensions between systems such as energy consumption and worst-case execution time.

Uses [GLPSOL](Solvers/GLPSOL.md), [Reduce](Reduce.md).

#### Comments:

#### URIs (github, websites, etc.):
Repository: https://github.com/suguman/DetLP

#### Last commit date:
7 October 2017

#### Last publication date:
18 July 2018

#### List of related papers:
[Automata vs Linear-Programming Discounted-Sum Inclusion](https://doi.org/10.1007/978-3-319-96142-2_9)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Automaton
:: PV1 :: comparator of two weighted automata