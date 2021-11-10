# Counter-Example Guided Abstraction Refinement
*Also known as CEGAR*

In model checking there are several techniques to reduce the state space. One of these is by building an abstract model of the original program.
With CEGAR, you use an iterative method to find a suitable abstraction, hence "Abstraction Refinement". 
You start with an initial abstraction and use this to check a property. If this property holds for the abstract model, then we know that it also holds for the original model. However, if the property is not proven, then we will check whether the counterexample in the abstraction corresponds to a counterexample in the original program. If not, then we consider this counterexample to be **spurious**. We then need to refine the abstraction and re-try the verification of the property. We can use the knowledge of the spurious counterexample to find a better abstraction.