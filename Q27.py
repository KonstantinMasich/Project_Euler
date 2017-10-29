# PROJECT EULER
# Question 27
# Konstantin Masich
# Python 3.5.2

def eratosthenes(n):
    l = []
    primes = []
    for i in range(2, n+1):
        if i not in l:
            primes.append(i)
            for j in range(i*i, n+1, i):
                l.append(j)
    return primes

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

range_A = range(-999, 1000)  # A lies in (-1000, 1000)
range_B = eratosthenes(1000) # B is prime within 1000 included

max_a = 0
max_b = 0
max_primes = 0
# Loop on B, then A, then n:
for b in range_B:
    for a in range_A:
        # 1. Eliminate every a=-b
        if a == -b and a!=0:
            continue
        # 2. Start counting primes produced by formula:
        n = 0
        x = n*n + a*n + b
        primes_produced = 0
        while isPrime(x): # while x is prime:
            primes_produced += 1
            x = n*n + a*n + b
            n += 1
        # 3. If new max primes encountered:
        if max_primes < primes_produced:
            max_primes = primes_produced
            max_a = a
            max_b = b
print("Ans:", max_a * max_b)
