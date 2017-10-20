# PROJECT EULER
# Question 22
# Konstantin Masich
# Python 3.5.2

SUBSTRACTION_BASE = 64

def get_name_score(name, number):
    """ Score = (name char sum - base) * (number) """
    sigma = 0
    for c in name:
        sigma += ord(c) - SUBSTRACTION_BASE
    return sigma*number

# 1. Obtain data from file
names = []
with open("Data_for_Q22", "rt") as f:
    for line in f:
        line = line.replace('"', '').replace('\n','')
        names = line.split(',')
        
# 2. Sort all names
names.sort()

thefile = open('a.txt', 'w')
for item in names:
    thefile.write("%s\n" % item)
       
# 2. Count the sum
sigma = 0
i = 1
for name in names:
    sigma += get_name_score(name, i)
    i += 1
print(sigma)
