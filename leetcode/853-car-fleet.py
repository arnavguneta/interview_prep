class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        stack = []
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        for p,s in pairs:
            stack.append((target-p)/s) # hours to get to location, with the closest car being evaluated first
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # iff newly added eta is same or faster than a car further ahead of it, treat it as same fleet
                stack.pop()
        return len(stack)
      
sol = Solution()
assert sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3