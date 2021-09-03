Language inclusion solver

#### Name:
RABIT: Ramsey-based Büchi automata inclusion testing

#### Application domain/field:
Büchi automata (BAs)
Language inclusion
Nondeterministic Büchi automata
Nondeterministic finite automata (NFAs)

#### Type of tool (e.g. model checker, test generator):
Property checker/language inclusion solver

#### Expected input thing:
- Two Büchi or nondeterministic automata
- The metagraph $M^I_{A,B}$?

#### Expected input format:
[[BA]] format

#### Expected output:
Returns `TRUE` iff $L(A) \subseteq L(B)$ otherwise `FALSE`

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Language inclusion solver, i.e. it can check language inclusion between Büchi automata, and thus also language equivalence and language universality.

#### Comments:
Checking language inclusion between nondeterministic Büchi automata is computationally hard (PSPACE-complete).

#### URIs (github, websites, etc.):
Project page: http://www.languageinclusion.org/doku.php?id=tools#rabit_and_reduce_v25
Repository: https://github.com/ISCAS-PMC/RABIT

#### Last commit date:
9 January 2019

#### Last publication date:
September 2011

#### List of related papers:
https://doi.org/10.23638/LMCS-15(1:12)2019 (Logical Methods in Computer Science 2019)
https://doi.org/10.1145/2480359.2429079 (POPL 2013)
https://doi.org/10.1007/978-3-642-23217-6_13 (CONCUR 2011)
https://doi.org/10.1007/978-3-642-14295-6_14 (CAV 2010)

#### Related tools (tools mentioned or compared to in the paper):
-