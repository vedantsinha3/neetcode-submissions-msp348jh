class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        best_profit = 0
        for i in range(len(prices)):
            if prices[i] < low: 
                low = prices[i]

            if prices[i] - low > best_profit:
                best_profit = prices[i] - low

        return best_profit

        