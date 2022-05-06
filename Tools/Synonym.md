Prototype for verifying k-safety properties of Java programs

#### Name:
Synonym

#### Application domain/field:
Relational verification
Relational specifications
Safety verification

#### Type of tool (e.g. model checker, test generator):
Relational verifier

#### Expected input thing:
- Program
- Reference to property that should be verified
- Tool that should be used for verification

#### Expected input format:
- *Program*: Java file
- *Property to be verified*: a number that is passed as an argument. The number indicates which property from `Properties.hs` to check
- *Tool for verification*: passed as an argument: `descartes`, `syn`, or `synonym`

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
*Relational specifications*: Specifications that can describe multiple runs of the same program or relate the behaviors of multiple programs.
*k-safety properties* are relational verification problems over k identical Java programs.

Built on top of [[Descartes]]

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/lmpick/synonym

#### Last commit date:
15 December 2018

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_9 (CAV '18)

#### Related tools (tools mentioned or compared to in the paper):
Tools for relational verification: [[Rosette/Unbound]], [[VeriMapRel]], [[Reve]], [[MoCHi]], [[SymDiff]]

#### Meta
:: PV3 :: checks user-specified k-safety properties for Java programs
:: Java