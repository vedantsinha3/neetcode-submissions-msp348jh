class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashm = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashm:
                return [min(hashm[difference], i), max(hashm[difference], i)]

            hashm[nums[i]] = i
        