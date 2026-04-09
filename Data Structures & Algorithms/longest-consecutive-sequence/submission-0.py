class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)

        best_len = 0

        for x in seen: 
            if x - 1 not in seen: 
                curr = x 
                length = 1
                while curr + 1 in seen:
                    length +=1
                    curr = curr + 1
                best_len = max(length, best_len)

        return best_len

                