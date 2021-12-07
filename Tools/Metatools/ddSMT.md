Delta-debugger for the SMT-LIBv2 language.

#### Name:
ddSMT

#### Application domain/field:
Debugging
SMT solving

#### Type of tool (e.g. model checker, test generator):
Debugger for SMT solvers

#### Expected input thing:
- Command, a typical command would be a call to an SMT solver.
- Input: SMT problem which can be used to trigger the problem

#### Expected input format:
One of the following: 
- [SMT-LIB](../../Formats/SMT-LIB.md)
- [SyGuS](../../Formats/SyGuS.md)
- the separation logic extension for [SMT-LIB](../../Formats/SMT-LIB.md).

#### Expected output:
Minimal working example, i.e. an input that is as small as possible but still triggers the original faulty behavior of the executed command.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Delta debugging: the goal is to minimize failure-inducing inputs. It extracts a minimal working example by omitting parts of the input that are irrelevant for triggering the faulty behavior.

#### Comments:
License: GPLv3

#### URIs (github, websites, etc.):
Documentation: https://ddsmt.readthedocs.io/
Repository: https://github.com/ddsmt/ddsmt

#### Last commit date:
2 September 2021

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81688-9_11 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
