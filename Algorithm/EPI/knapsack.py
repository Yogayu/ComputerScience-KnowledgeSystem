def MF_knapsack(i, wt, val, j):
    global F
    if F[i][j] < 0:
        if j < wt[i-1]:
            val = MF_knapsack(i - 1, wt, val, j)
        else:
            without_new = MF_knapsack(i - 1, wt, val, j)
            with_new = MF_knapsack(i - 1, wt, val, j - wt[i-1] + val[i]-1)
            val = max(with_new, without_new)
        F[i][j] = val
    return F[i][j]
    
def knapsack(W, wt, val, n):
    dp = [[0 for col in range(W+1)] for row in range(n+1)]
    '''
    dp
        0  1  2  3  4  5  6 背包重量 W
    0 [[0, 0, 0, 0, 0, 0, 0],
    1  [0, 0, 0, 0, 0, 0, 0],
    2  [0, 0, 0, 0, 0, 0, 0],
    3  [0, 0, 0, 0, 0, 0, 0], 
    4  [0, 0, 0, 0, 0, 0, 0]]
    物品
    n
    '''

    for i in range(1, n+1):
        for w in range(1, W+1):
            # 注意点：for i in range(1, n+1)这里 i 是指第几个物品，
            # 然而 wt 和 val 中第 i 个物品的下标是 i-1
            index = i -1
            if wt[index] <= w:  # 放得下
                # 不放新物品时价值
                without_new = dp[i-1][w]
                # 放新物品时剩余重量的背包(w-wt[index])的最大价值
                # dp[i-1][w-wt[i]] + 该物品价值
                with_new = dp[i-1][w-wt[index]] + val[index]
                dp[i][w] = max(with_new, without_new)
            else:   # 放不下
                dp[i][w] = dp[i-1][w]
    max_val = dp[n][w]

    return max_val

if __name__ == "__main__":
    val = [3, 2, 4, 5]
    wt = [4, 3, 2, 3]
    n = 4
    W = 6
    F = [[0]*(W+1)] + [[0] + [-1 for i in range(W+1)] \
                                 for j in range(n + 1)]
    print(F)
    print(knapsack(W, wt, val, n))

    # [[0, 0, 0, 0, 0, 0, 0], 
    #  [0, -1, -1, -1, -1, -1, -1, -1], 
    #  [0, -1, -1, -1, -1, -1, -1, -1], 
    #  [0, -1, -1, -1, -1, -1, -1, -1], 
    #  [0, -1, -1, -1, -1, -1, -1, -1], 
    #  [0, -1, -1, -1, -1, -1, -1, -1]]
    