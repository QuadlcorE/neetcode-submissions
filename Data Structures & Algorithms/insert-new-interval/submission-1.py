class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # I just need to insert the interval and check if it creates an overlap?
        # Insertion is O(n) deletion is also O(n)
        # I simply need to find where the new interval is and check overlaps after insertion till the end of the array. 
        # What happens when I need to delete multiple intervals? 
        # I would much rather create a new array and simply append to list than have to delete multiple elements
        # Do I need to return intervals or can I return a new array?
        # just go through intervals and insert when it's time to insert. 

        # Firstly I'd solve it in place which is O(n*n)
        i = 0
        # No instead how about we just look for the insertion point first
        while i < len(intervals):
            # we just break so i would be at the insertion point always
            # what do we compare? 
            # simply we make 2 checks 
            # curr, inst
            # is inst.end < curr.start: if true insert isnt before curr
            # is inst.start <= curr.end: Then we know there is an overlap
            #    2      5
            # [[1,3],[4,6],[7,9]] [2,5]
            #    23
            # [[1,3],[4,6],[7,9]] [2,3]
            #    2           10
            # [[1,3],[4,6],[7,9]] [2,10]
            #       34 
            # [[1,2],,[5,6],[7,9]] [3,4]
            #  12
            # [ ,[3,4],[5,6],[7,9]] [1,2]
            # check if the start overlaps 

            if newInterval[1] < intervals[i][0] or newInterval[0] <= intervals[i][1]:
                break
            i+=1
        
        intervals.insert(i, newInterval)
        
        # now just merge the intervals. 
        curr = i 
        count = len(intervals)
        i+=1
        while i < count:
            print(curr, " ", i, " ", count)
            if intervals[curr][1] < intervals[i][0]:
                
                break
            intervals[curr][0] = min(intervals[curr][0], intervals[i][0])
            intervals[curr][1] = max(intervals[curr][1], intervals[i][1])
            del intervals[i]
            count -=1
        
        return intervals
        # now would be collapsing all other points
        # i
        # we would insert at i 
        # start collapsing from i - 1 if there is i-1
        
        # collapsing is basically merge intervals.