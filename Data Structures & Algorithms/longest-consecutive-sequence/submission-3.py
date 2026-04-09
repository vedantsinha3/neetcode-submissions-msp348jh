class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        largest_count = 0

        for x in nums:
            if x - 1 in nums:
                continue

            current_count = 1
            while x + 1 in nums:
                current_count +=1
                x+=1

            largest_count = max(largest_count, current_count)

        return largest_count
        