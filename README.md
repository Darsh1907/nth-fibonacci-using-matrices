# Finding nth factorial using matrices
Finding nth factorial using Diagonalization of a matrix A and Powers of A

## First lets see what is Diagonalization of a matrix A :-

Consider a nxn matrix A having eigen values as λ1, λ2,......λn and X1, X2,.....Xn as the corresponding eigen vectors.
Then, we can define an eigen vector matrix S as follows: [X1 X2 ....  Xn] where every Xi is a column matrix (eigen vector).

We can now define a diagonal matrix D = *F-1)*A*S = <br>
[ λ1 0 0 ]<br>
[ 0 λ2 0 ]<br>
[ 0 0 λ3 ]<br>

## Powers of matrix A :-

From diagonalization of a matrix A, we have found out that D = S^(-1)AS

Let's say need to find D^2
= D * D
= S^(-1)AS S^(-1)AS
= S^(-1)A AS
= S^(-1) A^2 S

Similarly, to find D^3
= D^2 x D
= S^(-1) A^2 S S^(-1) A S
= S^(-1) A^2 A S
= S^(-1) A^3 S

Hence we can conclude, **D^n = S^(-1) A^n S**
