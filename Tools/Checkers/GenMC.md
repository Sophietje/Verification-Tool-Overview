LLVM-based stateless model checker (SMC) for concurrent C/C++ programs

Given a C/C++ program as inputs (that uses C/C++11 atomics and/or concurrency primitives from the pthread library), it reports any data races, assertion violations, or other errors encountered.
The verification can be performed with respect to the RC11 memory model (default), or other models such as IMM and LKMM.

Project page: https://plv.mpi-sws.org/genmc/
Repository: https://github.com/mpi-sws/genmc/