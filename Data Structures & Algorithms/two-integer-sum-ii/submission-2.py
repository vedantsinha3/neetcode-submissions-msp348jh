class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right: 
            add = numbers[right] + numbers[left]

            if add > target and left < right:
                right -=1
                add = numbers[right] + numbers[left]

            if add < target and left < right: 
                left +=1
                add = numbers[right] + numbers[left]

            if add == target: 
                return [left + 1, right + 1]


        
        