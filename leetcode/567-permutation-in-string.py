class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        left = 0
        char_info = {}
        for c in s1:
            char_info[c] = char_info.get(c, 0) + 1
        observed = {} # (original idx)
        for right, cur_c in enumerate(s2):
            cur_obs = observed.get(cur_c, (right, 1))
            print('new', right, cur_c, left, observed)
            
            if cur_c not in char_info:
                left = right + 1
                observed = {}
                print('not in',right, cur_c, left, observed)
            elif cur_obs[1] > char_info[cur_c]:
                left = max(observed.get(cur_c, (right, 1))[0] + 1, left+1)
                observed[cur_c] = (right, 1)
                print('too many', right, cur_c, left, observed)
            else:
                observed[cur_c] = (observed[cur_c][0],observed[cur_c][1]+1) if cur_c in observed else (right, 1)
                print('obs', right, cur_c, left, observed)
            if right - left + 1 == len(s1): return True
        return False

sol = Solution() 
# assert sol.checkInclusion("ab","eidbaooo") == True
# assert sol.checkInclusion("ab","eidboaoo") == False
assert sol.checkInclusion("hello","ooolleoooleh") == False
assert sol.checkInclusion("adc","dcda") == True
