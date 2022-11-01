Tool for inferring linear, lexicographic-linear and multiphase-linear ranking functions for multipath linear-constraint loops, with variables ranging over the rationals, reals, or integers.

#### Name:
iRankFinder

#### Application domain/field:
Multiphase ranking functions
Loop termination
Ranking function

#### Type of tool (e.g. model checker, test generator):
Termination analyzer? Ranking function finder?

#### Expected input thing:
- Loop
- Choose algorithm that should be used to infer a ranking function

#### Expected input format:
`.mlc` file (own syntax)

#### Expected output:
Ranking function

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This tool extends [[RankFinder]] by adding integers.

**Ranking function**: a function $f$ that maps program states into elements of a well-founded ordered set, such that $f(s) > f(s')$ holds whenever $s'$ follows state $s$. This implies termination since infinite descent in a well-founded order is impossible.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://loopkiller.com/irankfinder/interfaces/web/linrf.php
Project page: http://irankfinder.loopkiller.com:8081/
Repository?: https://github.com/costa-group/iRankFinder
Repository (new implementation?): https://github.com/jesusjda/pyRankFinder

#### Last commit date:
-

#### Last publication date:
13 July 2017

#### List of related papers:
[Multiphase-Linear Ranking Functions and Their Relation to Recurrent Sets](https://doi.org/10.1007/978-3-030-32304-2_22) (SAS '19)
[On Multiphase-Linear Ranking Functions](https://doi.org/10.1007/978-3-319-63390-9_32) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: infers ranking functions for loops