class Solution:
    def rob(self, nums: List[int]) -> int:
        # What exactly is the difference tho?
        # We know there are two win condition arrays 
        # So we just need to get the max of these arrays. 
        # What is the minimum number of houses?

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        cache = {}
        
        def robbery(house, end):
            # If we used house we pass true to the next function.
            # Else we don't pass it. 
            # Now what do we need to do we need the max between the last node. 
            if house >= end:
                return 0
            if house in cache:
                return cache[house]
            
            cache[house] = max(robbery(house+1, end), robbery(house+2, end) + nums[house])
            return cache[house]

        # We definitely would need two caches to build it
        cycle1 = robbery(0, len(nums)-1)
        cache = {}
        cycle2 = robbery(1, len(nums))

        return max(cycle1, cycle2)