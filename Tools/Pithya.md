Tool for parameter synthesis of piecewise multi-affine dynamical systems from specifications expressed in a hybrid branching-time temporal logic.

#### Name:
Pithya

#### Application domain/field:
Parameter synthesis
Hybrid branching-time temporal logic
Dynamical systems
Piecewise multi-affine dynamical systems
Differential equations

#### Type of tool (e.g. model checker, test generator):
Parameter synthesizer

#### Expected input thing:
- Parametrised model of a continuous-time dynamical system
- Desired properties, expressed in a hybrid extension of the UCTL logic, $HUCTL_P$

#### Expected input format:
- *Parametrised model*: own `.bio` format
- *Properties*: own `.huctl` format

#### Expected output:
Set of all parameter valuations under which the system satisfies the formula.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Pithya takes as input a parametrised model of a continuous-time dynamical system. This system is described by autonomous ordinary differential equations (ODEs) with sigmoidal functions.
Pithya then approximates this model into a piecewise multi-affine model and discretises it into a parametrised direction transition system (PDTS).
Using the computed PDTS and the $HUCTL_P$ formula, it computes all parameter valuations under which the PDTS satisfies the formula.

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Project page: http://biodivine.fi.muni.cz/pithya
Repository GUI: https://github.com/sybila/pithya-gui
Repository: https://github.com/sybila/pithya-core

#### Last commit date:
16 Aug 2022

#### Last publication date:
13 July 2017

#### List of related papers:
[Pithya: A Parallel Tool for Parameter Synthesis of Piecewise Multi-affine Dynamical Systems](https://doi.org/10.1007/978-3-319-63387-9_29) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Synthesis
:: PV2 :: provide a set of parameter valuations to satisfy the given formula on a given dynamical system