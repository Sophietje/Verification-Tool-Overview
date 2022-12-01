#### Name:
AliveInLean

#### Application domain/field:
Compilers
Compiler optimizations

#### Type of tool (e.g. model checker, test generator):
Compiler optimization verifier

#### Expected input thing:
Optimization pattern. This pattern describes what 'pattern' should be matched in the LLVM, and what the result should be (i.e. how it should be rewritten).

Example *(Source: "AliveInLean: A Verified LLVM Peephole Optimization Verifier" by J. Lee et al. (2019)*):
![[Screenshot 2021-05-31 at 10.41.14.png]]

#### Expected input format:
Domain-specific language

#### Expected output:
Whether the compiler optimization is correct

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Has been verified/implemented with the [[Lean]] theorem prover.
Uses a verification condition (VC) generator. The VCs are discharged using an SMT solver ([Z3](Solvers/SMT/Z3.md)).

The correctness of the optimization is checked by the following 3 things:
1. The target is defined when the source is defined
2. The target is poison-free when the source is poison-free
3. The source and target produce the same result when the source is defined and poison-free

#### Comments:
*Goal of the tool*: Developers can check the correctness of compiler optimizations.

#### URIs (github, websites, etc.):
https://sf.snu.ac.kr/aliveinlean/
https://github.com/microsoft/aliveinlean

#### Last commit date:
13 Aug 2022 (default branch)
13 Aug 2022 (last activity)

#### Last publication date:
12 July 2019

#### List of related papers:
[AliveInLean: A Verified LLVM Peephole Optimization Verifier](https://doi.org/10.1007/978-3-030-25543-5_25)

#### Related tools (tools mentioned or compared to in the paper):
AliveInLean is a re-implemented/-engineered version of [[Alive]], a tool for verifying LLVM's peephole optimizations. This has been done because Alive itself was not verified.

#### Meta
:: Compiler
:: PV1 :: verifies its own expectations of a given compiler optimisation
:: Source :: https://doi.org/10.1145/3550355.3552426
