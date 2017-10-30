# PROJECT EULER
# Question 28
# Konstantin Masich
# Python 3.5.2
    
l = [1] # list of diagonal values except 1
s = 2   # starting number; 2 is starting num for square with order = 2
n = 3   # square side; 3 is side of square with order = 2
while n <= 1001:
    for k in range(1, 5):
        l.append((s-1) + k*(n-1))
    s = l[-1] + 1
    n += 2
print("Ans:", sum(l))
