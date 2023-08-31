class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s.lower() if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57)])
        for i in range(len(s) // 2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True