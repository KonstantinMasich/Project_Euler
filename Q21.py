# PROJECT EULER
# Question 21
# Konstantin Masich
# Python 3.5.2

def d(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def eratosthenes(n):
    multiples = []
    res = []
    for i in range(2, n+1):
        if i not in multiples:
            res.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return set(res)
    
primes = eratosthenes(10000)

start_interval = set(range(1, 10000))
interval = list(start_interval - primes)

amicables = []
for i in interval:
    temp = d(i)
    if d(temp) == i:
        if temp != d(temp):
            amicables.append(i)
            amicables.append(temp)
print(sum(list(set(amicables))))
