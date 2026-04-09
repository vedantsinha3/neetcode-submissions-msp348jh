class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            # Sort each word and use the sorted version as the key
            key = "".join(sorted(word))

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        # Return just the grouped anagrams
        return list(hashmap.values())
