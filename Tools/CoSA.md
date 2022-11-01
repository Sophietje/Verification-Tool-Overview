SMT-based symbolic model checker for hardware design

#### Name:
CoSA: CoreIR Symbolic Analyzer

#### Application domain/field:
Model checking
SMT-based model checking
Hardware design
Bounded model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Input files describing the hardware
- Verification problem (e.g. safety or LTL) or equivalence checking
- *Depending on previous choice you may need to provide*: Property (invariant or LTL property)

#### Expected input format:
It supports many input formats including:
- [CoreIR](Not-verifiers/CoreIR.md)
- [[BTOR2]]
- [Verilog](../Formats/Verilog.md)
- [[SystemVerilog]]
- Symbolic Transition Systems (STS)
- Explicit states Transition Systems (ETS).

Properties can be defined as a parameter or in some of the input formats mentioned above.

#### Expected output:
Depends on the type of analysis that you do with the tool.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
CoSA supports many different analyses/verifications:
- Invariant properties
- LTL properties
- Equivalence checking
- Parametric (Invariant) model checking
- Fault analysis
- Automated lemma extraction
CoSA reduces all analyses to symbolic model-checking problems.

Uses [Yosys](Yosys.md) to support Verilog as input format.
Uses [PySMT](Libraries/PySMT.md), [[PyCoreIR]]

#### Comments:
License: Modified BSD (3-clause BSD) license

#### URIs (github, websites, etc.):
Repository: https://github.com/cristian-mattarei/CoSA

#### Last commit date:
27 October 2020

#### Last publication date:
2 November 2018

#### List of related papers:
[CoSA: Integrated Verification for Agile Hardware Design](https://doi.org/10.23919/FMCAD.2018.8603014) (FMCAD '18)

#### Related tools (tools mentioned or compared to in the paper):
[Pono](Checkers/Pono.md): this tool was developed as the next generation of CoSA.

#### Meta
:: Hardware
:: Model checking
:: LTL
:: PV3 :: checks user-specified properties for hardware designs