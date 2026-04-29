class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 # we start at 1 because that is the smallest k val we can have
        right = max(piles) # the right or the end of our search space is the largest pile 
                            #since we know for sure that we can eat all bananas in this k val

        
        while left < right:
            k = (left + right) // 2 # we make k the current value we are experimenting with
            total_hours = 0 #variable to track the current total hours it takes based off k val

            for pile in piles:
                total_hours += math.ceil(pile/k) #iterate through piles and see how long it will
                                                #take based off our current k value

            if total_hours <= h: #check to see if our current pace of eating piles of bananas 
                                #takes less time to consume than the time limit 
                right = k #if it does then we want to see if there are any possible smaller vals

            else: #other wise we just want to find a value that works so we need bigger nums
                left = k + 1
        
        return left #