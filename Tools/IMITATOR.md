Tool for automated parameter synthesis for concurrent timed systems

#### Name:
IMITATOR: Inverse Method for Inferring Time Abstract behavior

#### Application domain/field:
Parametric verification
Real-time systems
Safety analysis
Reachability analysis
Model checking
Parameter synthesis
Timed automata

#### Type of tool (e.g. model checker, test generator):
Model checker?

#### Expected input thing:
- Network of IMITATOR parametric timed automata (NIPTA)
- Property to check

#### Expected input format:
Own syntax/input language (`.imi` file)
Property should be in a separate file (`.imiprop` file)

#### Expected output:
? (depends on what analysis is done with the tool)

#### Internals (tools used, frameworks, techniques, paradigms, ...):
IMITATOR implements the following algorithms:
- On-the-fly computation of the parametric state space
- Parametric reachability or safety analysis
- Minimal-time reachability synthesis
- parametric deadlock freeness checking
- Parametric loop synthesis, and non-Zeno loop synthesis
- Robustness analysis
- Behavioral cartography algorithm
- PRP and PRPC

Uses [Parma Polyhedra Library (PPL)](Libraries/Parma%20Polyhedra%20Library%20(PPL).md)

#### Comments:
License: GPL v3

#### URIs (github, websites, etc.):
Project page: https://www.imitator.fr/
Repository: https://github.com/imitator-model-checker/imitator/

#### Last commit date:
3 November 2021 (also date of last release)

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_26 (CAV '21)
https://doi.org/10.1007/978-3-030-17465-1_12 (TACAS '19)
https://doi.org/10.1007/978-3-642-32759-9_6 (FM '12)
https://doi.org/10.1007/978-3-642-03466-4_22 (ICTAC '09)

#### Related tools (tools mentioned or compared to in the paper):
[[HyMITATOR]], extension of IMITATOR for parameter synthesis on hybrid systems.

#### Meta
:: Automaton