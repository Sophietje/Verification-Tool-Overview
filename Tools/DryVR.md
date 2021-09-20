Framework for verifying hybrid control systems that are described by a combination of a black-box simulator for trajectories and a white-box transition graph specifying mode switches.

This framework includes:
- A probabilistic algorithm for learning sensitivity of the continuous trajectories from simulation data
- Bounded reachability analysis that uses the learned sensitivity
- Reasoning techniques for verification of complex systems under long switching sequences, from the reachability analysis of a simpler system under short sequences.

Repository: https://github.com/qibolun/DryVR (last commit: 14 February 2018)
Successor/version 2.0 of DryVR: https://github.com/qibolun/DryVR_0.2 (last commit: 1 May 2018)
Documentation: https://dryvr.readthedocs.io/en/latest/index.html