#### Name:
GDVB: Generation of DNN Verification problem Benchmarks

#### Application domain/field:
Machine learning
Deep neural networks
Benchmarking

#### Type of tool (e.g. model checker, test generator):
Benchmark/test generator

#### Expected input thing:
- Seed problem $<n_s, \varphi_s>$
- Set of factors $F$
- Constraints $\Gamma$
- Coverage goal $t$

#### Expected input format:
A `.toml` configuration file

#### Expected output:
A benchmark of DNN verification problems

#### Internals (tools used, frameworks, techniques, paradigms, ...):
GDVB generates benchmarks for the verification of neural networks. The benchmarks that it generates seeks to cover variations that influence verifier performance.
Uses [[R4V]] and [DNNV](DNNV.md). 

#### Comments:

#### URIs (github, websites, etc.):
Repository: https://github.com/edwardxu0/GDVB

#### Last commit date:
22 Jun 2022

#### Last publication date:
14 July 2020

#### List of related papers:
[Systematic Generation of Diverse Benchmarks for DNN Verification](https://doi.org/10.1007/978-3-030-53288-8_5)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: DNN
:: Neural network
:: PV2 :: given a problem and constraints, generates benchmarks