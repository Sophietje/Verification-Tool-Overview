Tool to translate a typical First-Order Linear Temporal Logic (FOLTL) specification into two of its decidable fragments.

#### Name:
Cervino

#### Application domain/field:
First-Order Linear Temporal Logic (FOLTL)
Specification transformation/translation

#### Type of tool (e.g. model checker, test generator):
Specification translator?

#### Expected input thing:
- Cervino specification
- Property to be checked

#### Expected input format:
Cervino file

#### Expected output:
If the process is automated with the `-s` option, then it will report either `SAT` or `UNSAT`.

Otherwise, it generates a file `output.als` which can be analyzed with the Electrum Analyzer.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The tool takes a Cervino specification as input and generates Electrum models which are given to the [Electrum Analyzer](Checkers/Electrum%20Analyzer.md), which calls a complete procedure in [nuXmv](Checkers/nuXmv.md).

#### Comments:
Cervino seems to be both a name for the modelling language and for the tool.

#### URIs (github, websites, etc.):
Artifact for CAV '21 paper: https://zenodo.org/record/4893262
Repository: https://github.com/grayswandyr/cervino

#### Last commit date:
2 June 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_16 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: LTL
:: PV2 :: transforms first order LTL formulae to Electrum models