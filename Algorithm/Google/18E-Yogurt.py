'''
Yogurt
N cups of yogurt,
expire [A1,A2,...,Ai] days
K cups / day

Output:
Case #x: y
y: maximum number of cups of yogurt

先排序。
每天尽可能多喝，且快过期的先喝。

4
2 1
1 1
5 1
3 2 3 2 3
2 2
1 1
6 2
1 1 1 7 7 7
'''

def slove(N,K,l):
    l.sort()
    day = N
    cur = 0
    total = 0
    for d in range(1,day+1):
        k = 0
        # 没过期
        while cur < len(l):
            # 吃得下
            if k < K:
                if l[cur] >= d:
                    # 吃掉
                    cur += 1
                    total += 1
                    k += 1
                    continue
                else:
                    cur += 1
            else:
                # 吃不下了
                break
    return total

if __name__ == "__main__":
    # Test Case Number
    T = int(input().strip())
    
    # Each Test Case
    for i in range(T):
        N, K = map(int,input().split())
        l = list(map(int, input().split()))
        max_cups = slove(N, K, l)
        print("Case #{0}: {1}".format(i+1, max_cups))
    
    # Test
    # N = 6
    # K = 2
    # l = [1,1,1,7,7,7]
    # max_cups = slove(N, K, l)