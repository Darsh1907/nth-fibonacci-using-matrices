import numpy as np
import math

def nth_fibonacci(n):
    sq5 = math. sqrt(5)
    a = pow(((1+sq5)/2), n)
    b = pow(((1-sq5)/2), n)
    return (1/sq5)*(a-b)

# Take user input
n = int(input("Enter a positive integer n: "))
if n<0:
    print("Please don't enter a negative integer n")
else:
    print("The nth factorial is:", int(nth_fibonacci(n)))