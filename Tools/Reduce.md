Büchi automata minimization tool

#### Name:
Reduce

#### Application domain/field:
Büchi automata
Nondeterministic finite automata
Automata minimization

#### Type of tool (e.g. model checker, test generator):
Automata translator?

#### Expected input thing:
Büchi automaton (BA) or nondeterministic finite automaton (NFA)

#### Expected input format:
[[BA]] format

#### Expected output:
Minimized automaton?

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Reduce can be invoked with *one* of the following options:
- `-light`  to use the Light-k method
- `-nojump` to use the Heavy-k method
- `-pebble` uses a 2-pebble simulation (tends to be slow in practice)
- `-sat` might create an automaton with fewer states, possibly with more transitions

By default Reduce will reduce Büchi automata. You can switch to NFA semantics by using the option `-finite`.


#### Comments:
-

#### URIs (github, websites, etc.):
Repository (Reduce is packaged with [RABIT](RABIT.md)): https://github.com/ISCAS-PMC/RABIT

#### Last commit date:
9 January 2019

#### Last publication date:
January 2013

#### List of related papers:
https://doi.org/10.1145/2480359.2429079 (POPL 2013)

#### Related tools (tools mentioned or compared to in the paper):
Seems to be bundled with [RABIT](RABIT.md)