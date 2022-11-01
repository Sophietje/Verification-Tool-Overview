Tool for the analysis of SystemC systems. It extracts models that can be passed to tools such as [[SatAbs]] and [CBMC](Checkers/CBMC.md).

#### Name:
SCOOT

#### Application domain/field:
Model checking
Simulation
Model extraction
SystemC
Concurrency

#### Type of tool (e.g. model checker, test generator):
Model extractor?

#### Expected input thing:
SystemC program

#### Expected input format:
C++ files that use the SystemC header (`#include <systemc.h>`)

#### Expected output:
Formal model or a flat C++ program that does not use the SystemC library anymore.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
SCOOT statically analyses systems described using SystemC and extracts models that can be passed to verification tools such as [[SatAbs]] or [CBMC](Checkers/CBMC.md). It focuses on the scheduling of the SystemC threads. SCOOT can do race analysis.

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: http://www.cprover.org/scoot/

#### Last commit date:
- (latest download available on the project website is from October 2009)

#### Last publication date:

#### List of related papers:
[Race analysis for systemc using model checking](https://doi.org/10.1145/1754405.1754406) (ACM Transactions on design Automation of Electronic Systems, Vol. 15, '10)
[
              Scoot: A Tool for the Analysis of SystemC Models](https://doi.org/10.1007/978-3-540-78800-3_36) (TACAS '08)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C++
:: SystemC
:: PV2 :: extracts models from source code for other checkers, generates code that does not rely on SystemC