class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        l, r = 0, len(height) - 1
        while l < r:
            max_val = max(max_val, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_val
        