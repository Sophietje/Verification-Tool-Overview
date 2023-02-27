
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
- *CTMC*: model file, in the [PRISM language](../../Formats/PRISM%20language.md) for parametric CTMCs and the [[Galileo]] format for parametric fault trees.
- *Parameter probability distribution file*: Excel or CSV (semi-colon separated) file
- *Property definition file*: Excel or CSV (semi-colon separated) file
- Others are passed as parameters when executing the python script.

#### Expected output:
Prediction region (as image(s))

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Storm](../../Tools/Checkers/Storm.md)

SLURF computes prediction regions. This is useful since there are many cases where you are not sure what the exact transition rates or probabilities are. 
The prediction regions can depict how the uncertainty in the input influences the output. Intuitively this gives some feeling for the robustness of the output for some uncertain input.

#### Comments:
-

#### URIs (github, websites, etc.):
- Artifact: https://doi.org/10.5281/zenodo.6523863.
- Repository: https://github.com/LAVA-LAB/slurf

#### Last commit date:
22 September 2022

#### Last publication date:
7 August 2022

#### List of related papers:
[Sampling-Based Verification of CTMC with Uncertain Rates](https://doi.org/10.1007/978-3-031-13188-2_2) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Probabilistic programs