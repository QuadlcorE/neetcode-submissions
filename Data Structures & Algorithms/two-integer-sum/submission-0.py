class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, entry in enumerate(nums):
            if (hashmap.get(target-entry) != None):
                result = [hashmap[target-entry], i]
                return result
            hashmap[entry] = i