import numpy as np

def nth_fibonacci(n):

    if n==0:
        return 0
    
    elif n==1:
        return 1

    # define the matrix A
    A = np.array([[1, 1],
                [1, 0],])

    # define the column matrix [1;0]
    b = np.array([1, 0])
    b = b.reshape(2, 1)

    # Find eigenvalues and eigenvectors of A
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # D = diagonal matrix would be the matrix whose principal diagonal elements are the eigenvalues of A
    # D^n can be easily found by just rasing the diagonal elements to the power of n
    # (That's because D is a diagonal matrix)
    D_pow_n = np.diag(eigenvalues**n)

    # S is the eigenvectors matrix
    S = eigenvectors
    S_inv = np.linalg.inv(eigenvectors)

    # A^n = S * D^n * S^(-1)
    A_pow_temp = np.dot(S, D_pow_n)
    A_pow = np.dot(A_pow_temp, S_inv)

    # resultant matrix is the column matrix with 2 elements.
    result = list(np.dot(A_pow, b))

    # First element of result f(n+1) and second one being f(n) which is our required number. So we'll return it.
    # The variable result is a list of 2 tuples with one element in each.
    # result[1] will provide us with the second tuple.
    # (result[1])[0] will provide us with the element in it. (Our required answer)
    return round((result[1])[0])

# Take user input
n = int(input("Enter a positive integer n: "))
if n<0:
    print("Please don't enter a negative integer n")
else:
    print("The nth factorial is:", int(nth_fibonacci(n)))