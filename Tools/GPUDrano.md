Static analysis tool to detect uncoalesced global memory accesses in CUDA programs

#### Name:
GPUDrano, sometimes stylized as GPU Drano

#### Application domain/field:
Graphics Processing Units (GPUs)
Static analysis
Uncoalesced memory accesses
Performance bugs
Dataflow analysis
Abstract interpretation

#### Type of tool (e.g. model checker, test generator):
Bug detector?

#### Expected input thing:
LLVM IR

#### Expected input format:
`.ll` file(s)

#### Expected output:
GPUDrano will report all accesses that might be uncoalesced for each GPU kernel.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Load and store instructions that reference the GPU's global memory, should obey a certain structure to ensure optimal performance. If not, it might result in underutilization and performance problems.
GPUDrano tries to find uncoalesced accesses. Uncoalesced memory accesses occur when the the memory accesses are not contained within a single cache block.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/upenn-acg/gpudrano-static-analysis_v1.0

#### Last commit date:
16 November 2018

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63387-9_25 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
[[GKLEE]], [[PUG]]

#### Meta
:: CUDA
:: PV1 :: detects uncoalesced memory accesses in CUDA programs