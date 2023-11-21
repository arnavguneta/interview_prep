class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            print('before', l,m,r)
            if nums[m] == target: return m
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
        print('after', l,m,r)
            
        return -1
sol = Solution()
assert sol.search([-1,0,3,5,9,12], 9) == 4
assert sol.search([-1,0,3,5,9,12], 10) == -1
assert sol.search([-1,1], -1) == 0
