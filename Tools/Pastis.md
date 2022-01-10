Tool that computes polynomial resource bounds for imperative integer programs.

#### Name:
Pastis

#### Application domain/field:
Resource-bound analysis
Resource bounds
Resource consumption
Automatic amortized resource analysis (AARA)

#### Type of tool (e.g. model checker, test generator):
Resource bound analyzer

#### Expected input thing:
Imperative integer program

#### Expected input format:
Either written in a minimal (own) imperative language, or LLVM bitcode

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
AARA-based tool for generating polynomial bounds on low-level integer programs with recursive procedures

AARA: automatic amortized resource analysis. A technique that statically derives concrete (non-asymptotic) resource bounds.

The tool accepts a minimal imperative language and LLVM bitcode as input. It supports expressions that are additions, subtractions, and multiplications of constants and program variables. It uses a special random expression for all other operations (such as divisions).

Pastis also automatically generates proof certificates of the validity of its bounds.

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/academic-archive/cav17-pastis

#### Last commit date:
1 July 2021 (this was a single commit, before that the last commit is from 17 June 2017)

#### Last publication date:
13 July 2017

#### List of related papers:
https://doi.org/10.1007/978-3-319-63390-9_4 (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
Resource-bound analyses for integer programs: [[CAMPY]], [[KoAT]], [[Rank]], [[CoFloCo]], [[COSTA]], [[Loopus]]