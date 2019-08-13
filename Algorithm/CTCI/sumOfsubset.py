# sumOfsubset
# {2, 4, 6, 10}
'''
def sumofSubset(init_set, number):
    count = 0
    count = _sumOfsubset(init_set, number, count)
    return count

def _sumOfsubset(init_set, number, count):
    print(init_set, number)
    if len(init_set) == 0: return None
    if init_set[0] == number: return count + 1
    print(init_set)
    for index, number in enumerate(init_set):
        print(index, number)
        number = number - init_set[index]
        if number < 0:return count
        init_set.pop(index)
        _sumOfsubset(init_set, number, count)

def main():
    init_set = [2, 4, 6, 10]
    target_number = 16
    count = sumofSubset(init_set, target_number)
    print(count)
'''

def count_sets(arr, total):
    return rec(arr, total, len(arr)-1)

def rec(arr, total, i):
    if total == 0: return 1
    if total < 0 or i < 0: return 0
    if total < arr[i]:
        return rec(arr, total, i-1)
    else:
        return rec(arr, total-arr[i], i-1) + rec(arr, total, i-1)

def count_sets_dp(arr, total):
    mem = {}
    return dp(arr, total, len(arr)-1, mem)

def dp(arr, total, i, mem):
    key = str(total) + ':' + str(i)
    if key in mem:
        return mem[key]
    if total == 0: return 1
    if total < 0 or i < 0: return 0
    if total < arr[i]:
        return dp(arr, total, i-1, mem)
    else:
        result = dp(arr, total-arr[i], i-1, mem) + dp(arr, total, i-1, mem)
    mem[key] = result
    return result
    
if __name__ == '__main__':
    count = count_sets([2,4,6,10,1,1,1,1,3,4,5,12], 16)
    
    print(count)

    count = count_sets_dp([2,4,6,10,1,1,1,1,3,4,5,12], 16)

    print(count)
