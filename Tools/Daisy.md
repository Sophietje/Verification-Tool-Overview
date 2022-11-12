#### Name:
Daisy

#### Application domain/field:
Program approximation
Performance optimization
Synthesis

#### Type of tool (e.g. model checker, test generator):
Performance optimizer

#### Expected input thing:
- Floating-point program with elementary function calls (e.g. `sin`, `exp
- Domains of all inputs
- Target overall absolute error

#### Expected input format:
Input file (one single file) should follow the structure:
```scala
  import daisy.lang._
  import Real._

  object TestObject {

    def function1(x: Real): Real \= {
      require(0 <= x && x <= 1)

      val z \= x + x
      z \* x

    } ensuring(res \=> res +/- 1e-5)

    def function2 ...
  }
  ```
The repository has some more details 

#### Expected output:
Optimized program in Scala or C with the guaranteed error below the specified target error

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Framework for verifying and optimizing numerical programs.
Given a program it provides an efficient implementation for floating-point programs with elementary function calls.
Uses [Z3](Solvers/SMT/Z3.md), [dReal](Solvers/SMT/dReal.md), [MPFR](Libraries/MPFR.md), [[Metalibm]]

#### Comments:

#### URIs (github, websites, etc.):
Repository: https://github.com/malyzajko/daisy
Documentation: https://github.com/malyzajko/daisy/blob/master/doc/documentation.md

#### Last commit date:
12 February 2021

#### Last publication date:
12 July 2019

#### List of related papers:
[Sound Approximation of Programs with Elementary Functions](https://doi.org/10.1007/978-3-030-25543-5_11) (CAV '19)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Floating point
:: Performance
:: Synthesis
:: Scala
:: C
:: PV2 :: synthesises a Scala or C program where performance of floating-point operations are optimised
:: Source :: https://doi.org/10.1145/3550355.3552426