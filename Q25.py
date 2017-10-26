def fibonacci(n):
        if n<3:
                return 1
        else:
                return fibonacci(n-1) + fibonacci(n-2)

def fibo2(n):
    """Faster than regular Fibonacci"""
    n -= 1
    F = [1, 1]
    for i in range(1, n):
        F.append(F[len(F)-1] + F[len(F)-2])
    return F[len(F)-1]
        
        
for i in range(1, 14):
    print(i, fibo2(i))
    
print(fibo2(1000))

