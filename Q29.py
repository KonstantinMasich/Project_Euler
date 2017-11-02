# PROJECT EULER
# Question 29
# Konstantin Masich
# Python 3.5.2

r = set([])
for a in range(2, 101):
    for b in range(2, 101):
        r.add(a**b)
print("Ans:", len(r))
