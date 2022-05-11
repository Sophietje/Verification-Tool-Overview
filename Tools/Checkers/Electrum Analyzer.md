Model checker for Electrum specifications

#### Name:
Electrum Analyzer (sometimes called 'Electrum')

#### Application domain/field:
Model checking
Relational logic
Relational specifications

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Electrum model
- *Optional*: assertions (LTL properties)

#### Expected input format:
Electrum language

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Electrum is an extension of [Alloy](../Solvers/Alloy%20Analyzer.md) that enriches its relational logic with LTL operators.
The Electrum Analyzer can do bounded model checking (encoded into SAT) and unbounded model checking (encoding into SMV)

There are two main commands to analyse Electrum models:
- *run*: searches for instances that satisfy certain properties
- *check*: searches for counter-examples that break desirable properties

There is a visualiser to inspect the results of the *run* and *check* commands.

#### Comments:
License: Apache License 2.0

#### URIs (github, websites, etc.):
Repository: https://github.com/haslab/Electrum2
Repository of Electrum Analyzer version 1 (no longer maintained): https://github.com/haslab/electrum
Electrum examples: https://github.com/haslab/Electrum/wiki/Examples
Project page: https://haslab.github.io/Electrum/

#### Last commit date:
21 April 2021

#### Last publication date:
3 September 2018

#### List of related papers:
https://doi.org/10.1145/3238147.3240475 (ASE '18)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Model checking
:: LTL
:: PV4 :: checks assertions and LTL properties in Electrum models with bounded or unbounded model checking