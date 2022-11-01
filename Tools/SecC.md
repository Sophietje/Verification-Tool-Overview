"A prototype program verification tool for proving information flow security of C code."

#### Name:
SecC

#### Application domain/field:
Software verification
Information flow properties
Security verification

#### Type of tool (e.g. model checker, test generator):
Deductive verifier? Auto-active verifier?

#### Expected input thing:
- Program
- Information flow property (assertions in SecCSL)

#### Expected input format:
C file

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
An automatic verifier (for a subset of C) for SecCSL. 
SecCSL (Security Concurrent Separation Logic) is used to specify data-dependent information flow security properties of low-level programs.
SecC reasons about a program using symbolic execution, similar to [Verifast](Verifast.md) and [Viper](Frameworks/Viper.md).

#### Comments:
The underlying logic, SecCSL, has been proven sound with [Isabelle/HOL](Provers/Isabelle-HOL.md).

#### URIs (github, websites, etc.):
Project page: https://covern.org/secc/
Repository: https://bitbucket.org/covern/secc

#### Last commit date:
29 March 2021

#### Last publication date:
12 July 2019

#### List of related papers:
[SecCSL: Security Concurrent Separation Logic](https://doi.org/10.1007/978-3-030-25543-5_13) (CAV 2019)

#### Related tools (tools mentioned or compared to in the paper):
-

#### Meta
:: Security
:: PV3 :: checks user-specified information flow properties of C code