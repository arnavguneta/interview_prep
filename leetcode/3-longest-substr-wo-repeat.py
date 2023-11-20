class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            print('cur r', right)
            if s[right] in hash:
                left = hash[s[right]] + 1                   # move left pointer to after the last occurence of repeated character
            max_len = max(max_len, right - left + 1)
            hash[s[right]] = right                          # set hash with cur char and cur idx
        return max_len

sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))
# print(sol.lengthOfLongestSubstring("bbbbb"))
# print(sol.lengthOfLongestSubstring("pwwkew"))
# print(sol.lengthOfLongestSubstring("dvdf"))
print(sol.lengthOfLongestSubstring("abba"))

# assert sol.lengthOfLongestSubstring("abba") == 2


