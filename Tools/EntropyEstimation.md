
#### Name:
EntropyEstimation

#### Application domain/field:
Quantified information flow
Confidentiality measurements
Information leakage

#### Type of tool (e.g. model checker, test generator):
-

#### Expected input thing:
Boolean formula

#### Expected input format:
CNF file

#### Expected output:
Shannon entropy estimation

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Estimates the Shannon entropy of a formula $\varphi$ such that the computed estimate is guaranteed to lie with ($1 +- \epsilon$)-factor of the ground truth with confidence at least $1-\delta$.

They focus on Boolean formulas that capture the relationship between input X and output Y of a given program. They estimate the Shannon entropy for this Boolean formula.

Uses [[GANAK]] for model counting queries and [[SPUR]] for sampling queries.

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/meelgroup/entropyestimation
- Technical report with the complete analysis for all of the benchmarks: https://arxiv.org/pdf/2206.00921.pdf.

#### Last commit date:
4 June 2022

#### Last publication date:
7 August 2022

#### List of related papers:
https://doi.org/10.1007/978-3-031-13185-1_18 (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV1 :: computes the Shannon entropy for a given program
:: Security
:: Source :: https://doi.org/10.1007/978-3-031-13185-1