class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window approach
        have hashmap keeping track on freq of elements in current window
        if the min(hashmap.values()) < k -> that means window still valid and keep continuing
        keep track of longest window length
        return longest window length found
        """

        left = 0
        res = 0
        h = {}
        most_freq = 0

        for right in range(len(s)):
            h[s[right]] = h.get(s[right], 0) + 1
            most_freq = max(most_freq, h[s[right]])
            while (right - left + 1) - most_freq > k:
                h[s[left]] -= 1
                left +=1
            length = right - left + 1

        res = max(res, length)

        return res

            