def num_ways(num_str):
    mem = [None for i in range(0,len(num_str)+1)]
    return helper(num_str, len(num_str), mem)

def helper(num_str, k, mem):
    if k == 0: return 1
    start = len(num_str) - k
    if num_str[start] == 0: return 0
    
    if mem[k]:
        return mem[k]

    count = helper(num_str, k-1, mem)
    if k >=2 and int(num_str[start:start+2]) < 27:  # two number letter
        count += helper(num_str,k-2, mem)
    mem[k] = count
    return count
     
def main():
    print(num_ways('180121'))

if __name__ == '__main__':
    main()