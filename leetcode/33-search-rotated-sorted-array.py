class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            print('cur', l, m, r)
            if nums[m] == target: return m
            if nums[m] > nums[l]:
                if target > nums[m] or target < nums[r]:
                    l = m + 1
                else: 
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
sol = Solution()
assert sol.search(nums = [5,1,3], target = 5) == 0