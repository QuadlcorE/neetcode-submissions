class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Just need to go through and check for an overlap. Remove the overlap with the greater end range. 
        # We don't need to remove it just somehow keep track that it's been removed. 
        # We somehow need to keep track of the last interval we've seen tho
        # Also something worth nothing is that sort would sort it based on the first interval then the second for conflicts
        # So lets get started. 

        if len(intervals) <2:
            return 0
        
        removed = 0
        intervals.sort() # Here we have O(n log(n))

        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # for each interval we basically want to check if there was an overlap
            if start < lastEnd:
                # overlap existed, now we remove the one with the farther end value
                # basically we keep the minimum between both end and the previous endvalues
                removed += 1
                lastEnd = min(lastEnd, end)
            else:
                # we need to update the last end value
                lastEnd = end
        
        return removed