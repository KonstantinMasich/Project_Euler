import numpy as np
import math

def fibonacci(n):
        if n<3:
                return 1
        else:
                return fibonacci(n-1) + fibonacci(n-2)

def fibo2(n):
    """Faster than regular Fibonacci"""
    n -= 1
    F = [1, 1]
    for i in range(1, n):
        F.append(F[len(F)-1] + F[len(F)-2])
    return F[len(F)-1]
    
def digits_num(x):
    """Counts digits in a number"""
    x = np.float128(x)
    return int(np.log10(x)+1)
        
        
f = fibo2(1400)
print(type(f))
a = 8
print(type(a))       
print(digits_num(f))
