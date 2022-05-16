Tool for verifying scenarios involving vehicles executing complex plans in large cluttered workspaces. 

#### Name:
SceneChecker

#### Application domain/field:
Hybrid systems
Safety verification
Reachability verification
Cyber-physical systems
Scenario verification

#### Type of tool (e.g. model checker, test generator):
?

#### Expected input thing:
- Scenario file, this describes e.g. fixed obstacles, a plan, and an agent that is supposed to execute the plan without running into the obstacles.
- Dynamics file

#### Expected input format:
- *Scenario description*: JSON file
- *Dynamics file*: ?

#### Expected output:
`safe` in case the reachset of automaton H does not intersect with the unsafe set.
`unknown` otherwise.
It also gives some performance metrics and it can visualize various computed reachsets.

#### Internals (tools used, frameworks, techniques, paradigms, ...):
*Scenario verification*: check that a vehicle or an agent can safely execute a plan through a complex environment

Tool for verifying scenarios involving vehicles executing complex plans in large cluttered workspaces. It converts the scenario verification problem to a standard hybrid system verification problem, and solves it by exploiting structural properties in the plan and vehicle dynamics.
It uses reachability tools for verification.

Uses [Flow\*](Flow*.md), [DryVR](DryVR.md) for reachability analysis.

#### Comments:
-

#### URIs (github, websites, etc.):
Artifact CAV '21: https://figshare.com/articles/software/CAV2021_reduce_v6_ova/14504352
Project page: https://publish.illinois.edu/scenechecker/
Repository: https://gitlab.engr.illinois.edu/sibai2/multi-drone_simulator/-/releases/cav_artifact

#### Last commit date:
18 July 2021?

#### Last publication date:
15 July 2021

#### List of related papers:
https://doi.org/10.1007/978-3-030-81685-8_28 (CAV '21)

#### Related tools (tools mentioned or compared to in the paper):
Compared to in CAV '21 paper: [DryVR](DryVR.md), [Flow\*](Flow*.md)

#### Meta
:: PV2 :: transforms scenarios for hybrid control systems to reachability problems, requires an external solver