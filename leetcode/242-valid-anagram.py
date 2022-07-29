# https://leetcode.com/problems/valid-anagram/

def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return
        
        original = {}
        
        # populate the hash
        for letter in s:
            original[letter] = 1 if letter not in original else original[letter] + 1
        
        # check for similarity
        for letter in t:
            try:
                original[letter] -= 1
                # if original[letter] < 0: return False # extra letter that wasnt in string s
            except:
                return False # if letter didnt exist on string s

        for letter in original:
            if original[letter] != 0: return False
            
        return True
        
