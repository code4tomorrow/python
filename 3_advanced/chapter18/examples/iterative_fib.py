# iteration is much quicker than recursion for this problem

# finds the nth term in the Fibonacci sequence using iteration
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n - 1):
        a, b = b, a + b
        
    return a

print(fibonacci(5))
