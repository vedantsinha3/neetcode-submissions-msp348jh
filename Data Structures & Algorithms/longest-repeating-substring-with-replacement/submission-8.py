class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_len = 0
        max_item = 0
        h = {}

        for right in range(len(s)):
            h[s[right]] = h.get(s[right], 0) + 1
            max_item = max(h[s[right]], max_item)
            while (right - left + 1) - max_item > k:
                h[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        