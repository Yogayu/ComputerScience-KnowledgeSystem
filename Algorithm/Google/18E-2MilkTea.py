def slove(pref, forbtn, N):
    min_cp = 0
    return min_cp
    
if __name__ == "__main__":
    # Test Case Number
    T = int(input().strip())
    N, M, P = map(int,input().split())
    
    for i in range(T):
        pref = []
        for _ in range(N):
            pref.append(str(input().strip()))
        forbtn = []
        for _ in range(M):
            forbtn.append(str(input().strip()))
        
        min_cp = slove(pref, forbtn, N)
        
        print("Case #{0}: {1}".format(i+1, min_cp))        
