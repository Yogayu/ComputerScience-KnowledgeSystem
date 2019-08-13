# coding=utf-8
def solve_small(F,L):
    res = 0
    for i in range(F, L+1):
        if '9' not in str(i) and i % 9:
            res += 1
    return res

def solve(F, L):
    return count(L) - count(F) + 1

"""
count: from 0 to N, Count the numbers that are legal.
return count(L) - count(F) + 1, add 1 because F is legal too.
"""
def count(N):
    res = 0
    L = len(str(N))
    for i, v in enumerate(str(N)):
        if i < L - 1:
            res += int(v) * (9 ** (L - 2 - i)) * 8
        else:
            for i in range(N - N % 10, N + 1):
                if i % 9 > 0:
                    res += 1
            # res += N % 10 + (N % 9 > N % 10)
    return res

T = int(input().strip())
for i in range(T):
    F, L = map(int,input().split())
    res = solve(F,L)
    print("Case #{0}: {1}".format(i+1, res))