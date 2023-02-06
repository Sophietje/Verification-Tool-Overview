#### Name:
GANAK

#### Application domain/field:
Model counting
Boolean formula

#### Type of tool (e.g. model checker, test generator):
Model counter

#### Expected input thing:
- Boolean formula $F$
- Confidence $\delta$

#### Expected input format:
- *Boolean formula*: CNF file
- *Confidence $\delta$*: ?

#### Expected output:
The number of solutions of the formula $F$ with confidence at least $1-\delta$

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/meelgroup/ganak

#### Last commit date:
18 November 2022

#### Last publication date:
10 August 2019

#### List of related papers:
- [GANAK: A Scalable Probabilistic Exact Model Counter](https://dl.acm.org/doi/abs/10.5555/3367032.3367198) (IJCAI '19)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV1 :: Counts number of possible solutions for a Boolean formula
:: Source :: Used by [CountMUST](Tools/CountMUST.md) and [EntropyEstimation](Tools/EntropyEstimation.md)