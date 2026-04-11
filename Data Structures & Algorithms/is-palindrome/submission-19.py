class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.strip().lower()
        left = 0
        right = len(s) - 1


        while left < right:

            while s[left].isalnum() == False and left < right:
                print(s[left])
                left += 1

            while s[right].isalnum() == False and left < right:
                print(s[right])
                right -= 1
            
            if s[right].lower() != s[left].lower():
                return False
            
            left +=1
            right -=1

        return True





