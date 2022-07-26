# 9. Palindrome
# https://leetcode.com/problems/palindrome-number/
#
#  Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

def isPalindrome(x):
    s_x = str(x)
    len_s_x = len(s_x)
    if len_s_x == 2:
        return s_x[0] == s_x[1]
    for idx in range(0, int(len_s_x / 2)):
        if s_x[idx] != s_x[len_s_x - idx - 1]:
            return False
    return True


out = isPalindrome(1000030001)
print(out)
