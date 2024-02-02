START, END = 0, 1
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        stack = []
        for interval in intervals:
            if stack and self.overlapping(stack[-1], interval):
                minimum = min(stack[-1][START], interval[START])
                maximum = max(stack[-1][END], interval[END])
                interval = (minimum, maximum)
                stack[-1] = interval
            else:
                stack.append(interval)
        return stack
    
    def overlapping(self, a, b):
        return b[START] <= a[END] and a[START] <= b[END]