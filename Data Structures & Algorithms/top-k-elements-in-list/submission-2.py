class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashm = {}

        for i in range(len(nums)):
            hashm[nums[i]] = hashm.get(nums[i], 0) + 1

        arr = []

        for num, count in hashm.items():
            arr.append([count, num])
        arr.sort(reverse = True)

        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res



        