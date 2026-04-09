class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create hashmap
        #create [] to store answer
        #iterate through nums
        #add nums to hashmap along with freq
        #sort hashmap by descending order (most freq at top, least freq at bottom)
        #return k most frequently occuring elements

        hashmap = {}
        ans = []

        for num in nums: 
            hashmap[num] = 1 + hashmap.get(num, 0)

        arr = []
        for num, count in hashmap.items():
            arr.append([count, num])
        arr.sort(reverse = True)

        for i in range(k):
            ans.append(arr[i][1])

        return ans
