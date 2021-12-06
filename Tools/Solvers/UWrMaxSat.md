Solver for MaxSAT and pseudo-Boolean problems

#### Name:
UWrMaxSat (sometimes stylized as uwrmaxsat)

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
Uses [[COMiniSatPS]]

#### Comments:
This was created as an extension of [MiniSat+](MiniSat+.md). It was extended such that it could deal with MaxSAT instances.

#### URIs (github, websites, etc.):
Repository: https://github.com/marekpiotrow/UWrMaxSat

#### Last commit date:
1 December 2021

#### Last publication date:
November 2020

#### List of related papers:
https://doi.org/10.1109/ICTAI50040.2020.00031 (ICTAI '20)

#### Related tools (tools mentioned or compared to in the paper):
