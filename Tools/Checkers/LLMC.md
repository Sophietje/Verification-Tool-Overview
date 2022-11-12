Multi-core explicit-state model checker of multi-threaded LLVM IR.

#### Name:
LLMC: Low-Level Model Checker

#### Application domain/field:
Model checking
Multi-threaded
High-performance software

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- LLVM IR of a program (with assertions)
- Use single or multicore (with a single queue or with work-sharing) model checker (`singlecore_simple`, `multicore_simple`, `multicore_bitbetter`)
- How to store states (`dtree`, `treedbsmod`, `treedbs_cchm`, `cchm` or `stdmap`)
- Number of threads to use

#### Expected input format:
LLVM IR file, the rest are parameters when calling the tool via the command line.

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [[DMC]] (model checker)

#### Comments:
License: GNU General Public License 3.0

#### URIs (github, websites, etc.):
Repository: https://github.com/bergfi/llmc

#### Last commit date:
1 June 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[LLMC: Verifying High-Performance Software](https://doi.org/10.1007/978-3-030-81688-9_32)  (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to: [DIVINE](../DIVINE.md), [Nidhugg](../Nidhugg.md)

#### Meta
:: LLVM
:: Concurrency
:: PV3 :: checks assertions in a multi-threaded program
:: Model checking
:: Source :: https://doi.org/10.1145/3550355.3552426
