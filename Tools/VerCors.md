#### Name:
VerCors

#### Application domain/field:
Concurrency
Deductive verification
Auto-active verification

#### Type of tool (e.g. model checker, test generator):
Deductive verifier

#### Expected input thing:
Program annotated with specifications

#### Expected input format:
- Program: C, Java, PVL (own language)
- Specifications: added as annotations (in comments) to the program, written in their own specification language that was inspired by [JML](Formats/JML.md).

#### Expected output:
Whether the program adheres to the specification or not.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
VerCors can be used to verify both functional properties and memory-safety. VerCors aims to verify concurrent and parallel programs.

Two extensions have been built on top of VerCors namely [[Alpinist]] and [[VeyMont]].

Uses [Viper](Tools/Frameworks/Viper.md).

#### Comments:
-

#### URIs (github, websites, etc.):
- Repository: https://github.com/utwente-fmt/vercors
- Project page: https://vercors.ewi.utwente.nl/

#### Last commit date:
16 February 2023
06 Apr 2023 (last activity)

#### Last publication date:
17 October 2022

#### List of related papers:
- [On Deductive Verification of an Industrial Concurrent Software Component with VerCors](https://doi.org/10.1007/978-3-031-19849-6_29) (ISoLA '22)
- [Modular Transformation of Java Exceptions Modulo Errors](https://doi.org/10.1007/978-3-030-85248-1_5) (FMICS '21)
- [Practical Abstractions for Automated Verification of Shared-Memory Concurrency](https://doi.org/10.1007/978-3-030-39322-9_19) (VMCAI '20)
- [An Exercise in Verifying Sequential Programs with VerCors](https://doi.org/10.1145/3236454.3236479) (ISSTA '18)
- [The VerCors Tool Set: Verification of Parallel and Concurrent Software](https://doi.org/10.1007/978-3-319-66845-1_7) (IFM '17)
- [VerCors: A Layered Approach to Practical Verification of Concurrent Software](https://doi.org/10.1109/PDP.2016.107) (PDP '16)
- [The VerCors Tool for Verification of Concurrent Systems](https://doi.org/10.1007/978-3-319-06410-9_9) (FM '14)
- [The VerCors project: setting up basecamp](https://doi.org/10.1145/2103776.2103785) (PLPV '12)

#### Related tools (tools mentioned or compared to in the paper):
Other deductive verifiers for C/Java: [Verifast](Tools/Verifast.md), [OpenJML](OpenJML), [KeY](Tools/Provers/KeY.md)
Other verifiers that use [Viper](Tools/Frameworks/Viper.md): [Gobra](Tools/Gobra.md), [Nagini](Tools/Nagini.md), [[Prusti]], [[2vyper]]

#### Meta
:: Concurrency
:: Java
:: C
:: PV4 :: verifies user-written properties and memory-safety for a program
:: Source :: requested by the VerCors team
