#### Name:
𝜏-DIGITS

#### Application domain/field:
Program synthesis
Probabilistic synthesis
Distribution-guided inductive synthesis (DIGITS)
Sketch-based synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
Program sketch consisting of:
- a program written in a loop-free language with "holes". These "holes" represent some constant terminals in expressions.
- Precondition?
- Postcondition: Boolean probabilistic correctness property

#### Expected input format:
- *Program sketch*: `.fr` file where the program is defined in a method `D(args)`. Holes can be indicated with `Hole(...)`
- *Postcondition*: in a method `post(Pr)` in the same `.fr` file
- *Precondition*: in a method `pre()` in the same `.fr` file

#### Expected output:
Instantiations for the holes in the program.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The algorithm roughly follows the following steps to reduce the problem of probabilistic synthesis to non-probabilistic synthesis:
1. Approximate the input probability distribution with a finite sample set
2. Synthesize a program for various possible output assignments of the finite sample set
3. Invoke a probabilistic verifier to check if one of the synthesized programs adheres to the given specification.

As a back-end, you can use [Z3](Solvers/SMT/Z3.md) and [CVC4](Solvers/SMT/CVC4.md).

𝜏-DIGITS is an improved version of [DIGITS](DIGITS.md). It reduces the number of synthesis queries performed by the algorithm.

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Repository: https://github.com/sedrews/digits

#### Last commit date:
14 Oct 2019 (default branch)
14 Oct 2019 (last activity)

#### Last publication date:
12 July 2019

#### List of related papers:
[Efficient Synthesis with Probabilistic Constraints](https://doi.org/10.1007/978-3-030-25540-4_15) (CAV '19)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV2 :: fill holes a given loop-free program from a probabilistic specification of its desired behaviour
:: Probabilistic
:: Source :: https://doi.org/10.1145/3550355.3552426
