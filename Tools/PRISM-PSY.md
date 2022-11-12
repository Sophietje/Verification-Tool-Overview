GPU-accelerated parameter synthesis for stochastic systems

#### Name:
PRISM-PSY

#### Application domain/field:
Continuous-time Markov chains (CTMCs)
Parameter synthesis
Continuous stochastic logic (CSL)
Model checking
Stochastic model checking

#### Type of tool (e.g. model checker, test generator):
Parameter synthesizer

#### Expected input thing:
?

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
In model checking, one often assumes that model parameters are known. However, if these parameters are not known, then you can use parameter synthesis.

In **parameter synthesis** for CTMCs, one takes a time-bounded CSL formula and a model whose transition rates are functions of the parameters. Then you try to find parameter values such that the satisfaction probability of the CSL formula meets a given threshold, is maximised, or is minimised.

This tool uses GPUs to accelerate the synthesis procedure.

PRISM-PSY uses the front-end of [PRISM](Checkers/PRISM.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://www.prismmodelchecker.org/psy/
Repository: https://github.com/Palmik/prism-pse

#### Last commit date:
8 August 2014

#### Last publication date:
9 April 2016

#### List of related papers:
[PRISM-PSY: Precise GPU-Accelerated Parameter Synthesis for Stochastic Systems](https://doi.org/10.1007/978-3-662-49674-9_21) (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
Parameter synthesis for discrete-time Markovian models: [[PROPhESY]]

#### Meta
:: PV2 :: synthesises model parameters such that a property meets a given threshold
:: Source :: https://doi.org/10.1145/3550355.3552426