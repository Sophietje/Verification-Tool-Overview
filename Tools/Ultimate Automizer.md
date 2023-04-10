Ultimate Automizer is a software verifier that implements an automata-based approach for the verification of safety and liveness properties

#### Name:
Ultimate Automizer

#### Application domain/field:
Abstraction refinement
Counterexample Guided Abstraction Refinement (CEGAR)
Model checking
Software model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
- C program
- Specification file
- Architecture
- *Optional*: Witness file for witness validation

#### Expected input format:
- *Program*: `.c` file
- *Specification file*: `.prp` file, SV-COMP format
- *Architecture*: `32bit` or `64bit` passed as an argument
- *Optional witness file:* `.graphml` file containing a violation or correctness witness

#### Expected output:
Whether the property holds or not.
It may generate a violation or correctness witness to `witness.graphml`.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Ultimate Automizer can analyse the reachability of error functions, memory safety, absence of overflows and termination.

Built on top of [[Ultimate]], a program analysis framework. Uses [Z3](Solvers/SMT/Z3.md), [CVC4](Solvers/SMT/CVC4.md), [MathSAT](Solvers/SMT/MathSAT.md)

#### Comments:
License information: https://github.com/ultimate-pa/ultimate/wiki/License

#### URIs (github, websites, etc.):
Ultimate Automizer project page: https://monteverdi.informatik.uni-freiburg.de/tomcat/Website/?ui=tool&tool=automizer
Ultimate project page: https://monteverdi.informatik.uni-freiburg.de/tomcat/Website/
Try online: https://monteverdi.informatik.uni-freiburg.de/tomcat/Website/?ui=int&tool=automizer
Ultimate repository (Ultimate Automizer is a part of this): https://github.com/ultimate-pa/ultimate

#### Last commit date:
09 Apr 2023 (last activity)

#### Last publication date:
14 April 2018

#### List of related papers:
[Ultimate Automizer and the Search for Perfect Interpolants](https://doi.org/10.1007/978-3-319-89963-3_30) (TACAS '18)
[Ultimate Automizer with an On-Demand Construction of Floyd-Hoare Automata](https://doi.org/10.1007/978-3-662-54580-5_30) (TACAS '17)
[Ultimate Automizer with Two-track Proofs](https://doi.org/10.1007/978-3-662-49674-9_68) (TACAS '16)
[
                Ultimate Automizer with Array Interpolation]([
                Ultimate Automizer with Array Interpolation](https://doi.org/10.1007/978-3-662-46681-0_43)) (TACAS '15)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV4 :: checks user-specified properties and some built-in properties, e.g. memory safety, of a C program for a specified architecture
:: C
