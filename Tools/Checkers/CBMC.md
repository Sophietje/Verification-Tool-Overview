#### Name:
CBMC: C Bounded Model Checker

#### Application domain/field:
Model checking
Bounded model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Program
- *Optionally*: Loop bound

#### Expected input format:
- *Program*: C or C++ program
- *Loop bound*: Passed as an option when executing cbmc

#### Expected output:
- Error/warning when a property is violated.
- *Optionally*: If an assertion is violated, CBMC can give a counterexample trace where the assertion is violated. This trace can either be printed or output in an XML file.
- *Optionally*: a list the properties that it checks.
- *Optionally*: the verification conditions that are generated.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Loop unwinding
Bounded model checking: check if a property holds for traces up to n steps (i.e. length of the trace). 
SAT solving

It can verify array bounds (buffer overflows), pointer safety, exceptions and user-specified assertions. Note that for some of these checks you need to pass specific options when executing cbmc.

#### Comments:
It is part of [CProver](../Frameworks/CProver.md)

#### URIs (github, websites, etc.):
Repository: https://github.com/diffblue/cbmc
Project page: https://www.cprover.org/cbmc/

#### Last commit date:
30 Mar 2023 (last activity)

#### Last publication date:
18 July 2018

#### List of related papers:
[Model Checking Boot Code from AWS Data Centers](https://doi.org/10.1007/978-3-319-96142-2_28)
[A Tool for Checking ANSI-C Programs](https://doi.org/10.1007/978-3-540-24730-2_15)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: C
:: C++
:: PV3           :: verifies given/parameterised properties of C code
:: Model checking
:: Source :: https://doi.org/10.1145/3550355.3552426
