class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or len(t) > len(s):
            return ""

        t_count = {}

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        window = {}
        resLen = float('inf')
        res = [-1,-1]
        need = len(t_count)
        have = 0
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have += 1

            while have == need: 
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    res = [left, right]
                
                window[s[left]] -= 1

                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -=1

                left +=1

        left, right = res
        return s[left:right + 1] if resLen != float("inf") else ""

        