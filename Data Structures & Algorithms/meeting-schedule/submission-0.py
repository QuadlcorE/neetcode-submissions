"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # can a person attend both meetings if one ends at x and the next starts at x?
        # if the array has no element we want to return True
        if len(intervals) < 2:
            return True
        # Simply loop through all intervals and check if any overlap
        intervals.sort(key=lambda x: x.start)

        prev = intervals[0].end
        curr = 1
        while curr < len(intervals):
            # What do we need to do here?
            # We need to make sure the prev is not overlapping
            if intervals[curr].start < prev:
                return False
            prev = intervals[curr].end
            curr +=1
        return True