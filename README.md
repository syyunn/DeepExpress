# On Neural Expressivity 

This repository aims to search for the neural network expressivity, how the 
architectural properties of a neural network - such as depth, width, layer
type - could affect the resulting functions computational property.

This repository mainly rooted on the recently published article, [On the 
Expressive Power of Deep Neural Networks (Raghu et al, 2017)](http://proceedings.mlr.press/v70/raghu17a/raghu17a.pdf)

## Table of Contents 
1. Universal Approximation Theorem 

2. On Lower Bounds and Upper Bound 
  
     To evade the waste of computation, to find this upper and lower bound is
     practically important, however still not enough literature has been 
     published.
     
     Moreover, formalization also matters. How to define the *Bounds of 
     Neural Expressivity* is still unanswered clearly.
     
3. Measure of Expressivity
    
    __Currently known measures__
     
    - *Activation Pattern* (Raghu et al. 2017)
    
        Using the notion of *transition*, where changing an input x to 
        nearby point x + $\sigma $ 
    - *Counting Non Linear Pieces*(Rincon et al. 2014) 

4. Trajectory 
$x(t)$ may be more complicated, and potentially not expressible in closed form

## References

##### Use trajectory for measure of complexity 

Raghu, M., Poole, B., Kleinberg, J., Ganguli, S. & Sohl-Dickstein, J.. (2017). On the Expressive Power of Deep Neural Networks. Proceedings of the 34th International Conference on Machine Learning, in PMLR 70:2847-2854

##### Introducing of the concept Linear Region
Julian Rincon, Adriana Moreo, Gonzalo Alvarez: “Exotic magnetic order in the orbital-selective Mott regime of multiorbital systems”, 2014, Phys. Rev. Lett. 112, 106405 (2014); arXiv:1402.1689. DOI: 10.1103/PhysRevLett.112.106405.

This paper had revealed that:
 
 __"Given a neural network with piecewise linear activations (such as ReLU or hard tanh), the function
it computes is also piecewise linear, a consequence of the fact that composing piecewise linear functions results in a
piecewise linear function."__   


## On number of Linear Region

