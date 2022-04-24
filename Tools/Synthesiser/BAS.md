#### Name:
BAS: Bounded Asynchronous Synthesis

#### Application domain/field:
Program synthesis
Reactive asynchronous systems
Asynchronous synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
LTL formula $\varphi$

#### Expected input format:
? (probably LTL3BA format)

#### Expected output:
- `UNREALIZABLE` if the LTL specification is synchronously unrealizable
- `REALIZABLE` and implementation if $PR(\varphi)$ (Pnueli-Rosner closure of $\varphi$) is synchronously realizable.
- `UNREALIZABLE`  if $PR(\neg\varphi)$ (Pnueli-Rosner closure of $\neg\varphi$) is not synchronously realizable.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- Uses [[LTL3BA]], [BoSy](BoSy.md), [[Acacia+]]
- Uses BDDs (Binary Decision Diagrams).
- Given an LTL specification, they use that *asynchronous* synthesis can be reduced to checking whether a specification is *synchronously* synthesizable.

#### Comments:
Tool to synthesize (i.e. automatic construction from specification) asynchronous programs from temporal specifications

#### URIs (github, websites, etc.):

#### Last commit date:

#### Last publication date:
18 July 2018

#### List of related papers:
https://doi.org/10.1007/978-3-319-96145-3_20

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV5 :: synthesises asynchronous programs based on an LTL formula
:: Synthesis
:: LTL