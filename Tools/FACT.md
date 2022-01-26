Probabilistic model checker that can compute confidence intervals for certain properties for which observations of the transitions associated with unknown probabilities are available.

#### Name:
FACT: Formal verification with confidence intervals

#### Application domain/field:
Quantitative verification
Probabilistic model checking
Model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Parametric Markov chain (PMC)
- PCTL property
- Range of confidence levels

#### Expected input format:
- *PMC*: Extended version of [PRISM](Checkers/PRISM.md) modelling language
- *PCTL property*: ?
- *Range of confidence intervals*: 

#### Expected output:
Confidence interval for each confidence level $\alpha$ from the user-specified range

#### Internals (tools used, frameworks, techniques, paradigms, ...):
FACT uses a four-step approach:
1. Parametric quantitative verification is used to obtain an algebraic expressed for the analysed PCTL property (uses [PRISM](Checkers/PRISM.md))
2. Simultaneous confidence intervals are calculated for each set of parameters
3. Uses results of step 2 for a convex optimisation problem whose solution represents an $\alpha$ confidence interval for the analysed property
4. Uses a heuristic to seek alternative confidence intervals. This optimisation might reduce the width of property confidence intervals.

Uses [PRISM](Checkers/PRISM.md)

#### Comments:
License: GNU General Public LIcense

#### URIs (github, websites, etc.):
Project page: http://www-users.cs.york.ac.uk/~cap/FACT

#### Last commit date:
-

#### Last publication date:
9 April 2016

#### List of related papers:
https://doi.org/10.1007/978-3-662-49674-9_32 (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Probabilistic