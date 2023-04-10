#### Name:
Dartagnan

#### Application domain/field:
Concurrent programs
Weak memory models
Model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
Program (annotated with an assertion over the final states), and the memory model.

#### Expected input format:
- Program: PPC, x86, AArch64 assembly, subset of C11, or own .pts format (all limited to the subsets supported by Herd's .litmus format)
- Assertion in program should be written with the SVCOMP command: `__VERIFIER_assert`
- Memory model: CAT

#### Expected output:
Whether the written assertion holds for the program under the specified memory model

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Dartagnan is a bounded model checker for concurrent programs under weak memory models.
Uses [Z3](../Solvers/SMT/Z3.md).

#### Comments:
**Note:** repository only mentions that it supports programs written in the .litmus or .bpl (Boogie) formats. However, for .bpl files you have to specify the architecture as `none`, `tso`, `power`, `arm` or `arm8`.

#### URIs (github, websites, etc.):
Repository (also contains another tool): https://github.com/hernanponcedeleon/Dat3M

#### Last commit date:
30 Mar 2023 (last activity)

#### Last publication date:
23 March 2021

#### List of related papers:
[BMC for Weak Memory Models: Relation Analysis for Compact SMT Encodings](https://doi.org/10.1007/978-3-030-25540-4_19)
[Dartagnan: Leveraging Compiler Optimizations and the Price of Precision (Competition Contribution)](https://doi.org/10.1007/978-3-030-72013-1_26)

#### Related tools (tools mentioned or compared to in the paper):
Other bounded model checkers: [CBMC](CBMC.md), [Nidhugg](../Nidhugg.md)

#### Meta
:: C
:: PV4 :: checks assertions in a C program within a chosen memory spec
:: Model checking
:: Source :: https://doi.org/10.1145/3550355.3552426
