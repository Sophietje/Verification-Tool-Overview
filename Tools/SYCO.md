Systematic testing tool for message-passing concurrent programs

#### Name:
SYCO

#### Application domain/field:
Partial-order reduction (POR)
Concurrent programs
Actor programs
Message-passing programs

#### Type of tool (e.g. model checker, test generator):
Testing tool

#### Expected input thing:
ABS program

#### Expected input format:
`.abs` file

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- *Actor programs*: Programs consisting of computing entities called actors. Each actor has its own local state and thread of control. The actors communicate by exchanging messages asynchronously.
- *Partial Order Reduction (POR)*: Algorithms that are based on the idea that some program interleavings can be considered equivalent, and that you only need to explore one interleaving per equivalence class.
- Uses [VeryMax](VeryMax.md)

#### Comments:
-

#### URIs (github, websites, etc.):
Try online: http://costa.fdi.ucm.es/syco/clients/web/

#### Last commit date:
-

#### Last publication date:
January 2021

#### List of related papers:
[Actor-based model checking for Software-Defined Networks](https://doi.org/10.1016/j.jlamp.2020.100617) (Journal of Logical and Algebraic Methods in Programming. Vol. 118, '21)
[Optimal context-sensitive dynamic partial order reduction with observers](https://doi.org/10.1145/3293882.3330565) (ISSTA '19)
[Constrained Dynamic Partial Order Reduction](https://doi.org/10.1007/978-3-319-96142-2_24) (CAV '18)
[Context-Sensitive Dynamic Partial Order Reduction](https://doi.org/10.1007/978-3-319-63387-9_26) (CAV '17)
[Combining Static Analysis and Testing for Deadlock Detection](https://doi.org/10.1007/978-3-319-33693-0_26) (IFM '16)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: PV4 :: provides traces of deadlocks in a concurrent system
:: Concurrency
:: Source :: https://doi.org/10.1145/3550355.3552426