class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        curr_price = 0
        best_price = prices[0]

        for i in range(len(prices)):
            if best_price > prices[i]:
                best_price = prices[i]

            else:
                curr_price = prices[i] - best_price
                max_price = max(max_price, curr_price)

        return max_price

            

        