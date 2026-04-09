class Solution:
    def maxArea(self, heights: List[int]) -> int:

        right = len(heights) - 1
        left = 0
        largest_area = 0

        while left< right:
            length = right - left
            height = min(heights[left], heights[right])
            area = length * height
            largest_area = max(largest_area, area)

            if heights[left] < heights[right]:
                left +=1

            else:
                right -=1


        return largest_area


        