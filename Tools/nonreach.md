nonreach is an automated tool for nonreachability analysis that is intended as a drop-in addition to existing termination and confluence tools for term rewriting

#### Name:
nonreach

#### Application domain/field:
Nonreachability analysis
Reachability
Termination

#### Type of tool (e.g. model checker, test generator):
Nonreachability tool

#### Expected input thing:
- Rewrite system
- Nonreachability or infeasibility problem

#### Expected input format:
- *Rewrite system*: `.trs` file
- *Problem*: Defined as `s -> t` where s and t are terms. This should be given via one of the following options:
	1. white-space-separated list of problems via command line or a file
	2. infeasibility problem should be provided as part of the input rewrite system
	3. Or given via standard input

#### Expected output:
`NO` if nonreachability can be established for the problem. 
`YES` if it was given an infeasibility problem which is infeasible.
`MAYBE` or `TIMEOUT` otherwise.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
nonreach has been made to be a back end for reachability analysis tools. 

#### Comments:
-

#### URIs (github, websites, etc.):
Repository: https://bitbucket.org/fmessner/nonreach/src/master/

#### Last commit date:
6 December 2020

#### Last publication date:
4 April 2019

#### List of related papers:
[nonreach – A Tool for Nonreachability Analysis](https://doi.org/10.1007/978-3-030-17462-0_19) (TACAS '19)

#### Related tools (tools mentioned or compared to in the paper):

#### Meta
:: PV1 :: determines whether a problem for a rewrite system is nonreachable or infeasible
:: Source :: https://doi.org/10.1145/3550355.3552426