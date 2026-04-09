class Solution:
    def trap(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0

        total = 0

        maxRight = height[right]
        maxLeft = height[left]

        if not height: 
            return 0

        while left < right:

            if maxRight < maxLeft: 
                right -=1
                maxRight = max(maxRight, height[right])
                total += maxRight - height[right]

            else: 
                left +=1
                maxLeft = max(maxLeft, height[left])
                total += maxLeft - height[left]

        return total 
        