class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we are return indices in an array
        # we just need the indexes 
        # we know it in order 
        # we l and r 
        l = 0 
        r = len(numbers) -1 
        # is there always a solution?
        while l<r:
            solm = numbers[l] + numbers[r]
            if solm == target:
                return [l+1, r+1]
            elif solm < target: 
                l+=1 
            else:
                r-=1