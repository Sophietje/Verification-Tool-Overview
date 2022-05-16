#### Name:
Termite

#### Application domain/field:

#### Type of tool (e.g. model checker, test generator):

#### Expected input thing:

#### Expected input format:

#### Expected output:

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Uses [[LLVM]] and Clang as frontend
- Uses [[PAGAI]] as an invariant generator
- Uses [[z3overlay]] bindings for type-safe connection to [[Z3]]
- Uses [[LLVM2SMT]] to convert a program to a transition relation

#### Comments:
This is admittedly one of the most complex tools on PV1, but it really works fully automatically and does not require/tolerate user input at any stage besides providing the program to work on.

#### URIs (github, websites, etc.):
Project page: http://termite-analyser.github.io/
Repository: https://github.com/termite-analyser/termite
Demo/comparison: http://termite-analyser.github.io/results/results.html

#### Last commit date:
21 April 2018

#### Last publication date:

#### List of related papers:
https://doi.org/10.1145/2737924.2737976 (PLDI 2015)

#### Related tools (tools mentioned or compared to in the paper):
Compared to [[Loopus]], [[RanK]], [[AProVE]], 

#### Meta
:: C
:: LLVM
:: PV1 :: computes a ranking function for a given program