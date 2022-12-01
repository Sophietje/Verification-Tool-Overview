#### Name:
Dafny

#### Application domain/field:
Symbolic execution
Functional correctness
SMT-based verifier

#### Type of tool (e.g. model checker, test generator):
Auto-active verifier/Deductive verifier

#### Expected input thing:
Program and specifications

#### Expected input format:
Dafny language

#### Expected output:
Errors if the program violates a rule of the language or if the program violates the specification.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Dafny is an SMT-based automatic program verifier. It can be used to prove functional correctness of programs. It does not require any user interaction with the solver, but the user does need to write specifications. Dafny will report errors if the program may violate a rule of the language (e.g. index bounds error) or if the program violates the specification (e.g. postcondition not established).

Dafny will translate the given program (and specifications) into the verification language [Boogie](Frameworks/Boogie.md). Boogie will generate verification conditions based on the program, which are passed to an SMT solver (specifically [Z3](Solvers/SMT/Z3.md)).

*Dafny* is used to describe both the *verifier* and the *language* that it uses.

Specifications are written in the form of preconditions, postconditions, invariants, ghost code, frame conditions, and more.

#### Comments:
License: MIT license

There is a VSCode plugin for Dafny: [Repository](https://github.com/dafny-lang/ide-vscode) [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=correctnessLab.dafny-vscode)

#### URIs (github, websites, etc.):
Project page: https://www.microsoft.com/en-us/research/project/dafny-a-language-and-program-verifier-for-functional-correctness/
Documentation: https://dafny-lang.github.io/dafny/
Repository: https://github.com/dafny-lang/dafny

#### Last commit date:
30 Nov 2022 (default branch)
01 Dec 2022 (last activity)

#### Last publication date:
2018

#### List of related papers:
[Modular Verification Scopes via Export Sets and Translucent Exports](https://doi.org/10.1007/978-3-319-98047-8_12) (Principled Software Development '18)
[Modeling Concurrency in Dafny](https://doi.org/10.1007/978-3-030-02928-9_4) (SETSS '17)
[Accessible Software Verification with Dafny](https://doi.org/10.1109/MS.2017.4121212) (IEEE Software '17)
[Trigger Selection Strategies to Stabilize Program Verifiers](https://doi.org/10.1007/978-3-319-41528-4_20) (CAV '16)
[Integrated Environment for Diagnosing Verification Errors](https://doi.org/10.1007/978-3-662-49674-9_25) (TACAS '16)
[Compiling Hilbert's epsilon operator](https://doi.org/10.29007/rkxm) (LPAR '15)
[Developing verified programs with Dafny](https://doi.org/10.1109/ICSE.2013.6606754) (ICSE '13)
[Dafny: An Automatic Program Verifier for Functional Correctness](https://doi.org/10.1007/978-3-642-17511-4_20) (LPAR '10)

#### Related tools (tools mentioned or compared to in the paper):
Other auto-active verifiers (i.e. verifiers where the user has no interaction with the solver): [[Spec#]], [Frama-C](Frameworks/Frama-C.md), [SPARK](SPARK.md), [[AutoProof]].

#### Meta
:: PV4 :: checks user-specified annotations and languages' rules for a Dafny program
:: Source :: https://doi.org/10.1145/3550355.3552426
