Synthesis tool for recursive functions that satisfy both a functional specification and an asymptotic resource bound.

Example usage:
User asks the tool to synthesize an implementation of a sorting function with resource usage O(n log n) where n is the length of the input list.

#### Name:
SynPlexity

#### Application domain/field:
Program synthesis
Resource bound
Recursive functions
Resource-bound analysis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
- Refinement type that describes both the functionality and the asymptotic (big-O) resource usage of a program
- Set of auxiliary functions that the synthesized program can use

#### Expected input format:
`.sq` file?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Implemented on top of [[Synquid]], uses [Z3](../Solvers/SMT/Z3.md).
It uses a type-directed synthesis algorithm.

#### Comments:
License: MIT license

#### URIs (github, websites, etc.):
Repository: https://github.com/Herbping/Synplexity

#### Last commit date:
27 May 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[Synthesis with Asymptotic Resource Bounds](https://doi.org/10.1007/978-3-030-81685-8_37) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [[Synquid]] and [[ReSyn]]

#### Meta
:: Synthesis
:: PV2 :: synthesises recursive functions that satisfy a functional specification and an asymptotic resource bound