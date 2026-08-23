class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        def ways(n):
            # base case
            if n < 3:
                return n 
            
            if n in cache:
                return cache[n]
            
            result = ways(n-1) + ways(n-2)
            cache[n] = result
            
            return result
        
        return ways(n)