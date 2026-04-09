class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in (strs):
            s += str(len(word)) + "#" + word

        return s

    def decode(self, s: str) -> List[str]:

        i = 0
        ans = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1

            else: 
                length = int(s[i:j])
                i = j + 1
                j = (length) + i 
                ans.append(s[i:j])

            i = j

        return ans


