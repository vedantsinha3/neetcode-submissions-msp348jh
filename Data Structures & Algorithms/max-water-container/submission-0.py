class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # best_area = 0
        # left = 0
        # right = len(heights) - 1

        # while left < right:
        #     length = right - left
        #     curr_area = min(heights[left], heights[right]) * length
        #     best_area = max(curr_area, best_area)
        #     if heights[left] < heights[right]:
        #         left +=1
        #     else:
        #         right -=1
                
        # return best_area

        res = 0
        best = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                length = abs(i - j)
                curr_area = min(heights[i],heights[j]) * length
                best = max(curr_area, best)

        return best

                



        