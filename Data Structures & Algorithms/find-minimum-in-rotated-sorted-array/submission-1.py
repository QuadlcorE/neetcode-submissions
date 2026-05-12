class Solution:
    def findMin(self, nums: List[int]) -> int:
        # simply perform a binary search on the nums
        # We know that if we have a list 
        # [3,4,5,6,1,2]
        #  l   m     r

        # So if the l and m values are in the same section we know the min value is on the right segment.
        # But if r and m values are in the same section then min value is in the left segment. 
        # How do we know if two of them are in the same segment?
        # we keep performing binary search while l>r
        # We search the right side if l_value < m_value
        # We search the left side if the m_value < r_value

        # when l==r return that value

        l, r = 0, len(nums)-1
        M = nums[0]


        while l <= r:
            if nums[l] < nums[r]:
                M = min(M, nums[l])
                break
            
            m = (l+r)//2
            M = min(M, nums[m])
            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1
        
        return M