class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = l+1
        prof = 0
        
        while r < len(prices):
            prof = max(prices[r]-prices[l], prof)
            while prices[l] > prices[r] and l<r:
                l += 1
            r+=1
        
        return prof