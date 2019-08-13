'''
@author: youxinyu
@date: 2018-9-4
'''

# Recursion
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Linear iteration
def fibonacci_2(n):
    return fibonacci_iter(1, 0, n)

def fibonacci_iter(a, b, count):
    if count == 0: return b
    return fibonacci_iter(a+b, a, count-1)    # a←a+b,b←a.

# Linear iteration with list
def fibonacci_3_wap(n):
    memoize = [None for i in range(0,n)]
    return fibonacci_3(n,memoize)

def fibonacci_3(n, memoize):
    if n == 0: return 0
    if n == 1: return 1
    index = n - 1
    if memoize[index] != None:
        return memoize[index]
    memoize[index] = fibonacci_3(n-1, memoize)+fibonacci_3(n-2, memoize)
    return memoize[index]

# DP
def fibonacci_4(n):
    fib = [None for i in range(0,n+1)]  # !: n+1
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
        i += 1
    return fib[n]

def main():
    print(fibonacci(5))
    print(fibonacci_2(5))
    print(fibonacci_3_wap(5))
    print(fibonacci_4(5))

if __name__ == '__main__':
    main()
