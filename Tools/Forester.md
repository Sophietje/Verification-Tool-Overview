#### Name:
Forester

#### Application domain/field:
Shape analysis
Forest automata (FAs)
Model checking
Reachability analysis
Symbolic execution
Heap

#### Type of tool (e.g. model checker, test generator):
Model checker?

#### Expected input thing:
- Program
- LTL properties to check
- Output file for the witness

#### Expected input format:
- *Program*: C code
- *Properties*: `.prp` file, as used in SV-COMP
- *Output file for witness*: filename to which the witness will be written, passed as parameter

#### Expected output:
`TRUE`, `FALSE` or `UNKNOWN`.
It will also generate a violation/correctness witness as an automaton in GraphML.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
-

#### Comments:
License: GPLv3

#### URIs (github, websites, etc.):
Project page: https://www.fit.vutbr.cz/research/groups/verifit/tools/forester/
Repository: https://github.com/martinhruska/forester/

#### Last commit date:
21 July 2013

#### Last publication date:
31 March 2017

#### List of related papers:
[
      Forester: From Heap Shapes to Automata Predicates](https://doi.org/10.1007/978-3-662-54580-5_24) (TACAS '17)
[Run Forester, Run Backwards!](https://doi.org/10.1007/978-3-662-49674-9_61) (TACAS '16)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV3 :: checks user-specified property for a C program
:: C
:: LTL