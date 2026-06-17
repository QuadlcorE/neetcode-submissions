class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Since each item contains integers within the range of 1, n
        # First are they in order? 
        # Such that nums[i] = i+1?
        # If they are then we just loop through and make that comparison. 
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            nums[abs(nums[i])] *= -1