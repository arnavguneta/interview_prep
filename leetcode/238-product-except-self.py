class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 1
        answer = [1 for x in nums]
        for i in range(len(nums)):
            answer[i] = sum
            sum *= nums[i]
        sum = 1
        for i in range(len(nums)-1,0,-1):
            sum *= nums[i]
            answer[i-1] *= sum
        return answer