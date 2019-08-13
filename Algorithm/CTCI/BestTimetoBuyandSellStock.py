#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

def main():
    print(Solution().maxProfit([7,1,5,3,6,4]))

if __name__ == '__main__':
    main()
