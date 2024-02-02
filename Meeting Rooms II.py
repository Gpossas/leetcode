class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start_intervals = sorted([interval.start for interval in intervals])
        end_intervals = sorted([interval.end for interval in intervals])
        
        rooms, ongoing = 0, 0
        start, end = 0, 0
        while start < len(start_intervals):
            if start_intervals[start] < end_intervals[end]:
                ongoing += 1
                start += 1
                rooms = max(rooms, ongoing)
            else:
                ongoing -= 1
                end += 1
            
        return rooms