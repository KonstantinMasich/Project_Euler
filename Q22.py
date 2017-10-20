# PROJECT EULER
# Question 22
# Konstantin Masich
# Python 3.5.2

SUBSTRACTION_BASE = 64


# 1. Obtain data from file
x = []
with open("Data_for_Q22", "rt") as f:

    for line in f:
        line = line.replace('"', '')
        x = line.split(',')
        x.pop()
        
print(ord('A') - SUBSTRACTION_BASE)
