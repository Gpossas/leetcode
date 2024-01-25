class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            else:
                sell = price - buy
                max_profit = max(max_profit, sell)
        return max_profit