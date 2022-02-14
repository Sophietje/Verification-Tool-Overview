VeriFuzz is a coverage driven automated test-input generation tool based on grey-box fuzzing

#### Name:
VeriFuzz

#### Application domain/field:
Test-input generation
Fuzzing

#### Type of tool (e.g. model checker, test generator):
Fuzzer

#### Expected input thing:
- Program
- Safety property 

#### Expected input format:
- *Program*: ?
- *Safety property*: ?

#### Expected output:
It runs until an error location was reached or until the max. time is over.
If an error location was found, then it will generate a witness.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
VeriFuzz observes behaviors exhibited during a test run. It then uses evolutionary algorithms to generate newer test-inputs from an initial population of test inputs. 

It uses [CBMC](Checkers/CBMC.md) for the initial input generation. 

#### Comments:
-

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
4 April 2019

#### List of related papers:
https://doi.org/10.1007/978-3-030-17502-3_22 (TACAS '19)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
