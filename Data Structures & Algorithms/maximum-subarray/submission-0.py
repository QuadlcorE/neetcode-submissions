class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Yeah Kadanes algoritm
        curr = 0
        maxSum = max(nums)

        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            maxSum = max(curr, maxSum)
        
        return maxSum