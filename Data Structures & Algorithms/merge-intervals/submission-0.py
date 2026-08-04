class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # We would need to sort the interval first then go through each element adding them to a new array when we meet a different overlap. 
        intervals.sort()

        curr = intervals[0]

        i = 0 
        solution = []
        
        while i<len(intervals):
            # We want to go through all the elements in the array starting from the first element
            new_interval = intervals[i]
            # if the curr end is < new_interval start we have found a new interval. 
            # add the curr to solution 
            # set curr to new_interval
            if curr[1] < new_interval[0]:
                solution.append(curr)
                curr = new_interval
            
            # if the curr end >= new_interval start we have an overlap
            # set the curr end = max between curr.end and new_interval.end
            curr[1] = max(curr[1], new_interval[1])
            i+=1
        
        # We only add in a previous interval to the solution array
        # we never added the curr interval to the solution set so we have to remember to add it before returning the result.
        solution.append(curr)
        return solution