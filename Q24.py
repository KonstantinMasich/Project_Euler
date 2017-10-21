# PROJECT EULER
# Question 23
# Konstantin Masich
# Python 3.5.2

import math

def first_digit(l, target_num):
    """Gets list and target permutation num, returns 1st digit of perm."""
    index = target_num/math.factorial(len(l)-1)
    return l[int(index)]

#l = [0, 1, 2, 3]
l = [1, 2, 3]
n = len(l)
target_permutation = l
TARGET_PERMUTATION_NUMBER = 0

stop_flag = False
perm_no = 0

for i in range(0, math.factorial(n)):
    print("First digit is:", first_digit(l, i))
    
    
print(int(14/6))
