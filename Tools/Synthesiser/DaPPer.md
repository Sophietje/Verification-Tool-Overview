A tool to synthesize full PPL (probabilistic programming language) models from relational datasets.

#### Name:
DaPPer: Data-guided Probabilistic Program synthesizer

#### Application domain/field:
Probabilistic programming
Program synthesis

#### Type of tool (e.g. model checker, test generator):
Probabilistic program synthesizer

#### Expected input thing:
- Dataset
- Causal Order hypothesis (ordering of the dataset column identifiers). This is a hypothesis about the direction of causal links between variables.

#### Expected input format:
- *Dataset*: `.csv` file
- *Causal order hypothesis*: ?

#### Expected output:
PPL program in a subset of the [BLOG](../../Formats/BLOG.md) language.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It uses simulated annealing (SA) to synthesize PPL (probabilistic programming language) programs from relational datasets.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/schasins/PPL-synthesis

#### Last commit date:
21 Jan 2017 (default branch)
21 Jan 2017 (last activity)

#### Last publication date:
13 July 2017

#### List of related papers:
[Data-Driven Synthesis of Full Probabilistic Programs](https://doi.org/10.1007/978-3-319-63387-9_14) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
[[PSketch]]: given a sketch of a nearly complete PPL program and a dataset, it will synthesize expressions to complete the program.

#### Meta
:: Probabilistic
:: PV2 :: synthesises probabilistic programs from relational datasets
:: Synthesis
:: Source :: https://doi.org/10.1145/3550355.3552426
