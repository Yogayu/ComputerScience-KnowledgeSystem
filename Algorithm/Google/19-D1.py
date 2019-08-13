'''
T
N array大小 Q修改次数
0 1 2 ... N-1
P1 V1
P2 V2
P3 V3
...
Pi Vi(i=Q)
'''

def xor_even(l):
    # xor_sum
    res = l[0]
    for i in range(1,len(l)):
        res = res ^ l[i]
    is_even = bin(res)[2:].count('1')
    # xor_even
    if is_even % 2 == 0:
        return True
    else:
        return False

def max_sub(A):
    if len(A) < 2: return 0

    max_record = 0
    for i in range(len(A)-1):
        if max_record == len(A):
            return max_record
        l,r = i, i+1
        while r < len(A)+1:
            is_even = xor_even(A[l:r])
            if is_even:
                max_record = max(max_record, r-l)
            # print(is_even, A[l:r], max_record)
            r += 1

    return max_record

def slove(N,Q,A,modif):
    max_num_list = []
    for md in modif:
        i = int(md[0])
        A[i] = md[1]
        max_num_list.append(max_sub(A))
    return max_num_list

T = int(input().strip())
for i in range(T):
    N, Q = map(int,input().split())
    A = list(map(int, input().split()))
    
    modif = []
    for _ in range(Q):
        modif.append(list(map(int, input().split())))
    max_num_list = slove(N,Q,A,modif)

    max_list = " ".join(map(str,max_num_list))
    # 需要修改max num list 为str
    print("Case #{0}: ".format(i+1) + max_list)