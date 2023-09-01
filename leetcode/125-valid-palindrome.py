class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for c in s.lower():
            if c.isalnum():
                new_s += c
        for i in range(len(new_s) // 2):
            if new_s[i] != new_s[len(new_s)-1-i]:
                return False
        return True