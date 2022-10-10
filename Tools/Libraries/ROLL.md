ROLL 1.0 is an 𝜔-regular language learning library with command line tools to learn and complement Büchi automata

#### Name:
ROLL: Regular Omega Language Learning

#### Application domain/field:
Büchi automata
Automata learning
Active automata learning
𝜔-regular languages

#### Type of tool (e.g. model checker, test generator):
Library for automata learning

#### Expected input thing:
- Command indicating the running mode (e.g. `learn`, `convert`, `complement`, `include`)
- *Optional*: Depending on the command used, the user might need to give zero, one or two Büchi automata.

#### Expected input format:
- *Command*: Argument that is passed when calling ROLL
- *Büchi automata*: Hanoi Omega Automata ([HOA](../../Formats/HOA.md)) format and the BA format used by [RABIT](RABIT.md)

#### Expected output:
Depends on how the library is used. Typically it will output a learned or complement automaton along with some execution information.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
This is a library for learning 𝜔-regular languages, which can be used to describe liveness properties.

Uses [RABIT](RABIT.md) to check the equivalence of two Büchi automata.

The library can be used for:
- Learning an input Büchi automaton
- Converting files in the BA format to the HOA format or the other way around.
- Computing the complement of a Büchi automaton
- Check the language inclusion between two Büchi automata

#### Comments:
License: GPL v3.0

#### URIs (github, websites, etc.):
Project page: http://iscasmc.ios.ac.cn/roll/
Repository: https://github.com/ISCAS-PMC/roll-library

#### Last commit date:
12 July 2021

#### Last publication date:
December 2021

#### List of related papers:
[A novel learning algorithm for Büchi automata based on family of DFAs and classification trees](https://doi.org/10.1016/j.ic.2020.104678) (Information and Computation, vol. 281, '21)
[Proving Non-inclusion of Büchi Automata Based on Monte Carlo Sampling](https://doi.org/10.1007/978-3-030-59152-6_26) (ATVA '20)
[ROLL 1.0: 
                  
                    
                  
                  $$\omega $$
                -Regular Language Learning Library](https://doi.org/10.1007/978-3-030-17462-0_23) (TACAS '19)
[A Novel Learning Algorithm for Büchi Automata Based on Family of DFAs and Classification Trees](https://doi.org/10.1007/978-3-662-54577-5_12) (TACAS '17)

#### Related tools (tools mentioned or compared to in the paper):
Automata learning libraries: [[libalf]], [LearnLib](Libraries/LearnLib.md)

#### Meta
:: Automaton
:: Library
:: PV1 :: learns, transforms, inverts, complements Büchi automata