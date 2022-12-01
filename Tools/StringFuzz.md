Problem instance generator and fuzzer for SMT string solvers

#### Name:
StringFuzz

#### Application domain/field:
String constraint solvers
Problem generator
Benchmark generator
Fuzzing

#### Type of tool (e.g. model checker, test generator):
Generator/transformer for string constraint problems

#### Expected input thing:
Depends on which tool is used.

#### Expected input format:
Most things are passed as an argument when calling the tool. 

#### Expected output:
Depends on the tool that is used.
`stringfuzzg`, `stringfuzzx` and `stringmerge` will output an SMT-LIB instance.
`stringstats` will output some properties of a given SMT-LIB instance.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
Consists of the following tools:
- `stringfuzzg`: generates SMT-LIB instances
- `stringfuzzx`: Transforms SMT-LIB instances
- `stringstats`: Outputs properties of a given SMT-LIB instance such as the number of variables, the maximum syntactic depth of expressions, etc.
- `stringmerge`: Merges several SMT-LIB instances into one.

Uses [SMT-LIB](../Formats/SMT-LIB.md).

#### Comments:
License: MIT

#### URIs (github, websites, etc.):
Project page: http://stringfuzz.dmitryblotsky.com/
Repository: https://github.com/dblotsky/stringfuzz

#### Last commit date:
11 June 2018

#### Last publication date:
18 July 2018

#### List of related papers:
[StringFuzz: A Fuzzer for String Solvers](https://doi.org/10.1007/978-3-319-96142-2_6) (CAV '18)

#### Related tools (tools mentioned or compared to in the paper):
Test suites for solver testing and benchmarking: [[Kaluza]], [[Kausler]].
[[FuzzSMT]] generates SMT-LIB instances with bit-vectors and arrays (does not support strings or regexes).
[[SMTpp]] pre-processes and simplifies SMT-LIB instances.

#### Meta
:: PV2 :: generates and transforms SMT-LIB instances
:: Source :: https://doi.org/10.1145/3550355.3552426
