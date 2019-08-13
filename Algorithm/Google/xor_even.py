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
if __name__ == "__main__":
    print(xor_even([10,21,3,7]))