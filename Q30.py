# PROJECT EULER
# Question 30
# Konstantin Masich
# Python 3.5.2

def get_upper_limit():
    l = [9]
    n = len(l)
    while int(''.join(map(str,l))) < sum(list(map(lambda x: x**5, l))):
        l.append(9)
    return int(''.join(map(str,l)))

LIMIT = get_upper_limit()
val = 2
r = set([])
while val <= LIMIT:
    l = list(map(lambda x: int(x), list(str(val))))
    if val == sum(list(map(lambda x: x**5, l))):
        r.add(val)
    val += 1
print("Ans:", sum(r))
