GACAL verifies C programs by searching over the space of possible invariants, using traces of the input program to identify potential invariants. GACAL uses the [[ACL2s]] theorem prover to verify these potential invariants, using an interface provided by ACL2s for connecting with external tools. GACAL iteratively searches for and proves invariants of increasing complexity until the program is verified.