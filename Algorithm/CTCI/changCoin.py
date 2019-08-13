'''
@author: youxinyu
@date: 2018-9-9
'''

def changCoin(coins, money):

    return _changCoin(coins, money, 0, {})

def _changCoin(coins, money, index, memoriz):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0
    
    key = str(money) + '-' + str(index)
    if key in memoriz:
        return memoriz[key]

    ways = 0
    remained = money
    while remained >=0:
        ways += _changCoin(coins, remained, index+1, memoriz)
        remained -= coins[index]

    memoriz[key] = ways
    return ways


def main():
    ways = changCoin([12,6],12)
    print(ways)

if __name__ == '__main__':
    main()

    # ways = 0
    # remained = money
    # while remained <= money:
    #     remained = remained - coins[index]
    #     ways += _changCoin(coins, remained, index+1, memoriz)

    # ways = 0
    # total = money
    # while money >= total:
    #     ways += _changCoin(coins, total, index+1, memoriz)
    #     total += coins[index]

# ways = 0
#     coinTotal = 0
#     while coinTotal <= money:
#         remained = money - coinTotal
#         ways += _changCoin(coins, remained, index+1, memoriz)
#         coinTotal += coins[index]
