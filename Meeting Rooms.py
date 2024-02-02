"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        for index in range(len(intervals) - 1):
            if intervals[index + 1].start < intervals[index].end:
                return False
        return True