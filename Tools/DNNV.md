Framework that standardizes input and output formats, includes a DSL for specifying deep neural network (DNN) properties and provides simplification and reduction operations to facilitate the application, development and comparison of DNN verifiers.

#### Name:
DNNV: Deep Neural Network Verification

#### Application domain/field:

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
- Properties
- Neural network
- Verifier that should be used

#### Expected input format:
- *Prroperties*: specified in their own property DSL (`.prop` file) called DNNP
- *Neural network*: Can be defined in the `.prop` file, in the [ONNX](ONNX.md) format
- *Verifier to be used*: defined as a parameter when calling the DNNV tool

#### Expected output:
`sat` if the property was falsified, `unsat` if the property was proven to hold, `unknown` if the verifier is incomplete and could not prove the property, or `error` if there was an error.

If the result was `sat`, indicating that a violation of the property was found, then DNNV also returns a counterexample.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Supports the following verifiers: [Reluplex](Reluplex.md), [[planet]], [[MIPVerify.jl]], [Neurify](Neurify), [[ERAN]], [[PLNN]], [Marabou](Marabou.md), [nnenum](nnenum.md), [[verinet]]

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/dlshriver/DNNV
Documentation: https://dnnv.readthedocs.io/
Artifact for CAV '21 paper: https://doi.org/10.5281/zenodo.4883626

#### Last commit date:
5 October 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_6 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [[VNNLIB]] and [[SOCRATES]]
