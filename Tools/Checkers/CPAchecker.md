Software verification framework

#### Name:
CPAChecker

#### Application domain/field:
Software verification
Model checking
Software model checking

#### Type of tool (e.g. model checker, test generator):
Model checker?

#### Expected input thing:
- C program
	- CPAChecker will look for labels named `ERROR` (case insensitive) and assertions in the source code file
- Configuration file (there are default configurations available) which indicates what kind of analysis to perform

#### Expected input format:
- *C program*: `.c` file
- *Configuration*: `.properties` file

#### Expected output:
`Verification result:` `FALSE` or `TRUE` or `UNKNOWN` which indicates whether it found a violation of the property/assertion in the program.

HTML report named `Report.html` if the result was `TRUE` or `Counterexample.*.html` if the result was `FALSE`.  You can open these HTML files in a browser to view the analysis results.
The results include things such as a visualization of the control flow, counterexample (if there was an error) and time statistics.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Some techniques that are implemented/available in CPAChecker include:
- Predicate abstraction
- Interpolation-based refinement
- Adjustable-block encoding

Uses [MathSAT](../Solvers/SMT/MathSAT.md), [[CSIsat]], [CBMC](CBMC.md), [[JavaBDD]].

#### Comments:
License: Apache 2.0 License

#### URIs (github, websites, etc.):
Project page: https://cpachecker.sosy-lab.org/
Repository (mirror): https://github.com/sosy-lab/cpachecker
Repository: https://svn.sosy-lab.org/software/cpachecker/trunk/

#### Last commit date:
25 October 2021

#### Last publication date:
November 2020

#### List of related papers:
[Domain-independent interprocedural program analysis using block-abstraction memoization](https://doi.org/10.1145/3368089.3409718) (ESEC/FSE '20)
[CPA-RefSel: CPAchecker with Refinement Selection](https://doi.org/10.1007/978-3-662-49674-9_59) (TACAS '16)
[CPAchecker with Support for Recursive Programs and Floating-Point Arithmetic](https://doi.org/10.1007/978-3-662-46681-0_34) (TACAS '15)
[CPAchecker: A Tool for Configurable Software Verification](https://doi.org/10.1007/978-3-642-22110-1_16) (CAV '11)

#### Related tools (tools mentioned or compared to in the paper):
[[BLAST]]

#### Meta
:: C
:: PV3 :: checks user-specified assertions in C program
:: Source :: https://doi.org/10.1145/3550355.3552426
