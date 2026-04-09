class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_str = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1

            seen.add(s[right])
            longest_str = max(longest_str, right - left + 1)

        return longest_str

            