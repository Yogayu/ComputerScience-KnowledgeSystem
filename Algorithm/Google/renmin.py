def is_xor_sum_even(n):
    return bin(n).count('1')%2==0

def cal_sub(left,right,sum,array,visited,modified_index):
    if visited[left][right]!=0 and modified_index<left and modified_index>right:
        return visited[left][right]
    if is_xor_sum_even(sum):
        visited[left][right] = right-left+1
    else:
        visited[left][right] =  max(cal_sub(left+1,right,sum^array[left],array,visited,modified_index),cal_sub(left,right-1,sum^array[right],array,visited,modified_index))
    return visited[left][right]


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
        visited = [[0]*N]*N
        for _ in range(K):
            index,value = map(int,input().split())
            before_value = array[index]
            array[index] = value
            init_sum = init_sum^before_value^value
            results.append(cal_sub(0,len(array)-1,init_sum,array,visited,index))
        print("Case #{0}: {1}".format(i+1," ".join(map(str,results))) )