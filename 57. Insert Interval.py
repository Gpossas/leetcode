START, END = 0, 1

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        length = len(intervals)
        index = 0

        # insert all intervals smaller than new interval
        while (
            index < length
            and intervals[index][END] < newInterval[START]
        ):
            result.append(intervals[index])
            index += 1
        

        # merge intervals
        while (
            index < length
            and self.is_overlapping(intervals[index], newInterval)
        ):
            minimum = min(intervals[index][START], newInterval[START])
            maximum = max(intervals[index][END], newInterval[END])
            newInterval = [minimum, maximum]
            index += 1

        result.append(newInterval)


        # insert all the rest of intervals (bigger than new interval)
        while index < length:
            result.append(intervals[index])
            index += 1

        return result

    def is_overlapping(self, a, b):
        return b[START] <= a[END] and a[START] <= b[END]