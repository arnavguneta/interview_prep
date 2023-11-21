import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        l, r = 1, max(piles) # bin search of all possible values of banana/hour
        res = r # worst case, min banana/hour will be max banana in all piles
        while l <= r:
            k = l + (r-l)//2
            time_taken = sum(math.ceil(pile / k) for pile in piles)
            if time_taken <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
sol = Solution()
assert sol.minEatingSpeed(piles = [3,6,7,11], h = 8) == 4