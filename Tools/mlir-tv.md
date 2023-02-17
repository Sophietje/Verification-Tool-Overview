
#### Name:
mlir-tv

#### Application domain/field:
Machine learning compilers
Compilers
Translation validation
Multi-Level IR (MLIR)

#### Type of tool (e.g. model checker, test generator):
Translation validator

#### Expected input thing:
Two MLIR functions of identical signatures. One before compiler optimisations and one after compiler optimisations.

#### Expected input format:
`.mlir` files

#### Expected output:
Whether the compiler transformation is correct or incorrect.
If it is incorrect then it will also find a counterexample.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This is a translation validation framework for Multi-Level IR.
Multi-Level IR (MLIR) is a framework for supporting the development of domain-specific compilers by sharing intermediate representations (IRs).
Translation validation aims to check whether a compilation is correct by looking at the input (source program) and output (target program).

`mlir-tv` specifically targets intraprocedural transformations, i.e. functions in the two programs with the same signature are checked pairwisely.

Uses [Z3](../../Tools/Solvers/SMT/Z3.md)

#### Comments:
-

#### URIs (github, websites, etc.):
- Artifact: https://doi.org/10.5281/zenodo.6556379
- Repository: https://github.com/aqjune/mlir-tv

#### Last commit date:
24 October 2022

#### Last publication date:
6 August 2022

#### List of related papers:
[SMT-Based Translation Validation for Machine Learning Compiler](https://doi.org/10.1007/978-3-031-13188-2_19) (CAV 2022)

#### Related tools (tools mentioned or compared to in the paper):
Tools for translation validation of LLVM transformations: [Alive2](../../Tools/Alive2.md), [[LLVM-MD]], [[Peggy]].

#### Meta
:: Compiler
:: PV1 :: checks correctness of transformations for MLIR
:: Source :: https://doi.org/10.1007/978-3-031-13188-2