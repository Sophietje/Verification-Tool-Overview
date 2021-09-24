Tool that computes polynomial resource bounds for imperative integer programs.

AARA-based tool for generating polynomial bounds on low-level integer programs with recursive procedures

AARA: automatic amortized resource analysis. A technique that statically derives concrete (non-asymptotic) resource bounds.

The tool accepts a minimal imperative language and LLVM bitcode as input. It supports expressions that are additions, subtractions, and multiplications of constants and program variables. It uses a special random expression for all other operations (such as divisions).

Repository: https://github.com/academic-archive/cav17-pastis (last commit 1 July 2021, this is a single commit, before that the last commit is from 17 June 2017)