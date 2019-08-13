def is_xor_sum_even(n):
    return bin(n).count('1')%2==0

def cal_sub(init_sum,array):
    queue = []
    queue.append((0,len(array)-1,init_sum))
    while len(queue)>0:
        (l,r,current_sum) = queue.pop(0)
        if is_xor_sum_even(current_sum):
            return r-l+1
        else:
            if l < r:
                queue.append( (l+1,r,current_sum^array[l]) )
                queue.append( (l,r-1,current_sum^array[r]) )
    return 0

def cal_xor_sum(array):
    sum = 0
    for i in range(0,len(array)):
        sum = array[i]^sum
    return sum


if __name__ == '__main__':
    # Test Case Number
    T = int(input().strip())
    # Each Test Case
    for i in range(T):
        N, K = map(int,input().split())
        array = list(map(int, input().split()))
        init_sum = cal_xor_sum(array)
        results = []
        for _ in range(K):
            index,value = map(int,input().split())
            before_value = array[index]
            array[index] = value
            init_sum = init_sum^before_value^value
            results.append(cal_sub(init_sum,array))
        print("Case #{0}: {1}".format(i+1," ".join(map(str,results))) )