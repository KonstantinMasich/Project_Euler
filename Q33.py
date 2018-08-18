# PROJECT EULER
# Question 33
# Konstantin Masich
# Python 3.5.2

import numpy as np
from math import gcd

# Structure:
#  a
# --- = c
#  b

a_list, b_list = [], []

# a moves in [10, b) since it has to be strictly smaller than b in order
# for a fraction to be < 1
# 
# b moves in [11, 99]; from 11 because it must be greater than a
# which starts at 10

for b in range(11, 99+1):
    for a in range(10, b):
        common_digit = set(str(a)).intersection(set(str(b)))
        # If a and b have 1 common digit and a, b are not multiple of 10:
        if len(common_digit) == 1 and a%10!=0 and b%10!=0:
            old_frac = a / b
            # 1. We 'simplify' the fraction illegally:
            new_a = [int(el) for el in str(a)]
            new_a.remove(int(list(common_digit)[0]))
            new_b = [int(el) for el in str(b)]
            new_b.remove(int(list(common_digit)[0]))
            if (new_b[0] != 0):
                new_frac = new_a[0] / new_b[0]
            # 2. If illegally 'simplified' result is still correct, we store it:
            if old_frac == new_frac:
                a_list.append(a)
                b_list.append(b)
                
a_prod = np.prod(a_list)
b_prod = np.prod(b_list)
print('Ans:', b_prod / gcd(a_prod, b_prod))
