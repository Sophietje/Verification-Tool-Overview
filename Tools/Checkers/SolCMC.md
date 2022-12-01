#### Name:
SolCMC

#### Application domain/field:
Smart contracts
Model checking
Symbolic model checking

#### Type of tool (e.g. model checker, test generator):
Model checker

#### Expected input thing:
Solidity program with assert statements

#### Expected input format:
Solidity language
SolCMC uses the asserts and requires clauses to identify verification targets.

#### Expected output:
Reports violations of:
- Assertions
- Popping empty arrays
- Out of bounds index accesses
- Arithmetic underflow/overflow
- Division by zero
- Insufficient transfer balance.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
SolCMC supports unbounded model checking as well as bounded model checking.
It encodes a smart contract as a system of constrained horn clauses for unbounded model checking. It is encoded in SMT queries for bounded model checking.

It uses [Spacer](../../Tools/Solvers/Spacer.md) and [Eldarica](Eldarica).
It uses [cvc5](../../Tools/Solvers/SMT/cvc5.md) and [Z3](../../Tools/Solvers/SMT/Z3.md) for bounded model checking.

#### Comments:
Shipped with Ethereum Foundation's Solidity compiler. Used to be called SMTChecker.

#### URIs (github, websites, etc.):
- Documentation: https://docs.soliditylang.org/en/latest/smtchecker.html
- Artifact: https://github.com/leonardoalt/cav_2022_artifact
- Repository: https://github.com/ethereum/solidity/tree/develop/libsolidity/formal

#### Last commit date:
28 November 2022

#### Last publication date:
2022

#### List of related papers:
[SolCMC: Solidity Compiler's Model Checker](https://doi.org/10.1007/978-3-031-13185-1) (CAV 2022)
https://doi.org/10.5281/zenodo.6512173 (extended version of CAV '22 paper)

#### Related tools (tools mentioned or compared to in the paper):
Other tools for analyzing Solidity programs: [[Solc-verify]], [[Verisol]], [[SmartAce]], [[EThor]], [[Certora]], [[K framework]], [[HEVM]], [[Echidna]], [[Slither]]

#### Meta
:: Smart contract
:: Model checking
:: Source :: [CAV '22](https://doi.org/10.1007/978-3-031-13185-1)
