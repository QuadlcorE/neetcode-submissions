class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = sorted(nums)
        for i in range(len(arr)):
            if i>0 and arr[i] == arr[i-1]:
                continue

            l = i+1
            r = len(arr)-1
            while l<r:
                sum = arr[l] + arr[r] + arr[i]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    sol = [arr[i], arr[l], arr[r]]
                    res.append(sol)
                    l+=1
                    while l<r and arr[l] == arr[l-1]:
                        l+=1
                
        
        return res