# PROJECT EULER
# Question 23
# Konstantin Masich
# Python 3.5.2

# Raw running time: 40.5 sec

import time
import math

def is_abundant(n):
    sigma = 0
    for i in range(1, int(n/2 + 1)):
        if n%i==0:
            sigma+=i
        if sigma > n:
            return True
    return False
         

UPPER_LIMIT = 28123
INTERVAL = range(1, UPPER_LIMIT)

start = time.time()

# 1. Getting all abundant numbers
abundants = set()
for x in INTERVAL:
    # x is abundant: add it to the set and continue
    if is_abundant(x):
        abundants.add(x)

# 2. Getting sums of abundant numbers
sums = set()
for m in abundants:
    for n in abundants:
        sums.add(m+n)
        
# 3. Removing sums of abundant numbers
target_set = set(INTERVAL)
target_set -= sums

# 4. Getting result
print(sum(target_set))    

end = time.time()
print("Time elapsed:", end - start)
