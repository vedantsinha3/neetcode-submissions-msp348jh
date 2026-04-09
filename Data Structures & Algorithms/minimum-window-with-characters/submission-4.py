class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s) or not s:
            return ""

        t_count = {}

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        
        left = 0
        window = {}
        have = 0
        need = len(t_count)
        res = [-1,-1]
        resLen = float("inf")
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have += 1

            while need == have:
                if right - left + 1 < resLen:
                    resLen = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1

                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -=1

                left +=1

        left, right = res

        return s[left:right + 1] if res != float('inf') else ""


            


        
        