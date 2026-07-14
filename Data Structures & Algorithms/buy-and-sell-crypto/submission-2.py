class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0


        for sell in range(1, len(prices)):
            if prices[sell] < buy:
                buy = prices[sell]
            else:
                profit = prices[sell] - buy
                max_profit = max(max_profit, profit)
        return max_profit
