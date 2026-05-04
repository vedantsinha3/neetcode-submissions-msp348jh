class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right: 
            k = (left + right) // 2
            total_count = 0
            for pile in piles: 
                total_count += math.ceil(pile/k)

            if total_count <= h:
                right = k

            else:
                left = k + 1

        return left

        