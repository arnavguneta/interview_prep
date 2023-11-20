class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_map = [0] * 26
        s2_map = [0] * 26
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        l = 0
        for r in range(len(s1),len(s2)):
            if self.matches(s1_map, s2_map):
                return True
            s2_map[ord(s2[r])-ord('a')] += 1
            s2_map[ord(s2[l])-ord('a')] -= 1
            l += 1
        return self.matches(s1_map,s2_map)
    
    def matches(self, m1,m2):
        for i in range(26):
            if m1[i] != m2[i]:
                return False   
        return True
        # left = 0
        # char_info = {}
        # for c in s1:
        #     char_info[c] = char_info.get(c, 0) + 1
        # observed = {} # (original idx)
        # for right, cur_c in enumerate(s2):
        #     cur_obs = observed.get(cur_c, (right, 1))
        #     print('new', right, cur_c, left, observed)
            
        #     if cur_c not in char_info:
        #         left = right + 1
        #         observed = {}
        #         print('not in',right, cur_c, left, observed)
        #     elif cur_obs[1] > char_info[cur_c]:
        #         left = max(observed.get(cur_c, (right, 1))[0] + 1, left+1)
        #         observed[cur_c] = (right, 1)
        #         print('too many', right, cur_c, left, observed)
        #     else:
        #         observed[cur_c] = (observed[cur_c][0],observed[cur_c][1]+1) if cur_c in observed else (right, 1)
        #         print('obs', right, cur_c, left, observed)
        #     if right - left + 1 == len(s1): return True
        # return False

sol = Solution() 
# assert sol.checkInclusion("ab","eidbaooo") == True
# assert sol.checkInclusion("ab","eidboaoo") == False
assert sol.checkInclusion("hello","ooolleoooleh") == False
assert sol.checkInclusion("adc","dcda") == True
