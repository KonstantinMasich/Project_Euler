# PROJECT EULER
# Question 67
# Konstantin Masich
# Python 3.5.2
# Idea: summarize elements down-to-top and determine the best route based
# on total sums of each level.

from operator import add

def read_file_backwards():
    """Reads the file in reversed order into a list"""
    res = []
    for line in reversed(list(open("Data_for_Q67"))):
        res.append([int(i) for i in line.rstrip().split()])
    return res

def compare_pairs(l):
    """Compares every pair in list and returns maximum in each pair."""
    return [max(l[i], l[i+1]) for i in range(0, len(l)-1, 1)]
    
    
def add_lists(l1, l2):
    """Just sums 2 lists element-wise."""
    return list(map(add, l1, l2))
 
# 1. First, we read the data file in reversed order.
triangle = read_file_backwards()
# 2. After that we iterate over the triangle, comparing and adding pairs:
temp = [0] * (len(triangle))
for row in triangle:
    row_sum = add_lists(row, temp)
    temp = compare_pairs(row_sum)
print("Result =", row_sum)
