class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        largest_window = 0
        left = 0
        most_freq = 0

        for right in range(len(s)):
            h[s[right]] = h.get(s[right], 0) + 1
            most_freq = max(most_freq, h[s[right]])

            while (right - left + 1) - most_freq > k: 
                h[s[left]] -=1
                left +=1

            largest_window = max(largest_window, right - left + 1)

        return largest_window
            


        