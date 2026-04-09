class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create default dictionary so that we dont have to manually make key value if key doesnt exist
        #iterate through strs
        #for each word there is a key -> the sorted version of all anagrams will be the same 
        #in our default dict append the word to its sorted version (key)
        #return the values of the default dict only 

        group = defaultdict(list)

        for word in strs: 
            key = ''.join(sorted(word))
            group[key].append(word)

        return list(group.values())
