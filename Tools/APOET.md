Program analyser based on abstract unfoldings.

#### Name:
APOET

#### Application domain/field:
Abstract interpretation
Concurrent programs

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Concurrent C program that uses the POSIX thread library
- Parameters to control the widening level and the use of cutoffs

#### Expected input format:
?

#### Expected output:
?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The exploration strategy in this tool is based on [POET](Checkers/POET.md). 

#### Comments:
Note that the author calls "APOET" the second version of "[POET](Checkers/POET.md)".

#### URIs (github, websites, etc.):
Repository (CAV '17 release): https://github.com/marcelosousa/poet/tree/RELEASE-CAV-2017
Repository (of [POET](POET.md)): https://github.com/marcelosousa/poet

#### Last commit date:
marcelosousa/poet: 19 Oct 2018 (default branch)
marcelosousa/poet: 19 Oct 2018 (default branch)
19 Oct 2018 (last activity)

#### Last publication date:
13 July 2017

#### List of related papers:
[Abstract Interpretation with Unfoldings](https://doi.org/10.1007/978-3-319-63390-9_11) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
[[AstreeA]], [[Impara]], [[CBMC]]

#### Meta
:: C
:: Concurrency
:: Haskell
:: PV1 :: analyses a multi-threaded program to see if it conforms to expectations of the tool
:: Source :: https://doi.org/10.1145/3550355.3552426
