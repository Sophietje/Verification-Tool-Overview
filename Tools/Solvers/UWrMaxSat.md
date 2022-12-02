Solver for MaxSAT and pseudo-Boolean problems

#### Name:
UWrMaxSat

#### Application domain/field:
MaxSAT problems
Pseudo-Boolean problems

#### Type of tool (e.g. model checker, test generator):
Solver

#### Expected input thing:
MaxSAT or pseudo-Boolean problem

#### Expected input format:
`.wcnf` (MaxSAT) input file format or old variant of the OPB file format (`.opb`).

#### Expected output:
`s SATISFIABLE`, `c SATISFIABLE`, `s UNSATISFIABLE` , `s OPTIMUM FOUND` or `s UNKNOWN`

There is an option to print (more verbose) output to a file.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [[COMiniSatPS]], which can be replaced with [[CaDiCaL]] or [[Glucose]] or [[mergesat]].
Integrates the MaxPre preprocessor.

#### Comments:
This was created as an extension of [MiniSat+](MiniSat+.md). It was extended such that it could deal with MaxSAT instances.

#### URIs (github, websites, etc.):
Repository: https://github.com/marekpiotrow/UWrMaxSat

#### Last commit date:
28 Sep 2022 (default branch)
28 Sep 2022 (last activity)

#### Last publication date:
November 2020

#### List of related papers:
[UWrMaxSat: Efficient Solver for MaxSAT and Pseudo-Boolean Problems](https://doi.org/10.1109/ICTAI50040.2020.00031) (ICTAI 2020)

#### Related tools (tools mentioned or compared to in the paper):
"Since the version 1.3 you can merge the power of this solver with the [[SCIP]] solver, if you have a licence to use it"

#### Meta
:: PV4 :: a complete solver for partial weighted MaxSAT instances
:: Source :: extension of [[MiniSat+]] :: https://doi.org/10.1145/3550355.3552426
