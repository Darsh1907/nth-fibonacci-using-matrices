# Finding nth fibonacci using matrices
Finding nth fibonacci using Diagonalization of a matrix A and Powers of A

## First lets see what is Diagonalization of any matrix A :-

Consider a nxn matrix A having eigen values as λ1, λ2,......λn and X1, X2,.....Xn as the corresponding eigen vectors.
Then, we can define an eigen vector matrix S as follows: [X1 X2 ....  Xn] where every Xi is an eigen vector.

We can now define a diagonal matrix D = (S^-1) * A * S = <br>
[ λ1 0 0 ]<br>
[ 0 λ2 0 ]<br>
[ 0 0 λ3 ]<br>

## Powers of matrix A :-

From diagonalization of a matrix A, we have found out that D = S^(-1) * A * S

Let's say need to find D^2 <br>
= D * D <br>
= ( S^(-1) * A * S ) * ( S^(-1) * A * S ) <br>
= S^(-1) * A * A * S <br>
= S^(-1) * A^2 * S <br>

Similarly, to find D^3 <br>
= D^2 * D <br>
= ( S^(-1) * A^2 * S ) * ( S^(-1) * A * S ) <br>
= S^(-1) * A^2 * A * S <br>
= S^(-1) * A^3 * S <br>

Hence we can conclude, D^n = S^(-1) * A^n * S <br>
So,
A^n = S * D^n * S^(-1) <br>
We'll be using this formula later.

## Now, for nth fibonacci :-

We know that f0=0, f1=1, f2=f0+f1, f3=f1+f2 <br>
This can be represented in matrix form by, <br>

![image](https://user-images.githubusercontent.com/118650412/230645911-286e106b-0d10-4a12-864e-162b5aafcbe9.png)

So you can see, by multiplying this matrix repeatedly, it yields the nth and (n+1)th term

![image](https://user-images.githubusercontent.com/118650412/230646072-a7d2c0fe-1d86-4bb2-87bf-f4c1f8a94222.png)

We'll be using this logic in our implementation.
