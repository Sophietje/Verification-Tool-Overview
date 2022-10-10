Given a program (in a simple imperative language), where a hyperproperty is encoded using an *assume* statement, it attempts to prove the property.

#### Name:
Weaver

#### Application domain/field:
Hypersafety properties
Reduction
Counterexample-guided abstraction refinement (CEGAR)

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:
- Program
- Hyperproperty

#### Expected input format:
- *Program*: simple imperative language
- *Hyperproperty*: encoded in the program with *assume* statements

#### Expected output:
`SUCCESS` or `FAILURE`. In case of `FAILURE` it will also provide a counterexample.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
*Hypersafety property*: A property that describes the set of valid interrelations between multiple finite runs of a program.
*k-safety property*: safety property whose violation is witnessed by at least k finite runs of a program.

Weaver reduces verification of k-safety properties to verification of 1-safety properties. As a result, it is then possible to use existing safety verification techniques.

Uses [Z3](Solvers/SMT/Z3.md),  [MathSAT](Solvers/SMT/MathSAT.md), [Yices](Solvers/SMT/Yices.md), [CVC4](Solvers/SMT/CVC4.md).

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/weaver-verifier/weaver

#### Last commit date:
25 February 2021

#### Last publication date:
12 July 2019

#### List of related papers:
[Reductions for safety proofs](https://doi.org/10.1145/3371081) (POPL '20)
[Automated Hypersafety Verification](https://doi.org/10.1007/978-3-030-25540-4_11) (CAV '19)

#### Related tools (tools mentioned or compared to in the paper):
[Synonym](Synonym.md): checks k-safety properties of Java programs

#### Meta
:: PV3 :: checks user-specified k-safety properties for programs in a simple imperative language