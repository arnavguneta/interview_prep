#!/usr/bin/env python

# Given two strings, write a method to decide if one is a permutation of the other.

# Approach:
# BCR O(N) where N is the length of the string

# Function accepts two strings, and checks wether or not they are permutations of each other
def check_permutation(first_str: str, second_str: str) -> bool:
    # both strings have to be of the same length
    if len(first_str) != len(second_str): 
        return False
    # both strings need to have the same amount of characters
    first_map = get_char_map(first_str)
    second_map = get_char_map(second_str)
    if not compare_maps(first_map, second_map):
        return False
    return True

# Convert the string into a character map with a character counter as the value, could be done better with the Counter class
def get_char_map(string: str) -> dict:
    char_count = dict()
    for char in string:
        char_count[char] =  0 if char not in char_count else char_count[char] + 1 
    return char_count

# Compares the two maps to see if the strings have the same characters, could subtract values from second map from the first map as an improvement
def compare_maps(first_map: dict, second_map: dict) -> bool:
    for char in first_map:
        # both strings need to have the same number of each character
        if first_map[char] != second_map[char]:
            return False
    return True

print(check_permutation('wef34d', 'wffe3a'))