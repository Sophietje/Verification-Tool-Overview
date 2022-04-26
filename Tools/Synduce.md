#### Name:
Synduce

#### Application domain/field:
Program synthesis
Recursive functions
Recursive data types
Bounded model checking

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
- Input reference (recursive) function, this precisely describes the functionality
- Recursion skeleton, i.e. traversal plan over the new recursive data type
- Representation function, a mapping that converts an instance of the old data type to the new data type

#### Expected input format:
One of the following:
- a syntax for pattern-matching recursion schemes (PRMS) (`.pmrs` file)
- OCaml (`.ml` file)

#### Expected output:
Recursive function equivalent to the input function whose recursion strategy is specified by the recursion skeleton.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The *context* that they consider is one where you have two data types A and B. You have implemented a recursive function for A, and now want to implement this for B. 

Synduce uses bounded model checking to check the validity of a synthesis solution.

Uses [Z3](Solvers/SMT/Z3.md) and [CVC4](Solvers/SMT/CVC4.md).

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/synduce/Synduce

#### Last commit date:
16 December 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_39 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Tools for synthesizing recursive functional programs: [Escher](Synthesiser/Escher.md), $\lambda^2$, [[Myth]], [[Myth2]], [[SynQuid]], [[SyntRec]], [[Leon]].

#### Meta
:: Synthesis
:: Model checking
:: OCaml