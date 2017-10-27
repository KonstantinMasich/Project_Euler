# PROJECT EULER
# Question 26
# Konstantin Masich
# Python 3.5.2
        
def periodic_part_length(x):
    """Returns length of periodic part, 0 if there is no periodic part"""
    remainders = [1]
    remainder = 1
    negative = -1
    while True:
        # 1. Cannot divide
        remainder *= 10
        while remainder/x < 1:
            remainder *= 10
            remainders.append(negative)
            negative += -1
        # 2. Counting remainder:
        remainder = remainder%x
        # 3. Checking zero remainder:
        if remainder == 0:
            return 0
        # 4. Checking remainder already encountered:
        if remainder in remainders:
            return len(remainders)-remainders.index(remainder)
        remainders.append(remainder)

m = 0
d = 1
for i in range(1, 1000):
    v = periodic_part_length(i)
    if v > m:
        m = v
        d = i
print("Ans:", d)
