class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap: 
                return [min(i, hashmap[compliment]), max(i, hashmap[compliment])]

            else: 
                hashmap[nums[i]] = i 