# coding=utf-8
def solve_small(a, b, c):
    return res
def solve(a, b, c):
    return res

def getInput():
    # first line
    T = int(input().strip())
    # split next lines input
    for i in range(T):
        a, b, c = map(int,input().split())

        # res = solve(a, b, c)
        # print("Case #{0}: {1}".format(i+1, res))
        print("Case #{0}: {1}".format(i+1, a))
'''
2
5
1 2
2 3
3 4
2 4
5 3
Case #1: [(1, 2), (2, 3), (3, 4), (2, 4), (5, 3)]
3
1 2
3 2
1 3
Case #2: [(1, 2), (2, 3), (3, 4), (2, 4), (5, 3), (1, 2), (3, 2), (1, 3)]
'''
def main():
    # Test Case Number
    T = int(input().strip())
    eage = []
    for i in range(T):
        # 行数
        n = int(input().strip())
        for j in range(n):
            x,y  = map(int,input().split())
            eage.append((x,y))
        
        print("Case #{0}: {1}".format(i+1,eage))

if __name__ == "__main__":
    main()
