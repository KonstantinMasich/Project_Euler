# PROJECT EULER
# Question 25
# Konstantin Masich
# Python 3.5.2

F = [1, 1]
n = 2
while len(str(F[len(F)-1]))!=1000:
    n += 1
    F.append(F[len(F)-1] + F[len(F)-2])
print("Ans:", n)
