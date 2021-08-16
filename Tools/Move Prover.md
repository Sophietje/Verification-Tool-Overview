#### Name:
Move Prover

#### Application domain/field:
Deductive verification
Auto-active verification
Blockchain
Smart contracts

#### Type of tool (e.g. model checker, test generator):
Auto-active verifier/deductive verifier

#### Expected input thing:
Move source code annotated with specifications (pre-/postconditions).

#### Expected input format:
- *Source code*: Move source code
- *Specifications*: own specification language

#### Expected output:
Whether the specification holds or some kind of source-level diagnosis/error.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The Move Prover translates annotated Move source code to the [[Boogie]] intermediate language. [[Boogie]] then generates an SMT formula which can be checked using an SMT solver such as [[Z3]] or [[CVC4]].

"Move" is a language for implementing transactions, i.e. smart contracts, on the Libra blockchain.

The Move Prover seems to be an auto-active verifier though this is not mentioned in the paper.

#### Comments:
-

#### URIs (github, websites, etc.):
Code repository? (Has a different name but is linked in the paper): https://github.com/diem/diem

#### Last commit date:
14 August 2021

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_7

#### Related tools (tools mentioned or compared to in the paper):