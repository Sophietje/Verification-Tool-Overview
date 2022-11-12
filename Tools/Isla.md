Tool to evaluate relaxed-memory behaviour of instruction set architectures w.r.t. arbitrary axiomatic memory models

#### Name:
Isla

#### Application domain/field:
Instruction-set architecture (ISA) semantics
Concurrency models
Relaxed-memory concurrency models
Processor architecture
Symbolic execution

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Architecture (e.g. `aarch64.ir`)
- Configuration file that defines e.g. the initial state (`.toml` file)
- Memory model specified in the Cat language (`.cat` file)

#### Expected input format:
- *Architecture*: Pre-compiled Sail representation, `.ir` file. For some architectures compiled SAIL snapshots are available via https://github.com/rems-project/isla-snapshots
- *Configuration file*: `.toml` file
- Model: [Cat language](http://diy.inria.fr/doc/herd.html#herd%3Alanguage), `.cat` file

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
License: BSD 2-Clause

#### URIs (github, websites, etc.):
Try online: https://isla-axiomatic.cl.cam.ac.uk/
Repository: https://github.com/rems-project/isla
Documentation: https://github.com/rems-project/isla/blob/master/doc/axiomatic.adoc

#### Last commit date:
14 December 2021

#### Last publication date:
15 July 2021

#### List of related papers:
[Isla: Integrating Full-Scale ISA Semantics and Axiomatic Concurrency Models](https://doi.org/10.1007/978-3-030-81685-8_14) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Concurrency
:: Binary level
:: PV2 :: generates a state graph or a test case from an architecture spec
:: Source :: https://doi.org/10.1145/3550355.3552426