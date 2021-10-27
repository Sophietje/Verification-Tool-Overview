# Model checking
Check whether a model of a system meets a given specification. This relies on an **exhaustive search** of the state space. 

The specification that should be checked is often written in a temporal logic such as LTL or CTL.

A common problem is **state space explosion**, where the size of the state space tends to grow exponentially in the number of processes and variables. This makes it infeasible to do an exhaustive search of the state space. Therefore, researchers have come up with many methods to reduce the number of required states. For example through abstraction of the system or bounded model checking.

**Bounded model checking (BMC)**: search for a counterexample in executions whose length is bound by some integer *k*. If no bug is found, then *k* is increased until either a bug is found or the problem becomes intractable, or some pre-known upper bound is reached.