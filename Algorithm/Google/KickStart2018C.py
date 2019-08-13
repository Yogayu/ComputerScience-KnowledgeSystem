'''
尽量完成第一题，第二题和第三题的小数据
'''
'''
1. Plant Distance

N planets
N vacuum tubes 
there exists exactly one cycle in the universe

Input
T
N
Xi yi

Output
Case #x: [0,1,...,n]
'''
def solve_small():
    res = []
    return res

def main():
    # Test Case Number
    T = int(input().strip())
    
    # Each Test Case
    for i in range(T):
        # Line Nums
        n = int(input().strip())
        
        # Initialising Dictionary of edges
        g = {}
        for i in range(n):
            g[i+1] = []
        
        # Add edges
        for _ in range(n):
            x,y  = map(int, input().split())
            g[x].append(y)
            g[y].append(x)
            
            # 如果没有初始化就需要判断是否已经有 key
            # if x in g.keys():
            #     g[x].append(y)
            # else:
            #     g[x] = [y]
            # if y in g.keys():
            #     g[y].append(x)
            # else:
            #     g[y] = [x]

# // Construct the graph
        print("Case #{0}: {1}".format(i+1,g))

if __name__ == "__main__":
    main()


'''
图的表示，可以使用邻接(链)表和邻接矩阵

1. 邻接(链)表
空间复杂度 O(|V|+|E|)
2. 邻接矩阵
'''
