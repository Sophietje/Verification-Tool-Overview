
#### Name:
SLURF

#### Application domain/field:
Continuous-time Markov chains (CTMCs)
Probabilistic systems
Model checking

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- CTMC (Continuous-time Markov Chain)
- Parameter probability distribution file that defines the probability distributions of the parameters
- Property definition file that defines the properties that are verified by Storm
- Number of samples
- Confidence level

#### Expected input format:
- *CTMC*: model file, they support the [PRISM language](../../Formats/PRISM%20language.md) for parametric CTMCs and the [[Galileo]] format for parametric fault trees.
- *Parameter probability distribution file*: Excel or CSV (semi-colon separated) file
- *Property definition file*: Excel or CSV (semi-colon separated) file
- Others are passed as parameters when executing the python script.

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Storm](../../Tools/Checkers/Storm.md)

#### Comments:
-

#### URIs (github, websites, etc.):
- Artifact: https://doi.org/10.5281/zenodo.6523863.

#### Last commit date:
-

#### Last publication date:
7 August 2022

#### List of related papers:
[Sampling-Based Verification of CTMC with Uncertain Rates](https://doi.org/10.1007/978-3-031-13188-2_2) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Probabilistic programs