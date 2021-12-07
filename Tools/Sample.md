Infers permission pre- and postconditions for array programs

#### Name:
Sample

#### Application domain/field:
Separation logic
Program verification
Array programs
Permissions
Pre- and postconditions

#### Type of tool (e.g. model checker, test generator):
Specification generator/annotation generator

#### Expected input thing:
Program

#### Expected input format:
Viper program

#### Expected output:
Program annotated with permission pre- and postconditions

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Sample infers permission pre- and postconditions for [Viper](Frameworks/Viper.md) programs.

The tool first performs a forward numerical analysis to infer over-approximate loop invariants. Then, the tool performs inference and maximum elimination. Finally, it adds the annotations to the input program.

Uses [Apron](Libraries/Apron.md) for numerical analysis.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/viperproject/sample

#### Last commit date:
5 June 2020

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96142-2_7 (CAV 2018)

#### Related tools (tools mentioned or compared to in the paper):
-