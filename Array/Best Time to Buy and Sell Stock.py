"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""


class Solution(object):
    def maxProfit1(self, prices: List[int]) -> int:
        minimum = prices[0]
        diff = 0
        for i in prices:
            diff = max(diff, i - minimum)
            minimum = min(i, minimum)
        return diff

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0 for __ in range(len(prices))]
        minPrice = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            if (minPrice > prices[i]):
                minPrice = prices[i]
        return dp[-1]

    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if not prices : return 0
        # min_price = prices[0]
        # max_profit = 0
        # for x in prices :
        #    if x < min_price :
        #        min_price = x
        #    elif x - min_price > max_profit :
        #        max_profit = x - min_price
        # return max_profit
        max_profit = 0
        max_val = 0

        for x in reversed(prices):
            max_val = max(max_val, x)
            if max_val - x > max_profit:
                max_profit = max_val - x
        return max_profit



so=Solution()
print(so.maxProfit([7,1,5,3,6,4]))

