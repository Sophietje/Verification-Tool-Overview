Tool to synthesize a set of implementation decisions ensuring that a desired property is preserved from a high-level design into a low-level platform implementation

#### Name:
Mapping Synthesis Tool

#### Application domain/field:
Event-based behavioural models
Synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
- Processes P and Q
- Specification $\Phi$
- Mapping constraint C

#### Expected input format:
[Alloy](Alloy.md) model (`.als` file)

#### Expected output:
If it exists, a maximal set of mappings that ensures that the resulting platform implementation preserves the given property.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [Alloy](Alloy.md) and [Alloy Analyzer](Solvers/Alloy%20Analyzer.md)

#### Comments:
Note the authors themselves call this a "prototype implementation" and it doesn't seem to have been updated since the paper was published.

#### URIs (github, websites, etc.):
Repository: https://github.com/eskang/MappingSynthesisTool

#### Last commit date:
3 February 2019

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25540-4_12 (CAV 2019)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV2 :: given a high level spec and a low level spec, produces a set of property-preserving mappings
:: Source :: https://doi.org/10.1145/3550355.3552426