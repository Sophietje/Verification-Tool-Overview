Tool for the automatic checking of satisfiability, implication and equivalence of hyperproperties.

#### Name:
EAHyper

#### Application domain/field:
Hyperproperties
Temporal logic
Execution traces

#### Type of tool (e.g. model checker, test generator):
Satisfiability solver

#### Expected input thing:
HyperLTL formula in the $\exists^*\forall^*$ fragment, or an implication between two alternation-free formulas.

#### Expected input format:
?

#### Expected output:
- If given a formula in the $\exists^*\forall^*$ fragment, then it reports satisfiability
- If given an implication between two alternation-free formulas, then it reports validity.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- EAHyper is a tool for automatically checking satisfiability, implication and equivalence of hyperproperties. EAHyper analyzes hyperproperties that are specified in HyperLTL.
- EAHyper can therefore be used to detect specifications that inconsistent, vacuously true, or to check implication and equivalence between multiple formalizations of the same requirement.
- EAHyper supports the $\exists^*\forall^*$ fragment of HyperLTL, which is the largest decidable fragment of HyperLTL.
- This fragment consists of all formulas with at most one quantifier alternation, where no existential quantifier is in the scope of a universal quantifier.
- EAHyper reduces a HyperLTL formula to the satisfiability of an LTL formula. It then uses an external tool ([[pltl]] or [[aalta]]) to decide the satisfiability of the LTL formula.

- **Hyperproperties**: system properties that relate multiple computation traces.
- **HyperLTL**: Extension of LTL. It uses trace variables and trace quantifiers to refer to multiple execution traces simultaneously.

#### Comments:
License: ISC License

#### URIs (github, websites, etc.):
Project page: https://react.uni-saarland.de/tools/eahyper/
Repository: https://github.com/reactive-systems/eahyper
Try EAHyper online: https://www.react.uni-saarland.de/tools/online/EAHyper/

#### Last commit date:
18 July 2018

#### Last publication date:
13 July 2017

#### List of related papers:
[EAHyper: Satisfiability, Implication, and Equivalence Checking of Hyperproperties](https://doi.org/10.1007/978-3-319-63390-9_29) (CAV '17)

#### Related tools (tools mentioned or compared to in the paper):
Possibly related: [MCHyper](Checkers/MCHyper.md)

#### Meta
:: HyperLTL
:: PV4 :: checks satisfiability, implication and equivalence of hyperproperties