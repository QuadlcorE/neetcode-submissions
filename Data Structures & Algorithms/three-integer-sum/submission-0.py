class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, entry in enumerate(nums):
            if i>0 and entry == nums[i-1]:
                continue

            l = i +1
            r = len(nums) - 1

            while l < r:
                sol = entry + nums[l] + nums[r]
                if sol > 0:
                    r -=1
                elif sol < 0:
                    l +=1
                else:
                    result.append([entry, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l - 1] and l<r:
                        l +=1 
        
        return result