VALUE, TIMESTAMP, NO_DATA = 0, 1, ""
class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append( (value, timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        if (
            not key in self.time_map 
            or timestamp < (timestamps := self.time_map[key])[0][TIMESTAMP]
        ): return NO_DATA
        
        left, right = 0, len(timestamps) - 1
        while left < right:
            upper_bound = (left + right + 1) >> 1

            if timestamp < timestamps[upper_bound][TIMESTAMP]:
                right = upper_bound - 1
            else:
                left = upper_bound
        return timestamps[left][VALUE]


    
# tm = TimeMap()

# tm.set('foo', 'bar', 1)
# print(tm.get('foo', 1))
# print(tm.get('foo', 3))

# tm.set('foo', 'bar2', 4)
# print(tm.get('foo', 4))
# print(tm.get('foo', 5))