Converts Mission-time LTL (MLTL) to either LTL, $LTL_f$ (LTL over finite traces), SMV or SMT 

#### Name:
MLTLconverter

#### Application domain/field:
Satisfiability checking
Mission-time LTL
MLTL satisfiability checking

#### Type of tool (e.g. model checker, test generator):
Translator

#### Expected input thing:
MLTL formula and a converter flag.
The converter flag indicates whether it should be translated to LTL, $LTL_f$, SMV or SMT-LIB v2.

#### Expected input format:
?

#### Expected output:
Reports whether the MLTL formula is satisfiable or not.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Uses [[aalta]] (LTL solver), [[aaltaf]] ($LTL_f$ solver), [nuXmv](Checkers/nuXmv.md) (SMV model checker), [Z3](Solvers/SMT/Z3.md) (SMT solver). These tools are used to check the satisfiability of the input MLTL formula and their encodings.

#### Comments:
They tested the different translations and it seemed that the SMT-based approach tends to perform best for satisfiability checking.
They advise to use MLTL-SAT via KLIVE for satisfiability checking of MLTL formulas with interval ranges less than 100.

#### URIs (github, websites, etc.):
Project page: http://temporallogic.org/research/CAV19/

#### Last commit date:
?

#### Last publication date:
12 July 2019

#### List of related papers:
[Satisfiability Checking for Mission-Time LTL](https://doi.org/10.1007/978-3-030-25543-5_1)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: LTL
:: PV2 :: given a MLTL formula, generate an equivalent in another LTL dialect to be used with an external solver