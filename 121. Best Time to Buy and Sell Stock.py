class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum_bought_stock = prices[0]
        max_profit = 0
        for price in prices:
            if price < minimum_bought_stock:
                minimum_bought_stock = price
            else:
                profit = price - minimum_bought_stock
                if profit > max_profit:
                    max_profit = profit
        return max_profit