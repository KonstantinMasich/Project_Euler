# PROJECT EULER
# Question 32
# Konstantin Masich
# Python 3.5.2

import numpy as np

def digit_count(number): 
    return int(np.log10(number))+1


def is_valid_multiplier(number):
    digits_set = set([int(el) for el in str(number)])
    # Contains zero?
    if 0 in digits_set:
        return False
    # All the digits are different?
    return len(digits_set) == digit_count(number)
    

def is_pandigital(mult_1, mult_2, prod):
    combined_num_str = str(mult_1) + str(mult_2) + str(prod)
    return len(combined_num_str) == len(set(combined_num_str))


def digits_sum(n1, n2, n3):
    return digit_count(n1) + digit_count(n2) + digit_count(n3)


illegal_numbers = [10 * i for i in range(1, 10)] + [11*i for i in range(1, 10)]
range_1digit = list(range(2, 9+1))
range_2digit = [el for el in range(10, 100) if el not in illegal_numbers]

# m1 moves from 3 digits to 4 digits
# m2 moves from 1  digit to 2 digits
# 
# illegal maximum of 2x2 = 99*99 = 9801 [2 + 2 + 4 = 8 < 9], miss
#    so 2x2 is impossible, all the more 2x1
# 
# illegal minimum of 3x1 = 111*1 = 111 [3 + 1 + 3 = 7 < 9],  miss
# illegal maximum of 3x1 = 999*9 = 8991 [3 + 1 + 4 = 8 < 9], miss
#    so 3x1 is impossible
# illegal minimum of 3x2 = 111*11 = 1221 [3 + 2 + 4 = 9], hit
#    so 3x2 is possible
#
# illegal minimum of 4x1 = 1111*1 = 1111 [4 + 1 + 4 = 9 = 9], hit
#    so 4x1 is possible
# illegal minimum of 4x2 = 1111*11 = 12221 [4 + 2 + 5 = 11], miss
#    so 4x2 is impossible, all the more 5x1 but still we check:
#
# illegal minimum of 5x1 = 11111*1 = 11111 [5 + 1 + 5 = 11 > 9], miss
#    so 5x1 is possible, all the more 5x2
#
# Thus m1 should move between 3 and 4 digits, and m2 between 1 and 2 digits
pandigitals = []
LO, HI = 123, 9876
for m1 in range(LO, HI+1):
    if is_valid_multiplier(m1):
        range_m2 = range_2digit if digit_count(m1)==3 else range_1digit
        for m2 in range_m2:
            prod = m1*m2
            if is_valid_multiplier(prod) and is_pandigital(m1, m2, prod) and digits_sum(m1, m2, prod)==9:
                pandigitals.append(prod)
                
print('Ans:', sum(set(pandigitals)))
