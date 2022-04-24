Translates MITL (Metric Interval Temporal Logic) into timed automata

#### Name:
MightyL

#### Application domain/field:
Metric Interval Temporal Logic (MITL)
Real-time systems
Automata
Timed automata

#### Type of tool (e.g. model checker, test generator):
Logic-to-automata translator

#### Expected input thing:
MITL formula

#### Expected input format:
?

#### Expected output:
Automata equivalent to the MITL formula in [UPPAAL](Frameworks/UPPAAL.md) XML format.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Metric Interval Temporal Logic (MITL) is an extension of LTL that can be used to characterise real-time properties of computer systems.

After using MightyL, you can then use model checkers such as [UPPAAL](Frameworks/UPPAAL.md) or [[LTSMin]] on the output produced by MightyL.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://www.ulb.ac.be/di/verif/mightyl (seems unreachable)

#### Last commit date:
-

#### Last publication date:
12 December 2018

#### List of related papers:
https://doi.org/10.1109/ICECCS2018.2018.00027 (ICECCS '18)
https://doi.org/10.1007/978-3-319-63387-9_21 (CAV '17)
https://dx.doi.org/10.4230/LIPIcs.TIME.2017.7 (TIME '17)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: MITL
:: Automaton
:: PV5 :: compiles a temporal logic formula to a timed automaton