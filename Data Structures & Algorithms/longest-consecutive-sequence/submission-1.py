class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Example [2, 20, 4, 10, 3, 4, 5]

        # Example [0,3,2,5,4,6,1,1]

        # dis = set{}
        dis = set(nums)
        cur = 0
        largest = cur

        for n in nums:
            if n-1 not in nums:
                cur += 1
                x = n
                while x+1 in nums:
                    x += 1
                    cur += 1
                if cur > largest:
                    largest = cur 
                cur = 0
        
        return largest