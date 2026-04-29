class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = {}

        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1

        arr = []

        for num, freq in h.items():
            arr.append([freq, num]) 

        arr.sort(reverse= True)

        res = []
        i = 0

        while i < k: 
            
            res.append(arr[i][1])
            i +=1

        return res