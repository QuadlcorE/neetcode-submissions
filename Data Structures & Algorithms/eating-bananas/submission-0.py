class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We need the range for possible values of k 
        # l=1, r=maxvalue(piles)
        # we go get the curr k = maxvalue
        # loop through the range using binary search. 
        # For this binary search we want to make sure that l<=r 
        # when we find a new value for k less than h we update k

        l, r = 1, max(piles)
        k = r

        while l<=r:
            # let i be the new k
            i = (l + r)//2
            hours = 0

            for j in piles:
                hours += math.ceil(j/i)
            
            if hours <= h:
                # we want to update k 
                # then move the right pointer so we look for a smaller k value
                k = min(k, i)
                r = i-1
            else:
                # we want to look for a k value that has smaller hours to complete
                l = i+1
        
        return k
