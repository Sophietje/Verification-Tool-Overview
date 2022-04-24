Synthesizer of Super-optimized smart contracts

#### Name:
syrup

#### Application domain/field:
Smart contracts
Blockchain
Super-optimization
Synthesis
Ethereum
Gas optimization
Max-SMT

#### Type of tool (e.g. model checker, test generator):
Optimizer? Synthesis tool?

#### Expected input thing:
Stack Functional Specification (SFS). This describes the source and target stack of the Ethereum Virtual Machine (EVM).

#### Expected input format:
`.json` file

#### Expected output:
If successful, it outputs optimized EVM bytecode to transform the source into the target stack.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
"**Super-optimization** is a technique that tries to find the best translation of a block of code by trying all possible sequences of instructions that produce the same result."
In the case of smart contracts, one tries to optimize the gas usage. **Gas** is the fee required to successfully conduct a transaction or execute a smart contract.

It supports the following Max-SMT solvers: [Z3](../Solvers/SMT/Z3.md), [Barcelogic](../Solvers/SMT/Barcelogic.md) and [OptiMathSAT](../Solvers/OptiMathSAT.md).
It uses [[EthIR]] to generate control flow graphs of the analyzed contracts.

#### Comments:
License: Apache-2.0

#### URIs (github, websites, etc.):
Repository (of the backend): https://github.com/mariaschett/syrup-backend
Repository for examples of the CAV '20 paper: https://github.com/mariaschett/syrup-backend/tree/master/examples/cav2020

#### Last commit date:
14 May 2020

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_10 (CAV '20)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: Synthesis
:: Smart contract
:: PV2 :: generates optimized EVM bytecode to transform the source into the target stack