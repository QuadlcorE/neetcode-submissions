class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1,2,3,10,1,6,9]
        # We simply keep it recursive at each house choosing to rob it or rob its neighbour.
        # In order to reduce the time complexity from O(2^n) we could cache the max of each house when we've seen it before.
        cache = {}

        def robbery(house):
            """ Where house is the index of the current house 
                The fuction returns the max money to be achieved from this house to the end of the street
            """
            # Base cases should be if we hit a house outside the nums
            if house >= len(nums):
                return 0
            if house in cache:
                return cache[house]
            
            # Now we decide if the rob curr house or not.
            currMax = max(robbery(house+1), robbery(house+2) + nums[house])
            cache[house] = currMax
            return currMax

        return robbery(0)