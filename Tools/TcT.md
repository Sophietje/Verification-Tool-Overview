#### Name:
$T_CT$: Tyrolean Complexity Tool

#### Application domain/field:
Complexity analysis
Term rewrite systems
Integer transition system
Amortized resource analysis

#### Type of tool (e.g. model checker, test generator):
Complexity analyser

#### Expected input thing:
Program/system

#### Expected input format:
Depends on the instance that is used:
- `tct-its` expects a `.its` file (integer transition system)
- `tct-trs` expects a `.trs` file (term rewrite system)
- `tct-hoca` expects a `.fp` file. It translates a pure fragment of OCaml to a TRS.
- `tct-jbc` expects a `.trs` file.

#### Expected output:
If successful, textual representation of the obtained complexity judgement, and corresponding proof tree.
If not successful, it will print the uncompleted proof tree and the reason for failure.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
$T_CT$ has several instances which provide automated complexity analysis for different kinds of systems:
- `tct-its` for integer transition systems. Uses [Yices](Solvers/SMT/Yices.md).
- `tct-trs` for term rewrite systems. Uses [[MiniSmt]]
- `tct-hoca` for higher-order systems
- `tct-jbc` for Jinja bytecode. Uses [Yices](Solvers/SMT/Yices.md), [[MiniSmt]]

#### Comments:
License: BSD3

#### URIs (github, websites, etc.):
Project page: https://tcs-informatik.uibk.ac.at/tools/tct/
Collection of repositories: https://github.com/ComputationWithBoundedResources
Try online: http://colo6-c703.uibk.ac.at/tct/index.php

#### Last commit date:
18 August 2020
16 Feb 2017 (last activity)
16 Feb 2017 (last activity)
16 Feb 2017 (last activity)
16 Feb 2017 (last activity)

#### Last publication date:
9 April 2016

#### List of related papers:
[Automated amortised resource analysis for term rewrite systems](https://doi.org/10.1016/j.scico.2019.102306) (Science of Computer Programming, Vol. 185, '20)
[TcT: Tyrolean Complexity Tool](https://doi.org/10.1007/978-3-662-49674-9_24) (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):
[AProVE](AProVE.md)

#### Meta
:: Complexity
:: PV1 :: determines the complexity, including proof, of a given integer transition system or term rewrite system
