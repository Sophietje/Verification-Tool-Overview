
#### Name:
FRET (Formal Requirements Elicitation tool)

#### Application domain/field:
Requirements engineering
Requirements formalization
Specification
Realizability checking

#### Type of tool (e.g. model checker, test generator):
Framework for writing and analyzing requirements

#### Expected input thing:
Requirements

#### Expected input format:
Restricted natural language called [[FRETish]] (own language)

#### Expected output:
Depends on how the tool is used.
It provides a dashboard through which the user can interact with the requirements, including editing, visualization and analysis.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [JKind](../../Tools/Checkers/JKind.md) and [[Kind 2]] to implement realizability checks.

#### Comments:
Developed at NASA

#### URIs (github, websites, etc.):
Repository: https://github.com/NASA-SW-VnV/fret

#### Last commit date:
25 January 2023

#### Last publication date:
6 August 2022

#### List of related papers:
[Capture, Analyze, Diagnose: Realizability Checking of Requirements in FRET](https://doi.org/10.1007/978-3-031-13188-2_24) (CAV 2022)
[Automated formalization of structured natural language requirements](https://doi.org/10.1016/j.infsof.2021.106590) (Journal of Information and Software Technology '21)
[Formal Requirements Elicitation with FRET](https://ntrs.nasa.gov/citations/20200001989)

#### Related tools (tools mentioned or compared to in the paper):
Requirement specification tools for reactive synthesis (over GR(1) fragment of LTL): [[Spectra Tools]], [[RATSY]]
Tools for requirement specification and analysis: [SpeAR](SpeAR.md), [AGREE](../../Tools/Checkers/AGREE.md), [[EARS-CTRL]]

#### Meta
:: Framework
:: Requirements