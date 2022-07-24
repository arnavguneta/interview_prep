# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i in range(0, len(nums)):
        value = str(nums[i])
        if value in lookup: lookup[value].append(i) 
        else: lookup[value] = [i]
    for i in range(0, len(nums)):
        missing = str(target - nums[i])
        if missing in lookup:
            if i != lookup[missing][-1]: return [i, lookup[missing][-1]] 
            continue

print(twoSum([3,3], 6))