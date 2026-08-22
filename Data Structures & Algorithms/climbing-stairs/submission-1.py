class Solution:
    def climbStairs(self, n: int) -> int:
        # We could recursively sum the number of ways to get to each individual step in a solution
        # So for the final step we would want to find the summ of ways to climb the steps that can reach it.
        # lets say we have 4 steps
        # 0   1,       2,       3,        4
        #     (1)    (1, 0)   (1, 2)   (2,3)
        # 0    1       2         3       5

        # so our base cases would be for steps 1 and 2
        # For every other step we return the sum of the step-1 and step-2
        # BRUTE FORCE SOLUTION!

        # if n == 0:
        #     return 1
        # if n == 1 or n == 2:
        #     return n
        
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # Now this might be too inefficient so how about we cache different solutions?

        # We define a function and then have a cache. 
        cache = {
            0:1,
            1:1,
            2:2,
            }
        def calculateWays(t):
            if t in cache:
                return cache[t]
            res = calculateWays(t-1) + calculateWays(t-2)
            cache[t] = res
            return res
        
        return calculateWays(n)
