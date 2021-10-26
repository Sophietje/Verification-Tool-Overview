COMPASS is an international research effort aiming to ensure system-level correctness, safety, dependability and performability of on-board computer-based aerospace systems

COMPASS 3.0 brings together the results of various development projects since the original inception of COMPASS (this says nothing)

#### Name:
COMPASS: Correctness, Modeling and Performance of Aerospace Systems

#### Application domain/field:
Aerospace systems
Model checking

#### Type of tool (e.g. model checker, test generator):
Framework

#### Expected input thing:
- Model
- Properties

#### Expected input format:
[[SLIM]] language (dialect of [[AADL]])
http://www.compass-toolset.org/docs/slim-specification.pdf

#### Expected output:
Depends on the tool/back-end that is used to analyze the model.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The provided model is internally converted into a symbolic model and to a Markov chain. Properties are automatically translated into temporal logic formulas. COMPASS then provides many different ways to analyse these model/properties such as:
- [nuXmv](nuXmv.md) for correctness checking
- [[OCRA]] for contract-based analysis
- [[IMCA]] and [MRMC](MRMC) for performance analysis by probabilistic model checking
- [[slimsim]] for statistical model checking
- [xSAP](xSAP) for safety analysis

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://www.compass-toolset.org/

#### Last commit date:
Last release date: October 2019

#### Last publication date:
4 April 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-17462-0_25 (TACAS '19)

#### Related tools (tools mentioned or compared to in the paper):
