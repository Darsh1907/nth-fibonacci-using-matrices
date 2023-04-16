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

![image](https://user-images.githubusercontent.com/118650412/230646072-a7d2c0fe-1d86-4bb2-87bf-f4c1f8a94222.png)  ----(eqn 1)

As you can see, we need to find the nth power of A in this equation. We'll use the above derived formula to do so.

We'll be using this logic in our implementation.py program.

# Concluding...

An obvious improvisation to our previous implementation would be the following:
As we can see, we are finding the eigen values and eigen vectors of the <br>
[ 1 1 ]<br>
[ 1 0 ]<br>
matrix everytime we need to find some nth fibonnaci number. Instead of this, we can have the eigen values and eigen vectors of this constant matrix pre-calculated before implementing our program. This way we can generate a formula for nth fibonnaci number. Substituing the value of n in the formula will directly yield us the nth fibonnaci. Let's see how: <br>
![image](https://user-images.githubusercontent.com/118650412/232274373-bf8f741a-a4dd-4d8e-9196-3862db9a85a7.png)
![image](https://user-images.githubusercontent.com/118650412/232274382-bacafaf9-9917-490b-b56e-e3672d9cae7f.png)
![image](https://user-images.githubusercontent.com/118650412/232274387-f6ba98f5-6ea7-43a6-8d3c-80699f07ede1.png)
![image](https://user-images.githubusercontent.com/118650412/232274391-d6488f88-b199-4519-b3cc-3bd5ece5afb8.png)
![image](https://user-images.githubusercontent.com/118650412/232274393-65fd7190-3e84-4858-98b0-414151e9ed39.png)
Now to find the nth power of our matrix,
We use the formula we had derived i.e, A^n = S * D^n * S^(-1)
![la](https://user-images.githubusercontent.com/118650412/232274530-f51bc627-fe1e-4470-ad6d-4db1c5d2436a.jpg) <br>
Lets call this matrix the nth power matrix
Finally this matrix will be multiplied by the column vector: <br>
[ 1 ]<br>
[ 0 ]<br>
After multiplying, the second element in the resultant column vector will be our nth factorial (From eqn 1).
Hence, the formula for the nth number in the Fibonacci sequence is the lower left entry in the matrix we just found (nth power matrix). <br>
![image](https://user-images.githubusercontent.com/118650412/232274672-c8d6e420-d1ae-4df4-ac4a-4bd985c45d2d.png)
I have used this formula to find the nth factorial in the final.py
