class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or len(t) > len(s):
            return ""

        t_count = {}
        window = {}

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        
        need = len(t_count)
        have = 0
        left = 0
        resLen = float('inf')
        res = [-1, -1]

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have += 1

            while need == have:
                if right - left + 1 < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -=1

                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1

                left +=1

        left, right = res

        return s[left:right + 1] if resLen != float('inf') else ""

        


            


        