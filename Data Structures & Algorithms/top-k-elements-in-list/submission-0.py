class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)


        # sorted_items = sorted(hashmap.items(), key= lambda x: x[1], reverse = True )
        # return [item[0] for item in sorted_items[:k]]

        arr = []
        for num, cnt in hashmap.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k: 
            res.append(arr.pop()[1])
        return res


