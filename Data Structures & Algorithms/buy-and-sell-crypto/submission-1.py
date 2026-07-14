class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to store the minimum price and the maximum profit
        min_price = float('inf')
        max_profit = 0

        # Iterate through the prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if we sell at the current price and update the maximum profit if it's higher
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
           
            


