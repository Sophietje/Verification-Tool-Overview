Black-box framework that runs multiple parallel instances of a SyGuS (syntax-guided synthesis) tool with different grammars

#### Name:
PLearn

#### Application domain/field:
Syntax-guided synthesis (SyGuS)
Counterexample-guided inductive synthesis (CEGIS)

#### Type of tool (e.g. model checker, test generator):
? Synthesis tool? Metatool?

#### Expected input thing:
- Synthesis tool
- SyGuS problem
- Subgrammars $\mathcal{E}_1..p$ such that $\mathcal{E}_i \subseteq \mathcal{E}$

#### Expected input format:
?

#### Expected output:
First solution that was found or $\bot$ if no solution could be found.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The idea behind the tool is that SyGuS tools are sensitive to the choice of grammar. Sometimes increasing the grammar expressiveness allows the tool to solve some problems that are unsolvable with less expressive grammars. However, it is possible that the tool can no longer solve some problems that could be solved with less expressive grammars.

#### Comments:
-

#### URIs (github, websites, etc.):
Artifact of CAV '19 paper: https://github.com/SaswatPadhi/2019_CAV_Artifact_100

#### Last commit date:
-

#### Last publication date:
12 July 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-25540-4_17 (CAV '19)

#### Related tools (tools mentioned or compared to in the paper):