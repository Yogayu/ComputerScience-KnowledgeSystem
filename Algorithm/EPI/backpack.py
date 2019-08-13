w = [0, 1, 4, 3, 1]
p = [0, 1500, 3000, 2000, 2000]
n = len(w) - 1
m = 4

x = []
v = 0
# optp[i][j]表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值
optp = [[0 for col in range(m+1)] for row in range(n+1)]
#optp 相当于做了一个n*m的全零矩阵，n行为物件，m列为自背包载重量

'''
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
'''
def dnapsack_dynamic(w, p, n, m, x):
    for i in range(1, n+1): # 物品一件件来
        for j in range(1, m+1): # j为子背包的载重量，寻找能够承载物品的子背包
            if j >= w[i]:
                # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
                optp[i][j] = max(optp[i-1][j],optp[i-1][j-w[i]] + p[i])
            else:
                optp = optp[i-1][j]

    #递推装入背包的物体,寻找跳变的地方，从最后结果开始逆推
    j = m
    for i in range(n, 0, -1):
        if optp[i][j] > optp[i-1][j]:
            x.append(i)
            j = j - w[i]
    return optp[n][m]