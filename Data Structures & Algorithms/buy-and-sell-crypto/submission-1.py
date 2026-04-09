class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_price = prices[0]

        for i in range(len(prices)): 
            if prices[i] < curr_price:
                curr_price = prices[i]

            else:
                curr_profit = prices[i] - curr_price
                max_profit = max(curr_profit, max_profit)

        return max_profit
            
        