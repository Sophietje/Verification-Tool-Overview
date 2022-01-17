Algorithm & tool, called Sequential Iterative Scheme for solving a BMI (bilinear matrix inequality)

#### Name:
SISBMI: Sequential Iterative Scheme for solving a Bilinear Matrix Inequality

#### Application domain/field:
Safety properties
Hybrid systems
Bilinear Matrix inequality (BMI)
Barrier certificate generation
Safety verification

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- BMI problem
- Initial values $u^0, v^0, Z^0$ and $U^0$

#### Expected input format:
?

#### Expected output:
Feasible solution $(u^*,v^*)$ for the BMI problem

#### Internals (tools used, frameworks, techniques, paradigms, ...):
A **barrier certificate** is a function where the zero level set separates the unsafe region from all reachable states of a system. The existence of a barrier certificate implies that the unsafe region is not reachable, therefore safety verification can be transformed into the problem of **barrier certificate generation**.
Barrier certificate generation is equivalent to solving a bilinear matrix inequality (BMI) with a particular type.

#### Comments:
-

#### URIs (github, websites, etc.):
-

#### Last commit date:
-

#### Last publication date:
14 July 2020

#### List of related papers:
https://doi.org/10.1007/978-3-030-53288-8_29 (CAV '20)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in the CAV '20 paper: [[PENBMI]], [[SOSTOOLS]]