#### Name:
JBMC

#### Application domain/field:
Model checking
Bounded model checking
Software model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- Compiled Java program (may include assertions)
- Number of times loops should be unwinded

#### Expected input format:
- .class file (compiled Java program)
- integer passed as an argument when calling JBMC (number of loop unwinds)

#### Expected output:
Whether the verification failed or succeeded. It will show a list of defects and whether they were verified ('SUCCESS') or not ('FAILURE').

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Bounded model checker for Java bytecode.
It checks runtime exceptions (e.g. nullpointer exceptions) and user-defined assertions

Uses SAT/SMT solver (no specific one mentioned).
Built on top of [[CPROVER]].
Tool paper calls it an extension to [[CBMC]].

It is possible to configure JBMC by passing arguments when calling JBMC. For example one can choose to disable certain checks (e.g. division by zero checks). For more information on the configurations, see: https://www.cprover.org/jbmc/command_line_options.html

#### Comments:
-

#### URIs (github, websites, etc.):
Project page: https://www.cprover.org/jbmc/
Repository: https://github.com/diffblue/cbmc/tree/develop/jbmc (located in the [[CBMC]] repository)

#### Last commit date:
14 June 2021

#### Last publication date:
4 April 2019

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_10
https://doi.org/10.1007/978-3-030-17502-3_17

#### Related tools (tools mentioned or compared to in the paper):

