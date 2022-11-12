#### Name:
Sketcham, short for Sketch and Mocks

#### Application domain/field:
Program synthesis
Sketching
Modular synthesis

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Input sketch program

#### Expected input format:
Sketch's intermediate representation

#### Expected output:
Program sketch augmented with mock harnesses.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
*Sketch*: Program written in a C-like language augmented with holes, unknown constants, and generators, unknown expressions.
*Harnesses*: Way to specify the solution for a sketch using test cases that make assertions about the results.
*Mocks*: Functions that, in place of full implementations, approximate the desired behavior with a specification in the form of assertions about individual cases.

Sketcham converts a regular sketch problem into a modular sketch problem by automatically generating mocks from harnesses.

Sketcham has been implemented as an additional pass to [[Sketch]].

#### Comments:
-

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
15 July 2021

#### List of related papers:
[Program Sketching by Automatically Generating Mocks from Tests](https://doi.org/10.1007/978-3-030-81685-8_38) (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV2 :: synthesises a full program from its sketch
:: Synthesis
:: Source :: https://doi.org/10.1145/3550355.3552426