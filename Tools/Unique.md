#### Name:
Unique

#### Application domain/field:
Gate extraction
Quantified Boolean Formulas (QBFs)

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
- PCNF formula (QDIMACS)
- prenex non-CNF QBF (QCIR)
- DQBF with CNF matrices (DQDIMACS)

#### Expected input format:

#### Expected output:
- interpolants represented as AIG (And-Inverter Graphs)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- *Gate detection*
- *Gate extraction*

Uses [[ItpMiniSat]], a modified version of [[MiniSat]], bundled with the [[ExtAvy]] model checker

#### Comments:

#### URIs (github, websites, etc.):
https://github.com/fslivovsky/unique

#### Last commit date:
13 Sep 2022

#### Last publication date:
14 July 2020

#### List of related papers:
[Interpolation-Based Semantic Gate Extraction and Its Applications to QBF Preprocessing](https://doi.org/10.1007/978-3-030-53288-8_24) (CAV '20)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV4 :: generates interpolant graphs from CNF formulae