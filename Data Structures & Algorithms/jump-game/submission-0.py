class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Clearly a backtracking problem we check if a square can reach a square that can reach the end of the array.
        n = len(nums)
        goal = n-1

        for i in range(goal -1, -1, -1):
            # we cycle back
            if nums[i] + i >= goal:
                goal = i
        
        if goal == 0:
            return True
        return False