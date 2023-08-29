class Solution:
    def groupAnagrams(self, strs):
        out = {}
        for anagram in strs:
            sorted_anagram = "".join(sorted(anagram))
            if sorted_anagram in out:
                out[sorted_anagram].append(anagram)
            else:
                out[sorted_anagram] = [anagram]
        return [val for key, val in out.items()]
    
# can use tuple as dictionary keys!
# optimal solution to use tuple as keys, O(m * n) where m is size of list and n is size of word, space O()