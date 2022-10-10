SMT-based model checker

#### Name:
Pono

#### Application domain/field:
Model checking
Symbolic model checking
SMT-based model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Transition system
- Property to check

#### Expected input format:
One of the following
- Manually built transition system (can use the API to do this)
- [[BTOR2]] format
- (subset of) [nuXmv](nuXmv.md)'s SMT-based theory extension of SMV
- [CoreIR](../Not-verifiers/CoreIR.md)

The authors note that you could also use Verilog, by first using a tool to translate from Verilog to BTOR2 or SMV.

The property is represented as an smt-switch formula.

#### Expected output:
`UNKNOWN` if the result could not be determined, `FALSE` if the property does not hold, `TRUE` if the property holds, or `ERROR` in case of an internal error.
When the property does not hold, then Pono will give a witness trace (either in [[BTOR2]] witness format or the [[VCD]] standard format)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Designed with three use cases in mind:
1. Push-button verification
2. Expert verification
3. Model checker development

The user can ask the tool to attempt to prove the property with or without a bound. If the proof attempt failed then the user can ask for a counterexample trace.If the proof attempt succeeded then Pono can return an inductive invariant that implies the property.
- Uses [smt-switch](../Libraries/smt-switch.md)
- Uses [MathSAT](../Solvers/SMT/MathSAT.md) 5 as an underlying SMT solver and interpolant producer.
- Also uses [Boolector](../Solvers/SMT/Boolector.md) for hardware model checking problems.

#### Comments:
Pono was developed as the next generation of [CoSA](../CoSA.md) and was originally named cosa2.

#### URIs (github, websites, etc.):
Repository: https://github.com/upscale-project/pono

#### Last commit date:
6 November 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[Pono: A Flexible and Extensible SMT-Based Model Checker](https://doi.org/10.1007/978-3-030-81688-9_22) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV3 :: checks a user-specified property for a transition system
:: Hardware
:: Model checking