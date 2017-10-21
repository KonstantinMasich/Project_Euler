# PROJECT EULER
# Question 24
# Konstantin Masich
# Python 3.5.2

# Solved by math: T[i] = T[i-1] - row[i]*(n[i]-1)!

import math

def first_digit(l, target_num):
    """Gets list and target permutation num, returns 1st digit of perm."""
    index = target_num/math.factorial(len(l)-1)
    return int(index)

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Starting set
n = len(l)   # Length of starting set (will decrement over time)
T = 999999   # Target permutation number - we begin counting FROM ZERO!
res = []     # Result list

while (n-1)>=0:
    # 1. Getting current first digit:
    row = first_digit(l, T)
    x = l[row]
    res.append(x)
    # 2. Changing data:
    T = int(T - row * math.factorial(n-1))
    l.remove(x) # Working list
    n = len(l)  # Working list size
    
# 3. Result is:
print (''.join(str(x) for x in res))
