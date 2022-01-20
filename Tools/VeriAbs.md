VeriAbs verifies C programs by transforming them to abstract programs

#### Name:
VeriAbs: Verification by Abstraction

#### Application domain/field:
Model checking

#### Type of tool (e.g. model checker, test generator):
Preprocessor

#### Expected input thing:
C program

#### Expected input format:
?

#### Expected output:
[[CBMC]]-compatible representation

#### Internals (tools used, frameworks, techniques, paradigms, ...):
- static program analysis with [[PRISM]]
- bounded model checking with [[CBMC]]
- generating witnesses with [[CPAchecker]]
- full-program induction (since TACAS'20)

#### Comments:
-

#### URIs (github, websites, etc.):
SV-Comp'17: 115.113.148.49/VeriAbs.htm (dysfunctional)
SV-Comp'18: https://gitlab.com/sosy-lab/sv-comp/archives/-/blob/master/2018/veriabs.zip
SV-Comp'18: http://www.cmi.ac.in/~madhukar/veriabs/VeriAbs.zip
SV-Comp'19: https://gitlab.com/sosy-lab/sv-comp/archives-2020/tree/master/2020/veriabs.zip (wrong URL in the paper)
GitHub: https://github.com/divyeshunadkat/VAJRA ([[VAJRA]] and [[TILER]] are integrated and are claimed as the source of success of VeriAbs at SV-Comp'20)

#### Last commit date:
20 Feb 2020

#### Last publication date:
17 Apr 2020

#### List of related papers:
https://doi.org/10.1007/978-3-662-54580-5_32 (TACAS'17 tool)
https://doi.org/10.1007/978-3-319-89963-3_32 (TACAS'18 tool)
https://doi.org/10.1007/978-3-030-45237-7_25 (TACAS'20 tool)
https://doi.org/10.1007/978-3-030-45190-5_2 (TACAS'20 full paper)

#### Related tools (tools mentioned or compared to in the paper):
* [[PRISM]]
* [[CBMC]]
* [[CPAchecker]]
* [[VAJRA]]
* [[TILER]]
