def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = {}
    for i in nums:
        if i in seen: 
            return True
        else:
            seen[i] = 1
    return False
