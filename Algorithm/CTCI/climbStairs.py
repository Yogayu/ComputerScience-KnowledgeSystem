'''
@author: youxinyu
@date: 2018-8-29
'''


def re_num_ways(n):
    if n == 0 or n == 1:
        return 1
    return re_num_ways(n-1) + re_num_ways(n-2)


def num_ways(n):
    steps = [1, 1]
    for i in range(2, n+1):
        steps.append(steps[i-1]+steps[i-2])
    return steps[n]


def num_ways_x(n, x):
    steps = [0 for i in range(0, n+1)]
    steps[0] = 1

    for i in range(1, n+1):
        total = 0
        for j in x:
            if i - j >= 0:
                total += steps[i-j]
        steps[i] = total
    return steps[n]


def main():
    x = [1, 3, 5, 8]
    for i in range(1, 10):
        # print(re_num_ways(i))
        # print(num_ways(i))
        print(num_ways_x(i, x))


if __name__ == '__main__':
    main()
