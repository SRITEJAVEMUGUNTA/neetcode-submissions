"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)

        prevInterval = intervals[0]
        

        for curInterval in intervals[1:]:
            if curInterval.start < prevInterval.end:
                return False
            
            prevInterval = curInterval
        return True