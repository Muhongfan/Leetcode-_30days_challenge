"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
# s0 -> s0
# s0 -> s1
#       s1 -> s2
def maxProfit(prices):
    if not prices: return 0
    prev_sell = 0
    curr_sell = 0
    hold = -prices[0]
    for i in range(1, len(prices)):
        temp = curr_sell
        curr_sell = max(curr_sell, hold + prices[i])
        hold = max(hold, (prev_sell if i >= 2 else 0) - prices[i])
        prev_sell = temp
    return curr_sell

def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        have0_stay = 0
        have1_stay = -prices[0]
        have0_buy = -prices[0]
        have1_sell = 0
        for i in range(1, len(prices)):
            have1_stay = max(have1_stay, have0_buy)
            have0_buy = have0_stay - prices[i]
            have0_stay = max(have0_stay, have1_sell)
            have1_sell = have1_stay + prices[i]

        return max(have0_stay, have1_sell)