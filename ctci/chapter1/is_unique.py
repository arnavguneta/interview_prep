#!/usr/bin/env python

# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Approach:
# BCR O(N) where N is the length of the string

# Function loops through the string once and creates a hashmap, O(N) runtime with O(N) space complexity
def is_unique_1(string: str) -> bool:
    letters_seen = dict()
    for char in string:
        if char in letters_seen:
            return False
        letters_seen[char] = True
    return True

# Function loops through the string once and creates a boolmap for every possible ascii character, O(N) runtime with O(n) space complexity (n is number of all possible characters)
def is_unique_2(string: str) -> bool:
    # 128 ASCII characters
    chars = [False for _ in range(128)]
    for char in string:
        if chars[ord(char)]:  # letter found before
            return False
        chars[ord(char)] = True
    return True

# Approach 1 used a hashmap/dict and approach 2 did not use any addition data structures. In the worst case, the hashmap would be as large as the boolean map in approach 2.


print(is_unique_1("bldkahtu"))
print(is_unique_2("hb 627jh=j ()"))
