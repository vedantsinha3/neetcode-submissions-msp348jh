class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best_count = 0

        for x in nums:
            if x - 1 in nums: 
                continue
            curr_count = 1
            while x + 1 in nums:
                curr_count +=1
                x+=1
            
            best_count = max(best_count, curr_count)

        return best_count

        