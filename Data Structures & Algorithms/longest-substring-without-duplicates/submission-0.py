class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_length = 0

        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1

            seen.add(s[right]) 
            length = right - left + 1
            longest_length = max(length, longest_length)

        return longest_length
        

        