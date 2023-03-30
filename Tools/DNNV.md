Framework that standardizes input and output formats, includes a DSL for specifying deep neural network (DNN) properties and provides simplification and reduction operations to facilitate the application, development and comparison of DNN verifiers.

#### Name:
DNNV: Deep Neural Network Verification

#### Application domain/field:
Deep neural network (DNN)
DNN verification

#### Type of tool (e.g. model checker, test generator):
Framework?

#### Expected input thing:
- Properties
- Neural network
- Verifier that should be used

#### Expected input format:
- *Properties*: specified in their own property DSL (`.prop` file) called DNNP
- *Neural network*: Can be defined in the `.prop` file, in the [ONNX](../Formats/ONNX.md) format
- *Verifier to be used*: defined as a parameter when calling the DNNV tool

#### Expected output:
`sat` if the property was falsified, `unsat` if the property was proven to hold, `unknown` if the verifier is incomplete and could not prove the property, or `error` if there was an error.

If the result was `sat`, indicating that a violation of the property was found, then DNNV also returns a counterexample.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Supports the following verifiers: [Reluplex](Solvers/SMT/Reluplex.md), [[planet]], [[MIPVerify.jl]], [[Neurify]], [ERAN](ERAN.md), [[PLNN]], [Marabou](Marabou.md), [nnenum](nnenum.md), [[verinet]]

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/dlshriver/DNNV
Documentation: https://dnnv.readthedocs.io/
Artifact for CAV '21 paper: https://doi.org/10.5281/zenodo.4883626

#### Last commit date:
27 Mar 2023 (last activity)

#### Last publication date:
15 July 2021

#### List of related papers:
[DNNV: A Framework for Deep Neural Network Verification](https://doi.org/10.1007/978-3-030-81685-8_6) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [[VNNLIB]] and [[SOCRATES]]

#### Meta
:: DNN
:: Neural network
:: PV3 :: verifies if a given property holds for a given neural network according to a given verifier
:: Source :: https://doi.org/10.1145/3550355.3552426
