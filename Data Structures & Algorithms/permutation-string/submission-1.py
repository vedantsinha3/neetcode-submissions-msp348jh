class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = [0] * 26
        need = [0] * 26

        if len(s1) > len(s2):
            return False
        
        left = 0
        a = ord('a')

        for char in s1:
            need[ord(char) - a] +=1

        for right in range(len(s2)):

            window[ord(s2[right]) - a] +=1

            if right - left + 1 > len(s1):
                window[ord(s2[left]) - a] -= 1
                left +=1

            if window == need:
                return True

        return False