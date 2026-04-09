class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.strip().lower()
        left = 0 
        right = len(s) - 1

        while left < right:
            while s[left].isalnum() != True and left < right:
                left +=1

            while s[right].isalnum() != True and left < right:
                right -=1

            if s[right] != s[left]:
                return False

            right -=1
            left +=1

        return True



        