class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        found_min = float("inf")
        while l <= r:
            m = l + (r-l)//2
            found_min = min(found_min, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m -1
        return min(found_min, nums[l])
        
sol = Solution()
assert sol.findMin(nums = [3,4,5,1,2]) == 1
assert sol.findMin(nums = [3,4,0,1,2]) == 0
assert sol.findMin(nums = [4,5,0,1,2,3]) == 0

