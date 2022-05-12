Optimization Modulo Theories (OMT) tool

OptiMathSat allows for solving a list of optimization problems on SMT formulas with linear objective functions. It supports Boolean, rational and integer domains, as well as combinations of these, including MaxSMT.

#### Name:
OptiMathSAT

#### Application domain/field:
Optimization Modulo Theories (OMT)
Optimization problems
SMT formulas
Linear objective functions

#### Type of tool (e.g. model checker, test generator):
Optimization solver?

#### Expected input thing:
?

#### Expected input format:
One of the following two:
- [SMT-LIB](../../Formats/SMT-LIB.md) v2, enriched with language extensions for dealing with optimization capabilities
- [[FlatZinc]] 1.6 language format

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Extension of [MathSAT](SMT/MathSAT.md) 5. 
OMT is an extension of SMT to find models that optimize objection functions

#### Comments:
License: same license conditions as MathSAT 5. It is available for research and evaluation purposes only. It cannot be used in a commercial environment, particularly as part of a commercial product, without written permission. OptiMathSAT is provided as is, without any warranty.

#### URIs (github, websites, etc.):
Project page: https://optimathsat.disi.unitn.it/
Repository with examples using OptiMathSAT's Python API: https://github.com/PatrickTrentin88/omt_python_examples

#### Last commit date:
Last release on download page: 27 September 2021

#### Last publication date:
19 September 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-58942-4_10 (CPAIOR '20)
https://doi.org/10.1007/s10817-018-09508-6 (Journal of Automated Reasoning '18)
https://doi.org/10.1007/978-3-662-54580-5_14 (TACAS '17)
https://doi.org/10.1007/978-3-319-21690-4_27 (CAV '15)

#### Related tools (tools mentioned or compared to in the paper):
Other OMT tools: [[Symba]], [[𝜈𝑍]]

#### Meta
:: Mathematical optimization
:: PV4 :: produces a satisfiability result and a corresponding model, for a formula
:: SMT