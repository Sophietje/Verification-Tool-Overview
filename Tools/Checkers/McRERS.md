#### Name:
McRERS

#### Application domain/field:
Model checking
Interruptible properties
Stutter-invariant properties
Partial order reduction
Concurrent systems

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- LTS (as a parallel composition)
- LTL formula to check

#### Expected input format:
- *LTS*: Graphviz dot file
- *LTL formula*: text file

#### Expected output:
Text file with the results. 
It will contain a summary of the results at the end which indicates how many results were right, wrong or unknown (and the time taken).

#### Internals (tools used, frameworks, techniques, paradigms, ...):
The tool seems to have a 'property analyzer' which can be used to determine whether a property is interruptible. This model checker is meant to be used for checking interruptible properties.

This tool uses the same semantics for LTSs, LTL, and satisfiability as the RERS (verification competition/challenge).

It uses the [[Spot]] library to determine equivalence of LTL formulas, determine language equivalence of BAs (Büchi automata), and to convert LTL formula to BA.

#### Comments:

#### URIs (github, websites, etc.):
Artifact (CAV 2020): https://vsl.cis.udel.edu/cav2020/

#### Last commit date:
?

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53291-8_6

#### Related tools (tools mentioned or compared to in the paper):