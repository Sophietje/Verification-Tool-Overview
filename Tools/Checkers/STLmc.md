
#### Name:
STLmc

#### Application domain/field:
Signal Temporal Logic (STL)
Hybrid systems
Bounded model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Model of hybrid system, i.e. hybrid automaton
- STL properties

#### Expected input format:
- *Model*: `.model` file, STLmc modelling language
- *STL property*: also specified in the model file, STLmc modelling language 

#### Expected output:
Whether the properties hold or not.
If not, a counterexample can be shown.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The tool can be used to verify that, up to given bounds, the robustness degree of an STL formula $\varphi$ is greater than a robustness threshold $\epsilon > 0$ for all possible behaviors of the ysstem.
This is done by reducing the STL model checking problem to Boolean STL model checking using $\epsilon$-strengthening.

It uses SMT solvers such as [Z3](../../Tools/Solvers/SMT/Z3.md), [Yices](../../Tools/Solvers/SMT/Yices.md)2 and [dReal](../../Tools/Solvers/SMT/dReal.md).

#### Comments:
-

#### URIs (github, websites, etc.):
- Project page: https://stlmc.github.io
- Repository: https://github.com/stlmc/stlmc

#### Last commit date:
2 February 2023

#### Last publication date:
7 August 2022

#### List of related papers:
[STLmc:  Robust Model Checking of Hybrid Systems Using SMT](https://doi.org/10.1007/978-3-031-13185-1_26) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Model checking
:: STL
:: PV3 :: checks whether STL properties hold for a given hybrid system