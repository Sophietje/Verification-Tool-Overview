Data-driven approach to Boolean functional synthesis

#### Name:
Manthan

#### Application domain/field:
Boolean functional synthesis

#### Type of tool (e.g. model checker, test generator):
Synthesis tool

#### Expected input thing:
$F(X,Y)$ formula

#### Expected input format:
Either as a [QDIMACS](../../Formats/QDIMACS.md) or [Verilog](../../Formats/Verilog.md) input file

#### Expected output:
Boolean function $\Psi$ such that $\exists F(X,Y) = F(X, \Psi(X))$.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
"In the context of applications, the sets $X$ and $Y$ are viewed as inputs and outputs, and the formula $F(X,Y)$ is viewed as the functional specification capturing the relation between $X$ and $Y$".

It uses [ABC](../Frameworks/ABC.md), [PicoSAT](../Solvers/SAT/PicoSAT.md), [[Open-WBO]] and [[Scikit-Learn]].

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://github.com/meelgroup/manthan
#### Last commit date:
8 February 2021

#### Last publication date:
14 July 2020

#### List of related papers:
[Manthan: A Data-Driven Approach for Boolean Function Synthesis](https://doi.org/10.1007/978-3-030-53291-8_31)

#### Related tools (tools mentioned or compared to in the paper):
Compared in the paper to [[C2Syn]], [[BFSS]] and [CADET](../Solvers/CADET.md).

#### Meta
:: Synthesis
:: PV2 :: generates a depencency function linking two arguments of a given function