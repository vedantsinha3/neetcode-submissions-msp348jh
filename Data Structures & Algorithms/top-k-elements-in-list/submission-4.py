class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1

        arr = []
        for num, val in h.items():
            arr.append([val, num])


        arr.sort(reverse = True)

        print(arr)
        
        i = 0
        while k > 0:
            res.append(arr[i][1])
            k -=1
            i +=1

        return res