Platform/framework for the analysis of C code

#### Name:
Frama-C

#### Application domain/field:
Software verification
Runtime verification
Deductive verification
Abstract interpretation

#### Type of tool (e.g. model checker, test generator):
Framework

#### Expected input thing:
- C program
- Specifications (as [ACSL](../../Formats/ACSL.md) annotations)

#### Expected input format:
`.c` file with [ACSL](../../Formats/ACSL.md) annotations.

#### Expected output:
Depends on the plugin that is used.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
It has many different types of plugins that do different kind of analyses such as WP (deductive verification), E-ACSL (runtime verification), PathCrawler (test case generator) and EVA (value analysis based on abstract interpretation).

It uses the specification language [ACSL](../../Formats/ACSL.md). Some plugins support a subset of [ACSL](../../Formats/ACSL.md).

#### Comments:
It can be run from the command-line or via its graphical user interface. Some plugins are meant to be used via the command-line, not via the GUI.

#### URIs (github, websites, etc.):
Project page: https://frama-c.com/index.html
Repository: https://git.frama-c.com/pub/frama-c/

#### Last commit date:
22 October 2021

#### Last publication date:
12 July 2021

#### List of related papers:
https://doi.org/10.1145/3464974.3468451 (VORTEX 2021)
https://doi.org/10.1007/978-3-662-54577-5_22 (TACAS 2017)
https://doi.org/10.1007/s10009-011-0192-z (VSTTE 2009-2010)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Framework
:: PV1 :: framework providing abstractions for C code analysis