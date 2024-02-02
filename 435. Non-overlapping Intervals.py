START, END = 0, 1
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[START])

        removed_intervals = 0
        minimum_end = intervals[START][END]
        for start, end in intervals[1:]:
            if self.is_overlapping(start, minimum_end):
                removed_intervals += 1
                minimum_end = min(end, minimum_end)
            else:
                minimum_end = end
        return removed_intervals
    
    def is_overlapping(self, start, minimum_end):
        return start < minimum_end